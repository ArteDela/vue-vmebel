import json
with open('config.json') as json_file:
	config = json.load(json_file)

class BaseTest:
	config = config
