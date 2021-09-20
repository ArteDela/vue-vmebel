import requests
from tests.base_test import BaseTest

class SubscribeTests(BaseTest):
	def test_post(self):
		url = '%s/subscribe' % self.config['base_url']
		response = requests.post(url, data={'email': 'validemail@gmail.com'})
		assert response.status_code == 200

	def test_invalid_post(self):
		url = '%s/subscribe' % self.config['base_url']
		response = requests.post(url, data={'email': 'notvalidemail'})
		assert response.status_code == 400

	def test_empty_post(self):
		url = '%s/subscribe' % self.config['base_url']
		response = requests.post(url)
		assert response.status_code == 400
