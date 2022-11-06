from src.main.data.book_repository_impl import BookRepositoryImpl
from src.main.data.database.book_data_source import BookDataSource
from src.main.data.database.database import Database
from src.main.data.database.seat_data_source import SeatDataSource
from src.main.data.database.student_data_source import StudentDataSource
from src.main.data.seat_repository_impl import SeatRepositoryImpl
from src.main.data.student_repository_impl import StudentRepositoryImpl
from src.main.domain.repository.book_repository import BookRepository
from src.main.domain.repository.seat_repository import SeatRepository
from src.main.domain.repository.student_repository import StudentRepository
from src.main.domain.usecase.book.search_usecase import SearchUseCase
from src.main.domain.usecase.seat.cancel_seat_usecase import CancelSeatUseCase
from src.main.domain.usecase.seat.extend_seat_usecase import ExtendSeatUseCase
from src.main.domain.usecase.seat.get_all_seat_info_usecase import GetAllSeatInfoUseCase
from src.main.domain.usecase.seat.get_reservation_info_usecase import GetReservationInfoUseCase
from src.main.domain.usecase.seat.get_seat_info_usecase import GetSeatInfoUseCase
from src.main.domain.usecase.seat.reserve_seat_usecase import ReserveSeatUseCase
from src.main.domain.usecase.student.get_student_info_usecase import GetStudentInfoUseCase
from src.main.domain.usecase.student.login_usecase import LoginUseCase
from src.main.domain.usecase.student.logout_usecase import LogoutUseCase


class LibraryModule:
    def __init__(self):
        self.__database: Database = Database().get_instance()

        # DataSource
        self.__student_data_source: StudentDataSource = StudentDataSource(database=self.__database)
        self.__seat_data_source: SeatDataSource = SeatDataSource(database=self.__database)
        self.__book_data_source: BookDataSource = BookDataSource(database=self.__database)

        # Repository
        self.__student_repository: StudentRepository = StudentRepositoryImpl(data_source=self.__student_data_source)
        self.__seat_repository: SeatRepository = SeatRepositoryImpl(data_source=self.__seat_data_source)
        self.__book_repository: BookRepository = BookRepositoryImpl(data_source=self.__book_data_source)

        # Student UseCase
        self.login_usecase: LoginUseCase = LoginUseCase(repository=self.__student_repository)
        self.logout_usecase: LogoutUseCase = LogoutUseCase(repository=self.__student_repository)
        self.get_student_info_usecase: GetStudentInfoUseCase = GetStudentInfoUseCase(repository=self.__student_repository)

        # Seat UseCase
        self.get_all_seat_info_usecase: GetAllSeatInfoUseCase = GetAllSeatInfoUseCase(repository=self.__seat_repository)
        self.get_seat_info_usecase: GetSeatInfoUseCase = GetSeatInfoUseCase(repository=self.__seat_repository)
        self.reserve_seat_usecase: ReserveSeatUseCase = ReserveSeatUseCase(repository=self.__seat_repository)
        self.cancel_seat_usecase: CancelSeatUseCase = CancelSeatUseCase(repository=self.__seat_repository)
        self.extend_seat_usecase: ExtendSeatUseCase = ExtendSeatUseCase(repository=self.__seat_repository)
        self.get_reservation_info_usecase: GetReservationInfoUseCase = \
                                                        GetReservationInfoUseCase(repository=self.__seat_repository)

        # Book UseCase
        self.search_usecase: SearchUseCase = SearchUseCase(repository=self.__book_repository)
