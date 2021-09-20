import requests
from tests.base_test import BaseTest

class CategoriesTests(BaseTest):
    def test_get(self):
        url = '{base_url}/categories/'.format(base_url=self.config['base_url'])
        response = requests.get(url)
        categories = response.json()
        assert (
            categories
            and isinstance(categories, list)
        )

    def test_get_category_structure(self):
        url = '{base_url}/categories'.format(base_url=self.config['base_url'])
        response = requests.get(url)
        categories = response.json()
        if (categories):
            category = categories[0]
        assert (
            category
            and 'id' not in category
            and 'name' in category
            and 'url' in category
            and 'picture' in category
            and 'children' in category
        )

class CategoryTests(BaseTest):
    def test_get(self):
        url = '{base_url}/category/{category}/page/1'.format(base_url=self.config['base_url'], category=self.config['category_code'])
        response = requests.get(url)
        category = response.json()

        assert (
            category
            and 'id' not in category
            and 'name' in category
            and 'description' in category
            and 'page' in category
            and 'parent' in category
            and 'products' in category
        )

    def test_get_invalid(self):
        url = '{base_url}/category/{category}/page/1'.format(base_url=self.config['base_url'], category='none')
        response = requests.get(url)
        assert response.status_code == 404
