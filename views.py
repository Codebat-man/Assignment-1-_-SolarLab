from django.shortcuts import render

# Create your views here.
import requests
from bs4 import BeautifulSoup
from rest_framework import status
from rest_framework.response import Response
from .serializers import CountryInfoSerializer

def country_info(request, country_name):
    # Make an HTTP GET request to the Wikipedia page for the specified country
    url = f'https://en.wikipedia.org/wiki/{country_name}'
    response = requests.get(url)
    html = response.text

    # Parse the HTML of the page using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Extract relevant information from the page using BeautifulSoup
    flag_link = soup.select_one('.infobox .image img')['src']
    capital_tags = soup.select('.infobox td:contains("Capital") + td')
    if len(capital_tags) > 1:
        # Country has multiple capitals, return a list of all capital names
        capital = [tag.text for tag in capital_tags]
    else:
        # Country has one capital, return the capital name as a string
        capital = capital_tags[0].text if capital_tags else ''
    largest_city_tags = soup.select('.infobox td:contains("Largest city") + td a')
    largest_city = [tag.text for tag in largest_city_tags]
    official_language_tags = soup.select('.infobox td:contains("Official language") + td a')
    if len(official_language_tags) == 1:
        # Country has one official language, return the language name as a string
        official_languages = official_language_tags[0].text
    else:
        # Country has multiple official languages, return a list of all language names
        official_languages = [tag.text for tag in official_language_tags]
    area_total_tag = soup.select_one('.infobox td:contains("Area") + td')
