from db import db
from models.base_model import BaseModel

class Properties(BaseModel):
	id        = db.Column(db.Integer, primary_key=True)
	name      = db.Column(db.String(200))
	type      = db.Column(db.Enum('STRING','FLAG','INT','TEXT','IMAGE','JSON'))
	parent_id = db.Column(db.Integer, db.ForeignKey('properties.id'))
	parent    = db.relationship('Properties', remote_side=[id], backref='children')
	values    = db.relationship('PropertiesValues', back_populates='property')

	def json(self, need_values=True):
		return {
			'name': self.name,
			'parent': self.parent.json() if self.parent else None,
			'type': self.type,
			'values': [value.json() for value in self.values] if need_values else None,
		}
