from src.main.domain.entity.student import Student
from src.main.domain.repository.student_repository import StudentRepository


class GetStudentInfoUseCase:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, id: str) -> Student:
        return self.repository.get_student_info(id=id)
