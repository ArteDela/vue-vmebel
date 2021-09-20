from flask_restful import Resource, request, reqparse
from models import *
import json
parser = reqparse.RequestParser()

class Category(Resource):
    def get(self, category_id):
        parser.add_argument('page', type=int, location='args', default=0, ignore=True)
        parser.add_argument('limit', type=int, location='args', default=20, ignore=True)
        args = parser.parse_args()

        page = args['page']
        limit = args['limit'] if args['limit'] > 0 else 20

        if page < 1:
            return {'message': 'Некорректно задана страница', 'code': 'wrong_page'}, 400

        category = ProductsCategories.find_first({ 'id': category_id })

        if not category:
            return {'message': 'Категория не найдена', 'code': 'empty_category'}, 400

        return category.get_detail_data(page, limit), 200
