from src.main.data.database.database import Database
from src.main.data.model.student_model import StudentModel


class StudentDataSource:
    def __init__(self, database: Database):
        self.__database = database

    def get_all_student(self) -> list:
        query = self.__database.db.query(StudentModel)
        return query

    def get_student(self, id: str) -> StudentModel:
        query = self.__database.db.query(StudentModel).filter(StudentModel.id == id).first()
        return query

    def add_student(
            self, id: str, password: str, student_id: str, department: str, name: str, is_attending: bool, qr: str
    ) -> bool:
        student = StudentModel(id, password, student_id, department, name, is_attending, qr)
        try:
            self.__database.db.add(student)
            self.__database.db.commit()
        except Exception:
            return False
        return True
