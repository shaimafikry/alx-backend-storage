#!/usr/bin/env python3
""" find school """

def schools_by_topic(mongo_collection, topic):
    """ return specific topic"""
    return mongo_collection.find({"topics": topic})
