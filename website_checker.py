import requests

def check_website():
    url = input("Enter website URL: ")

    try:
        response = requests.get(url, timeout=5)

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            print("Website is online")
        else:
            print("Website responded with an error")

    except Exception:
        print("Unable to connect")
        