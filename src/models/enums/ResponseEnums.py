from enum import Enum


class ResponseSignals(Enum):


    FILE_VALIDATED_SUCCESS = "file_validated_susscessfully"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_SIZE_EXCEEDED= "file_size_exceeded"
    FILE_UPLOAD_SUCCESS = "file_uploaded_susscessfully"
    FILE_UPLOAD_FAILED = "file_uploaded_failed"

    PROCESSING_FAILES = "file processeing failed"
    PROCESSING_SUCCESS = "file processeing success"

    NO_FILES_ERROR = "files_are_not_found"
    FILE_ID_ERROR = "no_file_found_with_this_id"
    