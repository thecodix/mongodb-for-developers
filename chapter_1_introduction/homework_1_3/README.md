# Homework 1_3
## Abstract
We are now going to test that you have bottle installed correctly and can run a bottle-based project. Download the handout and run it as follows:

python hw1-3.py

It requires that:

* bottle be installed correctly
* your mongodb to be running
* you have run mongorestore properly

From a different terminal window type the following from the command line: <pre>curl http://localhost:8080/hw1/50</pre>

Alternatively, you can put the url above into your web browser.

Type the two-digit answer into the box below (no spaces). 

## Half empty

The goal here is to ensure bottle has been correctly installed on the OS of your choice

The main issues you can find here are:

* __Bottle, what's bottle?__. Be sure to install bottle before trying to attempt this homework
* __I'm running the script but the terminal is like.. frozen..__. Mongod service is not up an running. Do a sudo mongod service start
* __[Errno 111] Connection refused..__. Mongod service is not up an running. Do a sudo mongod service start.
* __http://localhost:8080/hw1/50 says 'Unable to connect'__. First run the script, then open the browser

