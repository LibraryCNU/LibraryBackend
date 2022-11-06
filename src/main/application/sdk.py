from src.main.di.library_module import LibraryModule


class SDK:
    def __init__(self):
        self.library_module = LibraryModule()
        print(self.library_module.get_all_seat_info_usecase.execute()[0].to_dict())


sdk = SDK()
