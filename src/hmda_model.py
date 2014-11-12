### ---------------------------------------------------------------------------
###   VERSION 0.1 
###  model.py
### Created on: Weds Aug 27 2014
### Created by: Michael Byrne
### Consumer Finance Protection Bureau 
### ---------------------------------------------------------------------------
### tests controller model the pilot for the pilot of HMDA collection operaitons          
### ---------------------------------------------------------------------------
### this example model is one of the stool legs in the model-view-controller pilot
### for cleaning hmda data
### this script opens and reads a .dat file of submitted data then
### applies the edit checks from the controller file.  the edit checks are derrived
### from the real HMDA edit checks document.  in order to slice the exact string of data
### from the dat file, a 'field lookup' is performed by grabbing the field name out of 
### the controller file, and then looking up that field name in the file spec document
### to grab the start and length items for that field. the start and end items are used
### to splice the line data to acquire and acquire the correct item of data

### originally i had hoped that the evaluate function would actually be logic 
### contained in the controller file, but i struggled w/ applying some of the logic
### (e.g. u'str'.isdigit() ) to the value of the string when it was in the controller
### so i switched to writing an evaluate function where the controller has the 'type' of
### test to perform (e.g. test) and the evaluate function looks up that test.  
### right now this is pretty in-efficient, b/c it is performing all kinds of extra tests
### per line (e.g. if/thens), but it generally works

### this script is not optimized and was written to test processing time examples for 
### files
# Import system modules
import sys, string, os
import json
from hmda_evaluate import evaluate

import time
from datetime import date
from os import remove, close
today = date.today()
now = time.localtime(time.time())
print "    start time:", time.asctime(now)

### yes i have some global variables - these are the input .dat file, the controller
###     and the file_specification files.  in a mature code the controller and the
###     file specification files would be at urls
myFile = "../data/lar.dat"
myControlFile = "controller.json"
myFileSpecFile = "file_spec.json"
json_data = open(myControlFile)
myControl = json.load(json_data) #the control file
json_data = open(myFileSpecFile) 
myFileSpec = json.load(json_data) #the File Specification Document    
json_data.close() 

#perform all the checks for the transmittal sheet
#the transmittal sheet is one line of data (the first, so this runs only once for a file)
def checkVals(section, myData):
	#section is the section of edits in the controller on 
	#which to operate - eg "Transmittal Sheet"
	#myData is the line you are operating on in the .dat file
	cltr = 0
	#operate on all controls in the section (read one json node at a time)
	while cltr < len(myControl[section]):
		#myField is the field on which to perform the check
		myField = myControl[section][cltr]["Transaction Item(s)"]
		#myStart is the starting postion in the .dat line for myField
		myStart = int(myFileSpec[section][0][myField][0]["Start"]) - 1
		#myLen is the length of that field; myStart and myLen are used to 'splice' the
		#data from the line (.dat) file to see what the curent value of the field is
		myLen  = int(myFileSpec[section][0][myField][0]["Length"])
		#myDat is the result of the splice; e.g. this is the value you want to test		
		myDat = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		#myTest is the Type of test; used as a 'case' style statement evaluation 
		#in the hmda_evaluate script to perform the test
		myTest = myControl[section][cltr]["Test"]
		#myVal is not used always;  it is used in complex cases when we need to pass
		#additional information on to the hmda_evaluation routine; things like other
		#fields or values to test
		myVal  = myControl[section][cltr]["Value"]
		myResult = evaluate(myDat, myTest, myVal, myData, myFileSpec)
		#at some point you will need to do something different than print pass/fail
		if myResult:
			print "     passed: " + myControl[section][cltr]["EDCK"]	+ " " + myDat	
			mycnt = 1
		else:
			print "     FAILED: " + myControl[section][cltr]["EDCK"]	+ " " + myDat
			mycnt = 1
		cltr = cltr + 1
	return()
	
#Create Receipt
cnt = 0
try:
	theFile = open(myFile, 'r')
	with open(myFile, 'r') as f:
		for line in f:
			if cnt == 0: #this is the transmittal sheet
				print "checking Transmittal Sheet ..."
				checkVals("Transmittal Sheet",line)
				print "checking LAR Data ..."
			if cnt > 0: #this is the LAR data
				checkVals("Loan Application Register",line)
			cnt = cnt + 1
		#there are likely to be tests to run not on a line by line basis
	now = time.localtime(time.time())
	print "    end time:", time.asctime(now)
except:
	print "an exception happened"
