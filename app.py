from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from src.main.presentation.student_api import *
from src.main.presentation.seat_api import *
from src.main.presentation.book_api import *

app = Flask(__name__)
api = Api(app)
CORS(app)


api.add_resource(GetStudentInfo, "/get_student_info")
api.add_resource(GetAllSeatInfo, "/get_all_seat_info")
api.add_resource(GetSeatInfo, "/get_seat_info")
api.add_resource(ReserveSeat, "/reserve_seat")
api.add_resource(CancelSeat, "/cancel_seat")
api.add_resource(ExtendSeat, "/extend_seat")
api.add_resource(GetReservationInfo, "/get_reservation_info")
api.add_resource(Search, "/book_search")


@app.route('/')
def hello_world():  # test route.
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
