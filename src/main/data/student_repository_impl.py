from src.main.data.database.student_data_source import StudentDataSource
from src.main.domain.entity.student import Student
from src.main.domain.repository.student_repository import StudentRepository


class StudentRepositoryImpl(StudentRepository):
    def __init__(self, data_source: StudentDataSource):
        self.data_source = data_source

    def login(self, id: str, password: str) -> bool:
        pass

    def logout(self, session: str) -> bool:
        pass

    def get_student_info(self, id: str) -> Student:
        student_model = self.data_source.get_student(id=id)
        if not student_model:
            return None
        student = Student(*student_model.to_dict().values())
        return student
