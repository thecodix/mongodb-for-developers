# Chapter 3: Schema Design

## Topics
This chapter develops on how to create a good schema design for the database.

The following topics are covered:

* Patterns
* Case Studies
* Tradeoffs

## Homework

* [Homework 3.1 - Find those students!](homework_3_1/README.md)
* [Homework 3.2 - Blog posts](homework_3_2/README.md)
* [Homework 3.3 - Blog comments](homework_3_3/README.md)

## What did we learn here

### Small summary

* MongoDB supports 'Rich documents'. Embedding arrays as value of a key is possible.
* It can pre-join / embed data for fast access.
* There are no joins, but also no constraints.
* Atomic operations are supported, but not transactions.
* No declared schema.

The most important factor when designing a MongoDB schema is making it match your application data access patterns.

### Relational normalization

The goals of normalization are

* Free the database of modification anomalies
* Minimize redesign when extending
* To avoid bias for a particular access pattern

The last one is not important in MongoDB

### Living without constraints

What does living without constraints mean?

Keeping your data consistent even though MongoDB lacks foreign key constraints

But the point extracted from the video is:

"What guarantee is it that when you insert a document in the comments collection, that the post_id appears in the post collection?"

The answer in MongoDB is __there is no guarantee__

Is really up to you as the programmer to be sure that your data is consistent in that manner. (?)

When you store something in a collection, if you mean for that to be an index into the posts collection you guarantee that, cause DBs won't guarantee that for you

Is it worth then 'living without constraints' when all the responsibility for data consistency in the DB is up to the programmer?

### Living without transactions

Approaches to overcome the lack of transactions in MongoDB

* Restructure the code to work with a single document (?)
* Implement locking in SW
* Tolerate a bit of inconsistency (?????)

### One to one relations

What's a good reason you might want to keep two documents that are related to each other one-to-one in separate collections? Check all that apply.

* To reduce the working set size of your application
* Because the combined size of the documents would be larger than 16MB

### One to many relations

When is it recommended to represent a one to many relationship in multiple collections?

Whenever the many is large

### Many to many relations

For performance reasons is better to embed content on the collection, but it can lead to inconsistencies.

Is better to maintain an array with ids of the linked collection items (?)

Embed at the risk of duplicating data.

### Benefits of embedding data

* Improved read performance
* One round trip to the DB

### Trees

Given the following typical document for a e-commerce category hierarchy collection called categories

    {
      _id: 34,
      name : "Snorkeling",
      parent_id: 12,
      ancestors: [12, 35, 90]
    }

Which query will find all descendants of the snorkeling category?

    db.categories.find({ancestors:34})

### When to denormalize

* 1:1 Embed
* 1:many Embed (from the many to one)
* many:many Link

### Handling Blobs

USe GridFS