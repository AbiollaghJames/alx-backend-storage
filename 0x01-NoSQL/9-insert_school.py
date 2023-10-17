#!/usr/bin/env python3

"""
function that inserts new document in a collection
based on kwargs.
mongo_collection will be pymongo collection object
returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    function that inserts new document based
    on kwargs
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
