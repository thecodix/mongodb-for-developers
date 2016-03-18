# MongoDB

## What's MongoDB
MongoDB is introduced in a couple small videos, with emphasis on the syntax and the differences with relational SQL databases, specially in terms of scalability

## Installing MongoDB

The version recommended to install is any 3.0.X version

While installing a previous release is very easy on Windows, I decided to go ahead and install the latest on Ubuntu (<i>caveat emptor</i>)

Current stable release is 3.2.4

This are the installation steps for both systems

### Installing MongoDB on Windows

Going to the [MongoDB download page](https://www.mongodb.org/downloads#production) should let you decide between installing latest release or a [previous one](https://www.mongodb.org/downloads#previous)

We choose __previous__ and aim for 3.0.10. An .msi package will be downloaded with a very simple configurator.

Remember to choose the 'complete' option on the installation wizard 

Next step is adding the path to the mongo application to the environment variables

The path is usually <pre>C:\Program Files\MongoDB\Server\3.0\bin</pre>

Before running the DB, we need to choose a folder to store the data. We can do it opening a terminal and running the following command

    $ md \data
    $ md \data\db

Then running mongod should start the MongoDB database

    $ mongod
    
To check that the DB is running correctly, open a new terminal - dont close the previous one! - and type:

    $ mongo
    
A message should appear saying that we connected to the test database, and the MongoDB prompt will appear as well


### Installing MongoDB on Ubuntu (14.04)

This are the instructions followed to [install mongoDB on Ubuntu 14.04](https://docs.mongodb.org/master/tutorial/install-mongodb-on-ubuntu/) which can be resumed to:

Import the public key used by the package management system

    $ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927

Create a list file for MongoDB

    $ echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
    
Reload local package database

    $ sudo apt-get update

Install the MongoDB packages
(In this step you could choose a previous release if you want to)

    $ sudo apt-get install -y mongodb-org
 
Start the DB

    $ sudo service mongod start

## What did we learn here?

* Scalability in MongoDB is easier
* The standard to interact with MongoDB is BSON, a superset of JSON
* We're going to build apps with MongoDB (yay!)

Oh, and a nice graph showing where MongoDB is positioned regarding scalability and functionality

<img style="float: left;" width="480" height="360" src="http://image.slidesharecdn.com/managingsocialcontentwithmongodb-121030081212-phpapp02/95/managing-social-content-with-mongodb-11-638.jpg?cb=1351584966">
