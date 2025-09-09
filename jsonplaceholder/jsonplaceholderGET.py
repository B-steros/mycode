import requests

GETURL = "https://jsonplaceholder.typicode.com/posts/1"

def main():

    resp = requests.get(GETURL)

    respjson = resp.json()

    print(respjson)

    print(f"The title of the post is --> {respjson['title']}")


if __name__ == "__main__":
    main()
