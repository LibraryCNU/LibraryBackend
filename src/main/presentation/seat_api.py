from flask_restful import Resource, reqparse

from src.main.presentation.sdk import SDK


class GetAllSeatInfo(Resource):
    def __init__(self):
        self.sdk = SDK()

    def get(self):
        try:
            seats = self.sdk.library_module.get_all_seat_info_usecase.execute()
            seat_list = []
            for seat in seats:
                seat.start_time = seat.start_time.strftime("%Y-%m-%dT%H:%M:%S")
                seat.end_time = seat.end_time.strftime("%Y-%m-%dT%H:%M:%S")
                seat_list.append(seat.to_dict())

            return seat_list

        except Exception as e:
            return {'error': str(e)}


class GetSeatInfo(Resource):
    def __init__(self):
        self.sdk = SDK()

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            args = parser.parse_args()

            _id = args['id']

            seat = self.sdk.library_module.get_seat_info_usecase.execute(id=_id)
            seat.start_time = seat.start_time.strftime("%Y-%m-%dT%H:%M:%S")
            seat.end_time = seat.end_time.strftime("%Y-%m-%dT%H:%M:%S")

            return seat.to_dict()

        except Exception as e:
            return {'error': str(e)}


class ReserveSeat(Resource):
    def __init__(self):
        self.sdk = SDK()

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            parser.add_argument('place', type=str)
            args = parser.parse_args()

            _id = args['id']
            _place = args['place']

            result = self.sdk.library_module.reserve_seat_usecase.execute(id=_id, place=_place)

            return {'result': result}

        except Exception as e:
            return {'error': str(e)}


class CancelSeat(Resource):
    def __init__(self):
        self.sdk = SDK()

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            parser.add_argument('place', type=str)
            args = parser.parse_args()

            _id = args['id']
            _place = args['place']

            result = self.sdk.library_module.cancel_seat_usecase.execute(id=_id, place=_place)

            return {'result': result}

        except Exception as e:
            return {'error': str(e)}


class ExtendSeat(Resource):
    def __init__(self):
        self.sdk = SDK()

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            parser.add_argument('place', type=str)
            args = parser.parse_args()

            _id = args['id']
            _place = args['place']

            result = self.sdk.library_module.extend_seat_usecase.execute(id=_id, place=_place)

            return {'result': result}

        except Exception as e:
            return {'error': str(e)}


class GetReservationInfo(Resource):
    def __init__(self):
        self.sdk = SDK()

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            parser.add_argument('place', type=str)
            args = parser.parse_args()

            _id = args['id']
            _place = args['place']

            reservation_info = self.sdk.library_module.get_reservation_info_usecase.execute(id=_id, place=_place)
            reservation_info['start_time'] = reservation_info['start_time'].strftime("%Y-%m-%dT%H:%M:%S")
            reservation_info['end_time'] = reservation_info['end_time'].strftime("%Y-%m-%dT%H:%M:%S")

            return reservation_info

        except Exception as e:
            return {'error': str(e)}
