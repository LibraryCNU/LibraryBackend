from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Database:
    __instance = None
    # TODO __connect_info = "write your db connection information"
    __connect_info = "mariadb+pymysql://root2:1q2w3e4r@122.32.102.102:46577/library"

    @classmethod
    def get_instance(cls):  # Singleton
        if not cls.__instance:
            cls.__instance = Database()
        return cls.__instance

    def __init__(self):
        self.engine = create_engine(self.__connect_info, echo=True)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.db = SessionLocal()
        Base.metadata.create_all(self.engine)
