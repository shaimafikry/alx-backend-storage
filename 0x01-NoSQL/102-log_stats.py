#!/usr/bin/env python3
"""Python script that provides some stats about Nginx logs stored in MongoDB
 """
from pymongo import MongoClient
# connect the data base


def main():
    """main function"""
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
        print(f"	method {k}: {v}")
    print(collection.count_documents({'path': '/status'}), "status check")

    ips = {
      "172.31.63.67": collection.count_documents({'ip': '172.31.63.67'}),
           "172.31.2.14": collection.count_documents({'ip': '172.31.2.14'}),
           "172.31.29.194": collection.count_documents({'ip': '172.31.29.194'}),
           "69.162.124.230": collection.count_documents({'ip': '69.162.124.230'}),
           "64.124.26.109": collection.count_documents({'ip': '64.124.26.109'}),
           "64.62.224.29": collection.count_documents({'ip': '64.62.224.29'}),
           "34.207.121.61": collection.count_documents({'ip': '34.207.121.61'}),
           "47.88.100.4": collection.count_documents({'ip': '47.88.100.4'}),
           "45.249.84.250": collection.count_documents({'ip': '45.249.84.250'}),
           "216.244.66.228": collection.count_documents({'ip': '216.244.66.228'})
           }
    print("IPs:")
    for k, v in ips.items():
        print(f"	{k}: {v}")

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
