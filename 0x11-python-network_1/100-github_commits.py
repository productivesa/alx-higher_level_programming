#!/usr/bin/python3
"""Python script that takes 2 arguments and solve challenges 
of first arguments will repositoryname and second will owner name."""

import requests
from sys import argv

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits?per_page=10"\
          .format(argv[2], argv[1])

    request = requests.get(url)
    commits = request.json()
    for commit in commits:
        print("{}: {}".format(commit.get("sha"),
                              commit.get("commit").get("author").get("name")))
