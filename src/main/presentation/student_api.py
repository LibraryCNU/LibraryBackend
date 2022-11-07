from flask_restful import Resource, reqparse

from src.main.presentation.sdk import SDK


class GetStudentInfo(Resource):
    def __init__(self):
        self.sdk = SDK()

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('id', type=str)
            args = parser.parse_args()

            _id = args['id']

            student = self.sdk.library_module.get_student_info_usecase.execute(id=_id)

            return student.to_dict()

        except Exception as e:
            return {'error': str(e)}
