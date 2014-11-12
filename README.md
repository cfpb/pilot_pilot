pilot_pilot
===========

this repo is a pilot of the hmda pilot.  as a pilot to a pilot, it has a very small focused purpose; test of some basic ideas for the pilot edit checking and reporting function.

The HMDA pilot (to be built) is a concept to test the idea of radically changing the business process by which current financial institution which are required to file data under HMDA.  The current filing process involves a series of [~150 edit checks](http://www.ffiec.gov/hmda/edits.htm) that need to be performed on the data.  Many of these checks must be valid prior to submission, but some are flags that need to be just affirmed (e.g. verified) that indeed this is an ok value.  The process today requires a significant back and forth effort between the government and the financial institution and has a substantial amount of paper and hand processing.  The efficiency of HMDA filing could be increased with some automation, thus reducing burden on both the financial institution and the government's ability to process this important data asset.

The HMDA pilot intends to test the idea that nearly all of the edits can be performed client side upstream, thereby eliminating much of paper and hand processing.  In order to help understand this process, we took on this very small effort to test some of the edits on the client side w/ synthetic data.  We call this test the pilot_pilot.

The pilot_pilot project takes the pilot concept and tests a very small function, namely the amount of time it might take to process an average hmda .dat file by building a simple model-controller component base.  This small component base is a) a controller and file specification base built from the published Edit document and file specification documents and b) a model built in python.  The controller identifies a taxonomy of each edit check and passed an edit to the model for running.  The model has a hard coded file.

The goal here is to establish a (a) [machine readable scaleable parser of the data](https://github.com/feomike/pilot_pilot/blob/master/src/file_spec.json) and (b) [a machine readable fully contained set of edits (e.g. a controller)](https://github.com/feomike/pilot_pilot/blob/master/src/controller.json) for the data.

The pilot_pilot is a simple python line command opportunity to test pilot before it begins.  it works by reading in a [sample synthetic data file](https://github.com/feomike/pilot_pilot/blob/master/data/lar.dat), reading one line at a lime, then cycling through one edit at a time in the [controller](https://github.com/feomike/pilot_pilot/blob/master/src/controller.json) to perform each test of the appropriate data point in the data file.  A result is returned which establishes if that edit passed or failed.  In this pilot_pilot, the result is merely printed to screen.  in a more advanced setting, say the pilot, the result would be written to a receipt file and later displayed in a nice user interface to the end user.

This whole effort establishes the opportunity to have the financial institution submitting data to know unequivocally that the data they submit is correct and no other effort later is required.

The pilot_pilot just establishes that a client side engine could be developed which would pre-process data.

Running the code
----------------
- make a local copy of this repo
- move to the src directory
- at a terminal, type `python hmda_model.py`
- to continue testing evalution time copy and paste data rows into the .dat file and to see how long runs take on larger sets of data 

Assumptions
-----------
-	Test a file for amount of time it takes python to get through it
-	At a certain processing time, we need to think of a different solution for edit checking (e.g. perhaps after a minute or so), like  sqlite, dat etc.  
-	Controller is a json file ([exmaple done](https://github.com/feomike/pilot_pilot/blob/master/src/controller.json))
- 	File specification document is a json file ([example done](https://github.com/feomike/pilot_pilot/blob/master/src/file_spec.json))
- 	Perform the testing on some synthetic files to begin with.  Once the basic components are in place, begin testing with real data.
-	Initial output should just be to screen (e.g. print pass/fail), but addvanced features should be writing results to a file.

Potential Needs
---------------
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
    - assess the data; repeat for all rows in the .dat file

-	Open controller to read
-	Open output to write
-	Cycle through all nodes in controller file (json), 
  - Perform test contained in pyController
  - Write result of test to screen (someday output .json file)
-	Close output
-	Close controller
