from flask_restful import Resource, reqparse

from src.main.presentation.sdk import SDK


class Search(Resource):
    def __init__(self):
        self.sdk = SDK()

    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('query', type=str)
            args = parser.parse_args()

            _query = args['query']

            self.sdk.library_module.search_usecase.execute()

            return "Not implemented"

        except Exception as e:
            return {'error': str(e)}
