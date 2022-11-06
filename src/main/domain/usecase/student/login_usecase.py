from src.main.domain.repository.student_repository import StudentRepository


class LoginUseCase:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, id: str, password: str) -> bool:
        return self.repository.login(id=id, password=password)
