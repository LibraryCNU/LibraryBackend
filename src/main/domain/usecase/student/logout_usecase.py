from src.main.domain.repository.student_repository import StudentRepository


class LogoutUseCase:
    def __init__(self, repository: StudentRepository):
        self.repository = repository

    def execute(self, session: str) -> bool:
        return self.repository.logout(session=session)
