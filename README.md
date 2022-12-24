# Assignment-1_SolarLab
Steps to  create an API using Django Rest Framework that scrapes information from Wikipedia's country pages and returns the data in JSON format : 
To Create a  virtual environment for the project  I have used use the venv module that comes with python. After activatinf this environment
Installed the required libraries for the project using pip - Django Rest Framework, and BeautifulSoup.
Created a serializer class in the app's serializers.py file to define the fields that will be included in the API's response.
Created a view class in the app's views.py file to handle the API request and scrape the data from the Wikipedia page. The view would use the BeautifulSoup library to parse the HTML of the page and extract the relevant information.
Defined a URL pattern in the app's urls.py file to specify the endpoint for the API. The endpoint should include a URL parameter for the country name.
And Test the API by making a request to the endpoint with a country name as the parameter.
