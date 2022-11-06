from src.main.data.database.student_data_source import StudentDataSource
from src.main.domain.repository.student_repository import StudentRepository


class StudentRepositoryImpl(StudentRepository):
    def __init__(self, data_source: StudentDataSource):
        self.data_source = data_source
