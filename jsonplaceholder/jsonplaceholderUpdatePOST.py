import requests

PUTURL = "https://jsonplaceholder.typicode.com/posts/1"

def main():

    updated_data = {
            "id": 1,
            "title": "Updated Title",
            "body": "This is the updated body of the post.",
            "userId": 1
            }

    resp = requests.put(PUTURL, json=updated_data)

    respjson = resp.json()


    print(respjson)

    print(f"Updated post title: {respjson['title']}")

if __name__ == "__main__":
    main()
