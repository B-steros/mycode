"""Star Wars API HTTP response parsing"""

#pprint makes dictionaries a lot more human readable
from pprint import pprint

#requests is used to send HTTP requests
import requests


URL = "https://swapi.info/api/people/4"

def main():
    """Sending GET request, checking response"""

    #SWAPI response is stored in "resp" object
    resp = requests.get(URL)

    #conver the JSON content of the response into a python dictionary
    vader = resp.json()

    pprint(vader)

if __name__== "__main__":
    main()
