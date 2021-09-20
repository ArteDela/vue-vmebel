from flask_restful import Resource
from models import *

class Product(Resource):
    def get(self, product_id):
        product = Products.find_first({ 'id': product_id })
        if not product:
            return {'message': 'Продукт не найден', 'code': 'empty_product'}, 404
        return product.get_detail_data(), 200
