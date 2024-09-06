#!/usr/bin/env python3
""" module"""
from pymongo import MongoClient

#input     school_collection = client.my_db.school
def list_all(mongo_collection):
    """lists all document in collections"""
    data = mongo_collection.find()
    return list(data)
