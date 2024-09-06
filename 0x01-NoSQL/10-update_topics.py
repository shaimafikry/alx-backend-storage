#!/usr/bin/env python3
""" modifiy school """
def update_topics(mongo_collection, name, topics):
    """ modifiy"""
    upd = mongo_collection.update_many({"name":name}, {"$set": {"topics": topics}})
