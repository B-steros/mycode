import requests

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    groundctrl = requests.get(MAJORTOM)

    helmetson = groundctrl.json()

    print("\n\nConverted Python data")
    print(helmetson)

    print(f"\n\nPeople in Space: {helmetson['number']}\n")

    people = helmetson['people']
    for person in people:
        print(person["name"] + " on the " + person["craft"])

if __name__ == "__main__":
    main()
