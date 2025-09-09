import requests

URL = "http://api.open-notify.org/iss-now.json"

def main():

    data = requests.get(URL)

    datason = data.json()

    print(f"CURRENT LOCATION OF THE ISS: \n Lon: {datason['iss_position']['longitude']} \n Lat: {datason['iss_position']['latitude']}")

if __name__ == "__main__":
    main()
