from db import db
from models.base_model import BaseModel

products_properties_values = db.Table('products_properties_values',
    db.Column('product_id',db.Integer, db.ForeignKey('products.id')),
    db.Column('property_value_id',db.Integer, db.ForeignKey('properties_values.id')),
)

class Products(BaseModel):
	name              = db.Column(db.String(200))
	slug              = db.Column(db.String(200))
	description       = db.Column(db.Text)
	remote_url        = db.Column(db.String(200))
	price             = db.Column(db.Integer)
	brand_id          = db.Column(db.Integer, db.ForeignKey('brands.id'))
	brand             = db.relationship('Brands')
	category_id       = db.Column(db.Integer, db.ForeignKey('products_categories.id'))
	category          = db.relationship('ProductsCategories', back_populates='products')
	parsed            = db.Column(db.Boolean)
	picture           = db.Column(db.Text)
	images            = db.Column(db.Text)
	vendor_code       = db.Column(db.String(200))
	properties_values = db.relationship('PropertiesValues', secondary=products_properties_values)

	def get_url(self):
		return '/product/%s/' % self.id

	def json(self):
		return {
			'name': self.name,
			'slug': self.slug,
			'description': self.description,
			'url': self.get_url(),
			'remote_url': self.remote_url,
			'price': self.price,
			'category_id': self.category_id,
			'category': self.category.json() if self.category else None,
			'parsed': self.parsed,
			'picture': self.picture,
			'images': self.images,
			'vendor_code': self.vendor_code,
			'properties': [property_value.json(need_property_value=True) for property_value in self.properties_values] if self.properties_values else None,
		}

	def get_common_data(self):
		return {
			'id': self.id,
			'name': self.name,
			'picture': self.picture,
			'url': self.get_url(),
			'price': self.price,
			'shops_count': len(self.brand.shops) if self.brand else 0,
		}

	def get_detail_data(self):
		return {
			'id': self.id,
			'name': self.name,
			'images': self.images,
			'vendor_code': self.vendor_code,
			'description': self.description,
			'properties': [property_value.json() for property_value in self.properties_values] if self.properties_values else None,
			'shops': [shop.json() for shop in self.brand.shops] if self.brand else None,
			'category': self.category.get_common_data(fetch_children=False,fetch_parent=True) if self.category else None,
		}
