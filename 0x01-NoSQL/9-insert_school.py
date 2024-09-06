#!/usr/bin/env python3
""" insert school """

def insert_school(mongo_collection, **kwargs):
    """ insert function"""
    data = mongo_collection.insert_one(kwargs)
    return data.inserted_id
