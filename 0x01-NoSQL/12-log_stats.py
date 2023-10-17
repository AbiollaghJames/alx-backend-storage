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

METHODS = ["GET", "POST", "PUT", "PATCH", "DELEE"]


def stats(mongo_collection, opt=None):
    """
    Function that provide stats about Nginx logs
    """
    l = {}

    if opt:
        val = mongo_collection.count_documents(
            {"method": {"$regex": opt}}
        )
        print(f"\tmethod {opt}: {val}")
        return

    res = mongo_collection.count_documents(l)
    print(f"{res} logs")
    print("Methods:")
    for method in METHODS:
        stats(nginx_collection, method)

    status = mongo_collection.count_documents({"path": "/status"})
    print(f"{status} status check")

if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://localhost:27017').logs.nginx
    stats(nginx_collection)
