#!/usr/bin/env python3

"""
Function that returns students sorted by average score
mongo_collection will be the pymongo collection object
The top must be ordered
avr_score must be part of each item returns with
key = averageScore
"""


def top_students(mongo_collection):
    """
    Function that retusn all students
    sorted by average score
    """
    docs = [
        {
            "$unwind": "$topics"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {"$first": "$name"},
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    res = mongo_collection.aggregate(docs)
    return list(res)
