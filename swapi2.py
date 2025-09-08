from pprint import pprint
import requests

#URL = "https://swapi.info/luke/force"
URL = "https://swapi.info/api/people/4/"
URL2 = "https://swapi.info/api/films/1/"
URL3 = "https://swapi.info/api/starships/13/"

def main():

    resp = requests.get(URL)
    resp2 = requests.get(URL2)
    resp3 = requests.get(URL3)

    #check to see if the status code is anything other than what we want, a 200 OK
    if resp.status_code == 200:
        #convert the JSON content of the response into a python dictionary
        vader = resp.json()
        film = resp2.json()
        ship = resp3.json()
        pprint(vader)
        pprint(film)
        pprint(ship)


    else:
        print("That is not a valid URL.")

    print(f"{vader['name']} was born in the year {vader['birth_year']}. His eyes are now {vader['eye_color']} and his hair is {vader['hair_color']}")
    print(f"He first appeared in the movie {film['title']} and could be found flying around in his {ship['name']}.") 
if __name__ == "__main__":
    main()

