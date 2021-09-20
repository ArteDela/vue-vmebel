from db import db
from models.base_model import BaseModel

class Brands(BaseModel):
	name  = db.Column(db.String(200))
	site  = db.Column(db.String(200))
	shops = db.relationship('Shops', back_populates='brand')

	def json(self):
		return {
			'name': self.name,
			'site': self.site,
			'shops': [shop.json() for shop in self.shops],
		}
