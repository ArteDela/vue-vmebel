from db import db
from models.base_model import BaseModel
import math

class ProductsCategories(BaseModel):
	id          = db.Column(db.Integer, primary_key=True)
	name        = db.Column(db.String(200))
	description = db.Column(db.Text)
	picture     = db.Column(db.Text)
	slug        = db.Column(db.String(100))
	parent_id   = db.Column(db.Integer, db.ForeignKey('products_categories.id'))
	parent      = db.relationship('ProductsCategories', remote_side=[id], backref='children')
	products    = db.relationship('Products', back_populates='category')

	def get_url(self):
		return '/category/%s?page=1' % self.id

	def json(self):
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'picture': self.picture,
			'parent_id': self.parent_id,
			'parent': self.parent.json() if self.parent else None,
			'slug': self.slug,
			'url': self.get_url(),
			'children': [ child.get_common_data() for child in self.children],
		}

	def get_common_data(self, fetch_children=True, fetch_children_recursively=False, fetch_parent=False):
		common_data = {
			'id': self.id,
			'name': self.name,
			'url': self.get_url(),
			'picture': self.picture,
		}

		if fetch_children:
			common_data['children'] = [ child.get_common_data(fetch_children_recursively, fetch_children_recursively) for child in self.children ] if self.children else None
		if fetch_parent:
			common_data['parent'] = self.parent.get_common_data(False) if self.parent else None

		return common_data

	def get_search_data(self, search):
		return {
			'id': self.id,
			'url': self.get_url(),
			'name': self.name,
			'products': [product.get_common_data() for product in self.products if (not search or (product.name and product.name.find(search) != -1))],
		}
		#

	def get_detail_data(self, page_number, limit):
		first_in_page_index = (page_number-1)*limit
		last_page = int(math.ceil(len(self.products)/limit))
		next_page = page_number + 1 if page_number < last_page else last_page
		previous_page = (next_page - 1 if next_page > 1 else 1) if next_page == last_page else (next_page - 2 if next_page > 2 else 1)
		return {
			'id': self.id,
			'name': self.name,
			'description': self.description,
			'parent': self.parent.get_common_data(False) if self.parent else None,
			'products': [product.get_common_data() for product in self.products[first_in_page_index:first_in_page_index+limit]],
			'paging': {
				'current': page_number,
				'previous': previous_page,
				'next': next_page,
				'first': 1,
				'last': last_page,
				'limit': limit,
				'total_pages': last_page,
				'total_items': len(self.products),
			},
		}
