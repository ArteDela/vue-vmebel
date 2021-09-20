from db import db
from models.base_model import BaseModel

class PropertiesValues(BaseModel):
	id                = db.Column(db.Integer, primary_key=True)
	value             = db.Column(db.String(200))
	property_id       = db.Column(db.Integer, db.ForeignKey('properties.id'))
	property          = db.relationship('Properties', back_populates='values')

	def json(self):
		result = {
			'value': self.value,
			'name': self.property.name if self.property else None,
		}
		type_conversion = {
			'FLAG': lambda x: bool(x),
			'INT': lambda x: float(x),
		}
		if self.property and self.property.type and self.property.type in type_conversion:
			result['value'] = type_conversion[self.property.type](result['value'])

		return result
