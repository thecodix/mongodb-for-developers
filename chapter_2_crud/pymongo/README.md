# Interacting with MongoDB using Pymongo

### Using find and findOne

Consider the following code snippet:

    import pymongo
    import sys

    # establish a connection to the server, and use it to get a handle on the scores collection.
    connection = pymongo.MongoClient("mongodb://localhost")
    
    # get a handle to the school database and the scores collection.
    db=connection.school
    scores = db.scores
         
    try:
            XXX
            
    except Exception as e:
            print "Unexpected error:", type(e), e
    
    print doc

Enter the one line of python code that would be needed in place of XXX to find one document in the collection and have it print out properly.

    doc = scores.find_one()

### Projection

How to project just the student_id from the scores collection using a find command.

    students.find({}, {'student_id', '_id': 0})

You need to specify the {} as first parameter so find understands you are expecting to receive a projection, not a query.

### Using $gt and $lt

In the following code, what is the correct line of code, marked by xxxx, to search for all quiz scores that are greater than 20 and less than 90.

    def find():
    
        xxxx
    
        try:
            iter = scores.find(query)
    
        except Exception as e:
            print "Unexpected error:", type(e), e
            
        return iter

Answer

    query = {'type': 'quiz', 'score': {'$gt': 20, '$lt': 90}}

### Using $regex

    query = {'title':{'$regex':'apple|google', '$options':'i'}}
    projection = {'title':1, '_id':0}

    try:
        cursor = stories.find(query, projection)

### Sort, skip and limit

The DB does not run the query until you start iterating with the cursor.

So no matter how you queue the sort, skip and limit operations, unless you start iterating, this will always be the order:
  
  * Sort
  * Skip
  * Limit
  
Supposed you had the following documents in a collection named things.

    { "_id" : 0, "value" : 10 }
    { "_id" : 2, "value" : 5 }
    { "_id" : 3, "value" : 7 }
    { "_id" : 4, "value" : 20 }

If you performed the following query in pymongo:

    cursor = things.find().skip( 3 ).limit( 1 ).sort( 'value', pymongo.DESCENDING )

Which document would be returned?

    The document with _id = 2
    
### Insert update and delete


<table>
<tr>
  <th>Operation</th>
  <th>Pymongo</th>
  <th>Server</th>
</tr>
<tr>
    <td>Inserting</td>
    <td>insert_one</td>
    <td>insert</td>
</tr>
<tr>
    <td></td>
    <td>insert_many</td>
    <td>bulk</td>
</tr>
<tr>
    <td>Updating</td>
    <td>update_one</td>
    <td>update</td>
</tr>
<tr>
    <td></td>
    <td>update_many</td>
    <td>update</td>
</tr>
<tr>
    <td></td>
    <td>replace_one</td>
    <td>update</td>
</tr>
<tr>
    <td>Delete</td>
    <td>delete_one</td>
    <td>remove</td>
</tr>
<tr>
    <td></td>
    <td>delete_many</td>
    <td>remove</td>
</tr>
</table>

#### Insert_one

Do you expect the second insert below to succeed?

    # get a handle to the school database
    db=connection.school
    people = db.people
    
    doc = {"name":"Andrew Erlichson", "company":"MongoDB",
                  "interests":['running', 'cycling', 'photography']}
    
    try:
            people.insert_one(doc)   # first insert
            del(doc['_id'])
            people.insert_one(doc)   # second insert
    
    except Exception as e:
            print "Unexpected error:", type(e), e

Answer:

    Yes, because the del call will remove the _id key added by the Pymongo driver in the first insert
    
#### Insert_many

Suppose you ran the following python program. How many documents would you expect to find in the things collection at the completion of the program, and why?

    def insert_many():
    
        docs = [{'_id':1,'a':1}, 
                {'_id':2,'b':2},            
                {'_id':3,'b':3},            
                {'_id':3,'b':4},            
                {'_id':4,'b':5}]
    
        try:
            things.insert_many(docs)
    
        except Exception as e:
            print "Unexpected error:", type(e), e

    insert_many()

Answer:
    
    Three documents, because insert_many has insert_ordered by default and it will fail at the moment of inserting the second element with same _id

#### Update one and update many

n the following code fragment, what is the python expression in place of xxxx to set a new key "examiner" to be "Jones"

Please use the $set operator.

    try:
        # get the doc
        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "before: ", score

        # update using set
        scores.update_one({'student_id':1, 'type':'homework'},
                      xxxx)

        score = scores.find_one({'student_id':1, 'type':'homework'})
        print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

Answer

    {'$set': {'examiner': 'Jones'}}

#### Replace one

* replace_one, update_one and update_many all call the server's __update__ command behind the scenes
* If you use update_one or update_many, you must specify a $operator of some sort.
* If you use replace_one, you may not specify a $operator, where operator is something like 'set' or 'unset'

## Upsert

_"If I can't find the document I want to update, insert one"_

Suppose we would like to upsert the following document into the collection stuff:

    {_id:"bat", friend:'ball', cousin:'glove'}

Which of the following python statements work when using PyMongo. Check all that apply.

    stuff.update_one({'_id': 'bat'}, {'$set': {'friend': 'ball', 'cousin': 'glove'}}, upsert=True)
    stuff.update_one({'_id': 'bat'}, {'$set': {'_id': 'bat', 'friend': 'ball', 'cousin': 'glove'}}, upsert=True)
    stuff.replace_one({'_id': 'bat'}, {'friend': 'ball', 'cousin': 'glove'}, upsert=True)

## Removing data

When performing a delete_one or delete_many, you get back a DeleteResult structure that contains the number of documents deleted.

This is called _deleted_count_

## Find_and_modify

_find_one_and_delete_, _find_one_and_update_ and _find_one_and_replace_ all call internally _find_and_modify_