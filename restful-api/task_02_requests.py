#!/usr/bin/python3
""" Nameless module for Task 2 """

import requests
import csv

def fetch_and_print_posts():
    """ Does what it says """
    url: str = "https://jsonplaceholder.typicode.com/posts/"
    posts_request = requests.get(url=url, timeout=10)
    data = posts_request.json()

    print("Status Code: {}".format(posts_request.status_code))

    for p in data:
        print(p['title'])
    print("")

def fetch_and_save_posts():
    """ Does what it says """
    url: str = "https://jsonplaceholder.typicode.com/posts/"
    posts_request = requests.get(url=url, timeout=10)
    data = posts_request.json()

    with open('posts.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames,
            quotechar='"',
            quoting=csv.QUOTE_NONNUMERIC
        )

        writer.writeheader()
        for p in data:
            d = {"id": p['id'], "title": p['title'], "body": p['body'].replace("\n", " ")}
            writer.writerow(d)
