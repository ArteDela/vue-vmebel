from db import db
from models.base_model import BaseModel

class MailingList(BaseModel):
	email = db.Column(db.String(255))

	def __init__(self, email):
		self.email = email
	def json(self):
		return {
			'email': self.email
		}
