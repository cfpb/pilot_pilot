Assumptions
-----------
-	Test a file for amount of time it takes python to get through it
-	If long time, load into something else (e.g. sqlite, dat etc), if not, keep as a stand alone app for larger files
-	Controller is a json file ([exmaple done](https://github.com/feomike/pilot_pilot/blob/master/controller.json)
- 	File specification document is a json file ([example done](https://github.com/feomike/pilot_pilot/blob/master/file_spec.json)
- 	work on some synthetic or real files
-	Output is a json file

Need
----
-	Work on synthetic file to begin with (n ~ 2500 – average, then move to 10,000 – 97%, then move to 25,000 – 99%)
-	Real submitted files
- 	Then move to real submitted files, must get from HMDA
- 	Create a test controller that just tests one thing (eg field 1 row 1)


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
