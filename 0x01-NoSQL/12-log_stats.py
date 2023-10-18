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
    print(f"{nginx_collection.estimated_document_count()} logs")
    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    gets = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f"{gets} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
