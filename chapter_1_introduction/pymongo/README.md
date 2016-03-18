# Pymongo
Quoting the experts:

 __PyMongo__ is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python

Fair enough

PyMongo is a Python distribution containing tools for working with MongoDB, and is the recommended way to work with MongoDB from Python

<img style="float: left;" width="400" height="263" src="https://emptysqua.re/blog/survey-how-do-you-use-python-with-mongodb/Albertus_Seba_Python_sebae.jpg">



## Installation

The video on the training suggests to install a beta version, which at this very moment is a legacy version and perfectly stable

We just open the pymongo page and go to [<i>Installing / Upgrading</i>](https://api.mongodb.org/python/current/installation.html)

There we see the command to install pymongo, which should be the same on any OS

    $ python -m pip install pymongo
    
That's all

To test applications or scripts that connect with pymongo, as stupid as it sounds, be sure to have the MongoDB up and running, else the connection will be stuck until it times out

## Usage
To use the library, import it on your python project
    
    import pymongo
    connection = pymongo.MongoClient("mongodb://localhost")
    db = connection.test
    users = db.users

## Exception processing

A small video is included showing the basics of exception processing by pymongo

This will sure come handy later when errors start to appear and we have to properly deal with them