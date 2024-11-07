from pydantic import BaseModel, field_validator
from app.db import manageable_session_db
from app.daos import CourseDAO

class CreateCourseDTO(BaseModel):
    name: str

    @field_validator('name')
    @classmethod
    def name_exists(cls, value:str) -> str:
        with manageable_session_db() as db:
            if CourseDAO.filterBy("name", value, db):
                raise ValueError("El campo name deberia ser unico")
            else:
                return value