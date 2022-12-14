from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Database:
    __instance = None
    # TODO __connect_info = "write your db connection information"
    __connect_info = ""

    @classmethod
    def get_instance(cls):  # Singleton
        if not cls.__instance:
            cls.__instance = Database()
        return cls.__instance

    def __init__(self):
        self.engine = create_engine(self.__connect_info, echo=True, pool_recycle=1800)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.db = SessionLocal()
        Base.metadata.create_all(self.engine)
