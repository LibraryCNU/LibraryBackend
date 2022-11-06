from sqlalchemy import Column, String, Boolean

from src.main.data.database.database import Base


class StudentModel(Base):
    __tablename__ = 'student'
    id = Column(String(255), primary_key=True)
    password = Column(String(255))
    student_id = Column(String(10))
    department = Column(String(255))
    name = Column(String(255))
    is_attending = Column(Boolean)
    qr = Column(String(255))

    def __init__(
            self, id: str, password: str, student_id: str, department: str, name: str, is_attending: bool, qr: str
    ) -> None:
        self.id = id
        self.password = password
        self.student_id = student_id
        self.department = department
        self.name = name
        self.is_attending = is_attending
        self.qr = qr

    def to_dict(self):
        return {
            "id": self.id,
            "password": self.password,
            "student_id": self.student_id,
            "department": self.department,
            "name": self.name,
            "is_attending": self.is_attending,
            "qr": self.qr,
        }
