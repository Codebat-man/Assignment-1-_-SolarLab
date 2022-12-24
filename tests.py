

# Create your tests here.
import requests
from django.test import TestCase

class CountryInfoAPITestCase(TestCase):
    @classmethod
    def test_api(cls):
        # Make a request to the API endpoint
        response = requests.get('http://localhost:8000/country_info/india')

        # Check that the status code is 200
        assertEqual(response.status_code, 200)

        # Check that the response content is what we expect it to be
        expected_data = {
            'flag_link': 'https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg',
            'capital': 'New Delhi',
            'largest_city': ['Mumbai', 'New Delhi'],
            'official_languages': ['Hindi', 'English'],
            'area_total': 3287263,
            'population': '1,352,642,280',
            'GDP_nominal': ' $3.050 trillion',
        }
        assertEqual(response.json(), expected_data)

