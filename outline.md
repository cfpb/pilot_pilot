Assumptions
-----------
-	Test a file for amount of time it takes python to get through it
-	If long time, load into sqlite, if not, keep as a stand alone app for larger files
-	Controller is a json file
-	Output is a json file

Need
----
-	Work on synthetic file to begin with (n ~ 2500 – average, then move to 10,000 – 97%, then move to 25,000 – 99%)
-	Real submitted files
  - Then move to real submitted files, must get from HMDA


Model
-----
-	Locate file, and open it.
-	Determine if file is real hmda file
  - If not; return error, stop
  - If so, load first row into an array
    - Fields are specified

-	Open controller to read
-	Open output to write
-	Cycle through all nodes in controller file (json), 
  - Perform test contained in pyController
  - Write result of test to output .json file
-	Close output
-	Close controller
