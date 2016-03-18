import pymongo
import bottle


# Copyright 2014, MongoDB, Inc.
# Author: Andrew Erlichson


@bottle.get("/hw1/<n>")
def get_hw1(n):

    # connect to to the db on standard port
    connection = pymongo.MongoClient("mongodb://localhost")

    n = int(n)

    db = connection.m101                 # attach to db
    collection = db.funnynumbers         # specify the collection

    try:
        collection_items = collection.find({}, limit=1, skip=n).sort('value', direction=1)
        for item in collection_items:
            return str(int(item['value'])) + "\n"
    except Exception as e:
        print "Error trying to read collection:", type(e), e


bottle.debug(True)
bottle.run(host='localhost', port=8080)
