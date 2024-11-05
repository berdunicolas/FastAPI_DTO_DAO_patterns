from datetime import datetime
from pydantic import BaseModel, Field

class UpdateCourseDTO(BaseModel):
    name: str    