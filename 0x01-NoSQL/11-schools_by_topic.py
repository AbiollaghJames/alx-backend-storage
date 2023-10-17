#!/usr/bin/env python3

"""
Function that returns list of school having a
specific topic.
mongo_collection will be pymongo collection object
topic (string) will be the topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """
    Function that returns list of school having a
    specific topic
    """
    docs = mongo_collection.find({"topics": topic})
    return list(docs)
