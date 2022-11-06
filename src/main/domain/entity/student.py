class Student:
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
