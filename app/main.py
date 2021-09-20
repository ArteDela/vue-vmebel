from flask import Flask, jsonify, request, render_template
from flask_restful import Resource, Api

# resources
from resources.categories import Categories
from resources.category import Category
from resources.subscribe import Subscribe
from resources.subscribe_market import SubscribeMarket
from resources.products import Product
from resources.category_filters import CategoryFilters

app = Flask(__name__)
app.url_map.strict_slashes = False
ROOT = app.root_path

# get config
import json
with open('%s/config/config.json' % ROOT) as json_file:
	config = json.load(json_file)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{user}:{password}@{host}/{database}?charset=utf8mb4'.format(**config['mysql'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)


api.add_resource(
	Categories,
	'/categories',
	'/categories/'
)

api.add_resource(
	Category,
	'/category/<category_id>/',
	'/category/<category_id>',
)

api.add_resource(
	Product,
	'/product/<product_id>',
	'/product/<product_id>/'
)

api.add_resource(
	Subscribe,
	'/subscribe',
	'/subscribe/'
)

api.add_resource(
	SubscribeMarket,
	'/subscribe/market',
	'/subscribe/market/'
)

api.add_resource(
	CategoryFilters,
	'/category/<category_id>/filters',
	'/category/<category_id>/filters/',
)

@app.after_request
def set_default_headers(response):
	response.headers['Accept'] = 'application/json, */*; q=0.01'

	if response.status_code == 200 and response.data:
		response.headers['Content-Type'] = 'application/json; charset=UTF-8'
	return response

if (__name__ == '__main__'):
	from db import db
	db.init_app(app)
	app.run(port=5000, host='0.0.0.0')
