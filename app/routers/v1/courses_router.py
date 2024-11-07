from fastapi import APIRouter
from app.controllers.v1 import CourseController

class CoursesRouter:
    def __init__(cls):
        cls.router = APIRouter(prefix="/courses", tags=["Courses"])

        cls.router.add_api_route("", CourseController.list, methods=["GET"])
        cls.router.add_api_route("", CourseController.create, methods=["POST"])
        cls.router.add_api_route("/{id}", CourseController.detail, methods=["GET"])
        cls.router.add_api_route("/{id}", CourseController.update, methods=["PUT"])
        cls.router.add_api_route("/{id}", CourseController.destroy, methods=["DELETE"])
