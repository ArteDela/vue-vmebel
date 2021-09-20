import requests
from tests.base_test import BaseTest

class ProductsTests(BaseTest):
    def test_get(self):
        url = '{base_url}/product/{code}/'.format(base_url=self.config['base_url'],code=self.config['product_code'])
        response = requests.get(url)
        product = response.json()

        assert (
            product
            and 'id' not in product
            and 'name' in product
            and 'images' in product
            and 'vendor_code' in product
            and 'description' in product
            and 'properties' in product
            and 'shops' in product
            and 'category' in product
        )

    def test_get_invalid(self):
        url = '{base_url}/product/{code}'.format(base_url=self.config['base_url'],code='none')
        response = requests.get(url)
        assert response.status_code == 404
