from fastapi import Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from app.dtos import CourseDTO, CreateCourseDTO, UpdateCourseDTO
from app.services import CourseService
from app.db import get_db
from app.models import Course
from app.daos import CourseDAO

class CourseController:
    """ 
    def _get_course(id:int, db:Session = Depends(get_db)) -> Course:
        course = CourseDAO.get_by_id(id, db)

        if course is None:
            raise HTTPException(status_code=404, detail="Item not found")
        
        return course """

    async def list(db:Session = Depends(get_db), page:int = 1, size:int = 10) -> List[CourseDTO]:
        return CourseService.get_courses_page(db=db, page=page, size=size)

    async def create(payload: CreateCourseDTO, db:Session = Depends(get_db)) -> CourseDTO:
        return CourseService.create_course(db=db, course_payload=payload)

    async def detail(id:int, db:Session = Depends(get_db)) -> CourseDTO:
        return CourseService.get_course(db=db, id=id)

    async def update(id:int, payload:UpdateCourseDTO, db:Session = Depends(get_db)) -> CourseDTO:
        return CourseService.update_course(db=db, id=id, course_payload=payload)

    async def destroy(id:int, db:Session = Depends(get_db)):
        return CourseService.delete_course(db=db, id=id)
