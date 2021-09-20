from db import db
from models.base_model import BaseModel

class BrandsRequests(BaseModel):
    phone = db.Column(db.String(100))
    is_active = db.Column(db.Integer)

    def __init__(self, phone):
        self.phone = phone
        self.is_active = 1

    def json(self):
        return {
            'phone': self.phone,
            'is_active': self.is_active,
        }
