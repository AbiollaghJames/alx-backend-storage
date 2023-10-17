#!/usr/bin/env python3

"""
Python script that provides some stats about Nginx logs stored in MongoDB:
    Database: logs
    Collection: nginx
    Display (same as the example):
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
    5 lines with the number of documents with the
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
    one line with the number of documents with:
    method=GET
    path=/status
"""

from pymongo import MongoClient

""" MongoDB connection """
client = MongoClient("mongodb://localhost:27017")

"""access DB and collection """
db = client["logs"]
collection = db["nginx"]

""" Docs in collection """
logs = collection.count_documents({})

""" Docs with http methods """
methods = [ "GET", "POST", "PUT", "PATCH", "DELETE" ]
counts = {method: collection.count_documents({"method": method}) for method in methods} 

""" Docs with specific methods and path """
spec_count = collection.count_documents({"method": "GET", "path": "/status"})

"""statistics"""
print(f"{logs} logs")
print("Methods:")

for method in methods:
    print(f"\tmethod {method}: {counts[method]}")
print(f"{spec_count} status check")
