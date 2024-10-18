#!/usr/bin/python3
import requests
import csv
url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    result = requests.get(url)
    print("Status Code: {}".format(result.status_code))
    if result.status_code == 200:
        deserialized = result.json()
        for index in deserialized:
            print(f"{index['title']}")


def fetch_and_save_posts():
    result = requests.get(url)
    if result.status_code == 200:
        deserialized = result.json()
        dictlist = [{"id": index["id"], "title": index["title"],
                     "body": index["body"]} for index in deserialized]
        with open('posts.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(dictlist)
