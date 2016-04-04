# Homework 2_1
## Abstract

In this problem, you will be using a collection of student scores that is similar to what we used in the lessons. Please download grades.json from the Download Handout link and import it into your local mongo database as follows:

    mongoimport -d students -c grades < grades.json

The dataset contains 4 scores for 200 students.

First, let’s confirm your data is intact; the number of documents should be 800.

    use students
    db.grades.count()

You should get 800.

This next query, which uses the aggregation framework that we have not taught yet, will tell you the student_id with the highest average score:

    db.grades.aggregate({'$group':{'_id':'$student_id', 'average':{$avg:'$score'}}}, {'$sort':{'average':-1}}, {'$limit':1})

The answer should be _student_id_ 164 with an average of approximately 89.3.

Now it’s your turn to analyze the data set. Find all exam scores greater than or equal to 65, and sort those scores from lowest to highest.

What is the _student_id_ of the lowest exam score above 65?

## So what's the drill?

The point of this homework is getting familiar with the usual commands for querying in MongoDB

It is necessary to concatenate different options when searching to obtain the desired result

Main issues you will find here:

* __I got a score in my query that is below 65__: The filter for score is not correctly placed or you forgot it