from flask_restful import Resource
from models import *
from db import db

class CategoryFilters(Resource):
	def get(self, category_id):
		category = ProductsCategories.find_first({ 'id': category_id })

		if not category:
			return {'message': 'Категория не найдена', 'code': 'empty_category'}, 400

		return self.get_filters(category_id), 200

	def get_filters(self, category_id):
		int_filters = db.session.execute(db
			.select(Properties.id, Properties.name, db.func.max(PropertiesValues.value).label('max'), db.func.min(PropertiesValues.value).label('min'))
			.join(Products.properties_values)
			.join(PropertiesValues.property)
			.where(Properties.type == 'INT')
			.where(Products.category_id == category_id)
			.group_by(Properties.name)
		)
		flag_filters = db.session.execute(db
			.select(Properties.id, Properties.name)
			.join(Products.properties_values)
			.join(PropertiesValues.property)
			.where(Properties.type == 'FLAG')
			.where(Products.category_id == category_id)
			.group_by(Properties.name)
		)
		string_filters = db.session.execute(db
			.select(Properties.id, Properties.name, PropertiesValues.value)
			.join(Products.properties_values)
			.join(PropertiesValues.property)
			.where(Properties.type == 'STRING')
			.where(Products.category_id == category_id)
			.group_by(Properties.name)
			.group_by(PropertiesValues.value)
		)

		result = []
		result.extend([
			{
				"id": int_filter[0],
				"type": "INT",
				"min": float(int_filter[2].replace(',', '.')),
				"max": float(int_filter[3].replace(',', '.')),
				"title": int_filter[1],
			}
			for int_filter in int_filters
		])

		result.extend([
			{
				"id": flag_filter[0],
				"type": "FLAG",
				"title": flag_filter[1],
			}
			for flag_filter in flag_filters
		])

		string_test = {}
		for string_filter in string_filters:
			if string_filter[1] not in string_test:
				string_test[string_filter[1]] = {
					"id": string_filter[0],
					"type": "STRING",
					"title": string_filter[1],
					"values": [string_filter[2]],
				}
			else:
				string_test[string_filter[1]]['values'].append(string_filter[2])
		result.extend(list(string_test.values()))

		return sorted(result, key=lambda field: field['title'])

