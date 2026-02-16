import os
import logging

import aiofiles
from controllers import DataController, ProjectController, ProcessController
from helpers.config import get_settings, Settings

from fastapi import FastAPI, APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse

from models import ResponseSignals

from .schemas.data import ProcessRequest

logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)


@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,\
                      app_settings:Settings = Depends(get_settings)):
    
    # input file validation
    data_controller = DataController()
    is_valid, result_signal = data_controller.validate_uploaded_file(file=file)

    if is_valid == False:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "signal": result_signal
            }
        )
    project_dir_path = ProjectController().get_project_path(project_id=project_id)
    #file_path = os.path.join(project_dir_path, file.filename)
    file_path, file_id= data_controller.generate_unique_filepath(
        orig_file_name=file.filename,
        project_id=project_id
    )
    try:
        async with aiofiles.open(file_path, 'wb') as f:
            while chunk := await file.read(app_settings.FILE_DEFAULT_CHUNCK_SIZE):
                await f.write(chunk)
    except Exception as e:
        logger.error(f"Error while file upload: {e}")
        return JSONResponse(
        status_code = status.HTTP_400_BAD_REQUEST,
        content={
            "signal": ResponseSignals.FILE_UPLOAD_FAILED.value
        })


    return JSONResponse(
        content={
            "signal": ResponseSignals.FILE_UPLOAD_SUCCESS.value,
            "file_id": file_id
        }
    )
@data_router.post("/process/{project_id}")
async def process_endpoint(project_id:str, process_request: ProcessRequest):
    file_id = process_request.file_id
    chunck_size = process_request.chunck_size
    overlap_size = process_request.overlap_size
    
    process_controller = ProcessController(project_id=project_id)

    file_content = process_controller.get_file_content(file_id=file_id)

    file_chuncks = process_controller.process_file_content(
        file_content=file_content,
        file_id=file_id,

    )

    if file_chuncks is None or len(file_chuncks) == 0:
        return JSONResponse(
        status_code = status.HTTP_400_BAD_REQUEST,
        content={
            "signal": ResponseSignals.PROCESSING_FAILES.value
        })
    return file_chuncks