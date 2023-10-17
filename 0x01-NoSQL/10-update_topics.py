#!/usr/bin/env python3

"""
Function that changes all topics of a school
document based on the name.
mongo_collection will be pymongo collection obj
name (string) will be school name to update
topics(list of str) list of topics in the school
"""


def update_topics(mongo_collection, name, topics):
    """
    Fucntion that updates school based on the name
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}},
        upsert=False
    )
