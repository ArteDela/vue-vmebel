from db import db
from models.base_model import BaseModel

class Shops(BaseModel):
	name     = db.Column(db.String(255))
	address  = db.Column(db.String(255))
	brand_id = db.Column(db.Integer, db.ForeignKey('brands.id'))
	brand    = db.relationship('Brands', back_populates='shops')

	def json(self):
		return {
			'name': self.name,
			'address': self.address,
		}
