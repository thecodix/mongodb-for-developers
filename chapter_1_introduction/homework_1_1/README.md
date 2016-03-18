# Homework 1_1
## Abstract
Install MongoDB on your computer and run it on the standard port.

Download the HW1-1 from the Download Handout link and uncompress it.

Use mongorestore to restore the dump into your running mongod. Do this by opening a terminal window (mac) or cmd window (windows) and navigating to the directory so that you are in the parent directory of the dump directory (if you used the default extraction method, it should be hw1/). Now type:

    mongorestore dump

Note you will need to have your path setup correctly to find mongorestore.

Next, go into the Mongo shell, perform a findOne on the collection called _hw1_ in the database _m101_. That will return one document. Please provide the value corresponding to the "answer" key from the document returned.

_hint: if you get back a document that looks like { "_id": 1234, "answer": 2468 }, please only put in 2468 (with no spaces) for your answer._

## How do I mongorestore?

This homework, like the others on the first chapters, is just a quick check to know if you've been able to install the proper tools and dependencies explained on the videos

The main issues you can find here are:

* __MongoDB is not installed__. That's like the first step... Go and have it installed
* __Mongo / Mongod / Mongorestore is not recognized as a command__. That means Windows path has not been updated with the path to the MongoDB executable. Update it and try again.
* __Can't find any document__. Sure you are connecting to collection hw1, database m101? Try again

I won't provide the answer so you follow this simple steps, but just worth mentioning that if you read Douglas Adams you'll appreciate the trivia reference.

