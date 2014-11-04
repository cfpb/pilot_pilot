pilot_pilot
===========

this repo is a pilot of the hmda pilot.  as a pilot to a pilot, it has a very small focused purpose; test of some basic ideas for the pilot edit checking and reporting function.

The pilot_pilot project takes the pilot concept and tests a very small function, namely the amount of time it would take to process an average hmda .dat file by building a simple model-controller component base.  This small component base is a) a controller and file specification base built from the published Edit document and file specification documents and b) a model built in python.  The controller identifies a taxonomy of each edit check and passed an edit to the model for running.  The model has a hard coded file.

Running the code
----------------
- make a local copy of this repo
- move to the src directory
- edit hmda_model.py lines 45-47 to ensure the code is pointing to the proper data, controller and file spec files
- at a terminal, type 'python hmda_model.py'

Assumptions
-----------
-	Test a file for amount of time it takes python to get through it
-	At a certain processing time, we need to think of a different solution for edit checking (e.g. perhaps after a minute or so), like  sqlite, dat etc.  
-	Controller is a json file ([exmaple done](https://github.com/feomike/pilot_pilot/blob/master/src/controller.json))
- 	File specification document is a json file ([example done](https://github.com/feomike/pilot_pilot/blob/master/src/file_spec.json))
- 	Perform the testing on some synthetic files to begin with.  Once the basic components are in place, begin testing with real data.
-	Initial output should just be to screen (e.g. print pass/fail), but addvanced features should be writing results to a file.

Need
----
- Create a test controller that just tests one thing (eg field 1 row 1)
-	Work on synthetic file to begin with (n ~ 2500 – average, then move to 10,000 – 97%, then move to 25,000 – 99%)
-	Real submitted files

Model
-----
- 	Locate file to test, and open it.
- 	Locate and open the file spec document to create all the field variables
-	Determine if file to test is real hmda file
  - If not; return error, stop
  - If so, load first row into an array
    - assess the 

-	Open controller to read
-	Open output to write
-	Cycle through all nodes in controller file (json), 
  - Perform test contained in pyController
  - Write result of test to output .json file
-	Close output
-	Close controller
