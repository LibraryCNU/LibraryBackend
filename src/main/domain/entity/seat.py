from datetime import datetime


class Seat:
    def __init__(
            self, id: int, place: str, plug_existence: bool, start_time: datetime, end_time: datetime,
            can_reserve: bool, is_favorite: bool
    ) -> None:
        self.id = id
        self.place = place
        self.plug_existence = plug_existence
        self.start_time = start_time
        self.end_time = end_time
        self.can_reserve = can_reserve
        self.is_favorite = is_favorite

    def to_dict(self):
        return {
            "id": self.id,
            "place": self.place,
            "plug_existence": self.plug_existence,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "can_reserve": self.can_reserve,
            "is_favorite": self.is_favorite,
        }
