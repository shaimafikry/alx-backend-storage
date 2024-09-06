#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB
 """
from pymongo import MongoClient
# connect the data base


def main():
    """main"""
    client = MongoClient()
    # access data base
    db = client.logs
    # access collection
    collection = db.nginx

    # count
    count_data = collection.count_documents({})
    print (f"{count_data} logs")
    data = collection.find()
    # print(list(data))
    get_method = collection.count_documents({'method': 'GET'})
    post_method = collection.count_documents({'method': 'POST'})
    put_method = collection.count_documents({'method': 'PUT'})
    patch_method = collection.count_documents({'method': 'PATCH'})
    delete_method = collection.count_documents({'method': 'DELETE'})
    method = {"GET": get_method, "POST": post_method, "PUT": put_method,
          "PATCH": patch_method, "DELETE": delete_method}

    # print(data_method)
    print("Methods:")
    for k, v in method.items():
        print(f"	Method {k}: {v}")
    print(collection.count_documents({'path': '/status'}), "status check")
    # 94778 logs
    # Methods:
    #     method GET: 93842
    #     method POST: 229
    #     method PUT: 0
    #     method PATCH: 0
    #     method DELETE: 0
    # 47415 status check

if __name__ == "__main__":
    main()
