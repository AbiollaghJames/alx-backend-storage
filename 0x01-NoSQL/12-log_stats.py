#!/usr/bin/env python3

"""
Python script that provides some stats about Nginx logs stored in MongoDB:
    Database: logs
    Collection: nginx
    Display (same as the example):
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
    5 lines with the number of documents with the
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order
    one line with the number of documents with:
    method=GET
    path=/status
"""

from pymongo import MongoClient


def log_stats(nginx_collection):
    """
    Function that provide stats about Nginx logs
    """
    print(f"{} logs".format(nginx_collection.count_documents({})))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        count = len(list(nginx_collection.find({"method": method})))
        print(f"\tmethod {method}: {count}")

    status_check = len(list(nginx_collection.find(
        {"method": "GET", "path": "/status"})))
    print(f"{status_check}")


if __name__ == "__main__":
    client = MongoClient('mongodb://localhost:27017')
    log_stats(client.logs.nginx)
