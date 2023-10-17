#!/usr/bin/env python3

"""
function that lists all documents in a collection
Return an empty list if no document in the collection
monog_collection will be pymongo collection object
"""


def list_all(mongo_collection):
    """
    function that lists all docs in
    a collection with collection name
    given as argument
    """
    docs = mongo_collection.find()
    return list(docs)
