from flask_restful import Resource
from models import *

class Categories(Resource):
    def get(self):
        categories = ProductsCategories.find({})
        return [category.get_common_data(fetch_children=True, fetch_children_recursively=True) for category in categories if (category and category.children)], 200
