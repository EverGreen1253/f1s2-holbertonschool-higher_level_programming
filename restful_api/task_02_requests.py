#!/usr/bin/python3
""" Nameless module for Task 2 """

import requests
import csv

url: str = "https://jsonplaceholder.typicode.com/posts/"
posts_request = requests.get(url=url, timeout=10)

# Step 1
print("---Status Code---\n{}\n".format(posts_request.status_code))

# Step 2
data = posts_request.json()
print("---Titles---")
for p in data:
    print(p['title'])
print("")

# Step 3
# output = []
# for p in data:
#     d = {}
#     d['id'] = p['id']
#     d['title'] = p['title']
#     d['body'] = p['body']
#     output.append(d)

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
