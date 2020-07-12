import requests


def request():
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return 'There was an error'


if __name__ == "__main__":
    response = request()
    print(response)
