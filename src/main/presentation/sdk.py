from src.main.di.library_module import LibraryModule


class SDK:
    __instance = None

    @classmethod
    def get_instance(cls):  # Singleton
        if not cls.__instance:
            cls.__instance = SDK()
        return cls.__instance

    def __init__(self):
        self.library_module = LibraryModule()
