from pydantic import BaseSettings, Field, validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseSettings):
    _id: Optional[ObjectId]
    project_id: str = Field(..., min_length=1)

    @validator('project_id')
    def validate_project_id(cls, value:str):
        if not value.isalnum():
            raise ValueError("field project_id must be alpha neumeric")
        return value
    
    class Config:
        arbitrary_types_allowed = True
        

