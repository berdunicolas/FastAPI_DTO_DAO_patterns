from pydantic import BaseModel

class CreateCourseDTO(BaseModel):
    name: str
    