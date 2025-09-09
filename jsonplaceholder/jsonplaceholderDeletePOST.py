import requests

DELETEURL = "https://jsonplaceholder.typicode.com/posts/1"

def main():

    resp = requests.delete(DELETEURL)

    if resp.status_code == 200 or resp.status_code == 204:
        print("Post deleted successfully!")
    else:
        print(f"Failed to delete post. Status code: {resp.status_code}")

if __name__ == "__main__":
    main()
