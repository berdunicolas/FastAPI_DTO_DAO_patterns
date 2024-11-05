from datetime import datetime
from sqlalchemy.orm import Session
from typing import List
from app.daos import CourseDAO
from app.dtos import CourseDTO, CreateCourseDTO, UpdateCourseDTO

class CourseService():
    
    def get_all_courses(db:Session) -> List[CourseDTO]:
        courses = CourseDAO.get_all(db=db)
        return [CourseDTO.model_validate(course) for course in courses]
    
    def get_courses_page(db:Session, page: int = 1, size: int = 10) -> List[CourseDTO]:
        courses = CourseDAO.get_paginated(db=db, page=page, size=size)
        
        return [CourseDTO.model_validate(course) for course in courses]

    def create_course(db:Session, course_payload:CreateCourseDTO) -> CourseDTO:
        course = CourseDAO.create(data=course_payload.model_dump(), db=db)
        return CourseDTO.model_validate(course)
    
    def get_course(db:Session, id:int) -> CourseDTO:
        return CourseDAO.get_by_id(id, db=db)
    
    def update_course(db:Session, id:int, course_payload:UpdateCourseDTO):
        data=course_payload.model_dump()
        data["updated_at"] = datetime.now()

        return CourseDAO.update(id, data, db)
    
    def delete_course(db:Session, id:int):
        CourseDAO.delete(id, db=db)