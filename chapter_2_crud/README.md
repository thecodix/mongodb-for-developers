# Chapter 2: CRUD

This chapter will cover the basic operations that you can perform in Mongo. Create, Read, Update and Delete

This are the topics that will be explained:

* MongoDBs basic document creation, retrieval, modification and removal operations
* [How to manipulate MongoDB documents from Python using Pymongo](pymongo/README.md)
* How to analyze data in MongoDB collections

## Homework

* [Homework 2.1 - MongoDB operations](homework_2_1/README.md)
* [Homework 2.2 - Cursors](homework_2_2/README.md)
* [Homework 2.3 - Blog User Sign-up and Login](homework_2_3/README.md)

## Mongo Shell

The Mongo Shell accepts Javascript syntax. It has shortcuts and autocompletion. 

Two basic syntaxes for accesing object elements: dot notation <pre>z.a</pre> vs square brackets notation <pre>z["a"]</pre>

### BSON

Serialization format which is a superset of what can be represented in JSON format. There is an overview on the BSON datatypes

## Analyzing data in MongoDB collections

### Create
Inserting elements

    > obj = {name: "Angel", color: "red"}
    > db.collection_name.insert(obj)
    WriteResult({ "nInserted" : 1 })

### Read
#### Retrieving elements with findOne

    > db.collection_name.findOne()
    {
        "_id" : ObjectId("56f28015d3f5ebd0c47dd5de"),
        "name" : "Angel",
        "color" : "red"
    }
    > db.collection_name.findOne({name : "Joseph"})
    {
        "_id" : ObjectId("56f28058d3f5ebd0c47dd5df"),
        "name" : "Joseph",
        "color" : "blue"
    }
    
    > db.collection_name.findOne({name : "Joseph"}, {name: true})
    { "_id" : ObjectId("56f28058d3f5ebd0c47dd5df"), "name" : "Joseph" }
    
    > db.collection_name.findOne({name : "Joseph"}, {name: true, _id: false})
    { "name" : "Joseph" }

#### Retrieving elements with find

    > db.collection_name.find()
    { "_id" : ObjectId("56f28015d3f5ebd0c47dd5de"), "name" : "Angel", "color" : "red" }
    { "_id" : ObjectId("56f28058d3f5ebd0c47dd5df"), "name" : "Joseph", "color" : "blue" }
    
    > db.collection_name.find().pretty()
    {
        "_id" : ObjectId("56f28015d3f5ebd0c47dd5de"),
        "name" : "Angel",
        "color" : "red"
    }
    {
        "_id" : ObjectId("56f28058d3f5ebd0c47dd5df"),
        "name" : "Joseph",
        "color" : "blue"
    }

#### Querying with $gt qnd $lt

Retrieve with score > 95:

    > db.users.find({score : { $gt : 95}})
    
Retrieve with score < 100:

    > db.users.find({score : { $lt : 95}})

Retrieve with score > 95 and <= 100:

    > db.users.find({score : { $gt : 95, $lte: 100}})

Note: Operations in MongoDB are strongly and dynamically typed

#### Regex and conditional stuff

Find elements where name is a string value (look BSON specification sheet for more info on types):

    > db.users.find({ name: { $type: 2 }})
    
Find by regex those who start with capital A:

    > db.users.find({ name: { $regex: "^A" }})
    
Write a query that retrieves documents from a users collection where the name has a "q" in it, and the document has an email field.

    > db.users.find({name: {$regex: "q"}}, {email: true})

Find all documents in the _scores_ collection where the _score_ is less than 50 or greater than 90:

    > db.scores.find( { $or : [ { score : { $lt : 50 } }, { score : { $gt: 90 } } ] } )
    
$all and $in. 

    > db.users.find( { friends : { $all : [ "Joe" , "Bob" ] }, favorites : { $in : [ "running" , "pickles" ] } } )
    { name : "Cliff", friends ["Pete", "Joe", "Bob", "Tom"], favorites : ["pickles", "cycling"]}

Write a query that finds all products that cost more than 10,000 and that have a rating of 5 or better.

    > db.catalog.find({price : {$gt: 10000}, "reviews.rating" : {$gte: 5}})

Count the documents in the _scores_ collection where the type was "essay" and the score was greater than 90

    > db.scores.count({type: "essay", score: {$gt: 90}})
    
### Update

#### Wholesale updating

Replaces the matching documents, updating them with the properties that you set after the comma

Let's say you had a collection with the following document in it:

    { "_id" : "Texas", "population" : 2500000, "land_locked" : 1 }

and you issued the query:

    > db.foo.update({_id:"Texas"},{population:30000000})

What would be the state of the collection after the update?

    { "_id" : "Texas", "population" : 2500000}
    
#### $set and $inc

$set sets the value for a single property of the document

$inc increments the value of the property specified

Given the document

    {'username': 'splunker', 'country': 'US', 'phone': '718-343-3433'}

in the collection users, write the shell command for updating the country to 'RU' for only this user.

    > db.users.update({username: "splunker"}, {$set: {country: "RU"}})
    
#### $unset

Removes a property for the element

Given the document

    {'username': 'jimmy', favorite_color: 'blue', interests:['debating', 'politics']}

Write an update query that will unset the interests key in the following documents in the collection users.

    > db.users.update({'username': 'jimmy'}, {'$unset': {'interests' : 1}})
    
#### Array operations

Suppose you have the following document in your friends collection:

    { _id : "Mike", interests : [ "chess", "botany" ] }

What will the result of the following updates be?

    db.friends.update( { _id : "Mike" }, { $push : { interests : "skydiving" } } );
    db.friends.update( { _id : "Mike" }, { $pop : { interests : -1 } } );
    db.friends.update( { _id : "Mike" }, { $addToSet : { interests : "skydiving" } } );
    db.friends.update( { _id : "Mike" }, { $pushAll: { interests : [ "skydiving" , "skiing" ] } } );

    > {_id: "Mike", interests : [ "botany", "skydiving" , "skydiving", "skiing" ]}
    
#### Upsert

Updates or inserts depending if the document exists or not

After performing the following update on an empty collection

    db.foo.update( { username : 'bar' }, { '$set' : { 'interests': [ 'cat' , 'dog' ] } } , { upsert : true } );

What could be a document in the collection?

    > { "_id" : ObjectId("ojog34u09u2fjsdifj23ji34i"), "interests" : ["cat", "dog"], "username": "bar"}
    
#### Multi-update

Recall the schema of the scores collection:

    {
        "_id" : ObjectId("50844162cb4cf456b4694f8"),
        "student" : 0,
        "type" : "exam",
        "score" : 75
    }

How would you give every record whose score was less than 70 an extra 20 points?

    > db.scores.update({score: {$lt: 70}}, {$inc: {score: 20}}, {multi: true})
    
### Delete

Recall the schema of the scores collection:

    {
        "_id" : ObjectId("50844162cb4cf4564b4694f8"),
        "student" : 0,
        "type" : "exam",
        "score" : 75
    }

Delete every document with a score of less than 60.

    > db.scores.remove({score: {$lt:60}})
    
