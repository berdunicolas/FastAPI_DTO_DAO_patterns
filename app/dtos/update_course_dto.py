from pydantic import BaseModel
from app.db import manageable_session_db
from app.daos import CourseDAO
from app.models import Course

class UpdateCourseDTO(BaseModel):
    name: str
""" 
    @classmethod
    def validate_name(cls, course:Course) -> bool:
        #name = cls.name
        print(cls.model_dump(self=cls)["name"])

        with manageable_session_db() as db:
            existing_course = CourseDAO.filterBy("name", name, db)

        if existing_course and existing_course.id != course.id:
            raise ValueError("El campo name deberia ser unico") """