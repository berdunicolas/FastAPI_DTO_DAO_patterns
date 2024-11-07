from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import List
from app.daos import CourseDAO
from app.dtos import CourseDTO, CreateCourseDTO, UpdateCourseDTO
from app.models import Course

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
    
    def get_course(db:Session, id:int) -> CourseDTO | HTTPException:
        course = CourseDAO.get_by_id(id, db=db)
        if course is None:
            raise HTTPException(status_code=404, detail="Course not found")
        return 
    
    def update_course(db:Session, id:int, course_payload:UpdateCourseDTO) -> CourseDTO | HTTPException:
        data=course_payload.model_dump()

        query = select(Course).where(Course.name == data['name'], Course.id != id)
        name_exists = db.execute(query).first()

        if name_exists is not None:
            raise HTTPException(status_code=422, detail="El campo name deberia ser unico")

        data["updated_at"] = datetime.now()

        return CourseDAO.update(id, data, db)
    
    def delete_course(db:Session, id:int):
        CourseDAO.delete(id, db=db)