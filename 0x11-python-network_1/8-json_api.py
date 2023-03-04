#!/usr/bin/python3
"""
Python script that sends a POST request to the URL and
to an URL with the letter as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    data = {"q": argv[1] if len(argv) > 1 else ""}
    request = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        json = request.json()
        if json:
            print("[{}] {}".format(json.get("id"), json.get("name")))
        else:
            print("No result")
    except ValueError:
        pass
