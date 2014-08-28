### ---------------------------------------------------------------------------
###   VERSION 0.1 
###  model.py
### Created on: Weds Aug 27 2014
### Created by: Michael Byrne
### Consumer Finance Protection Bureau 
### ---------------------------------------------------------------------------
### tests controller model the pilot for the pilot of HMDA collection operaitons          
### ---------------------------------------------------------------------------

# Import system modules
import sys, string, os
import json


#import time
#from datetime import date
#from os import remove, close
#today = date.today()

myFile = "/Users/feomike/documents/analysis/2014/pilot_pilot/lar_10000.dat"
myControlFile = "/Users/feomike/documents/analysis/2014/pilot_pilot/controller_1.json"
myFileSpecFile = "/Users/feomike/documents/analysis/2014/pilot_pilot/file_spec.json"
json_data = open(myControlFile)
myControl = json.load(json_data) 
json_data = open(myFileSpecFile)
myFileSpec = json.load(json_data)    
json_data.close() 

#perform all the checks for the transmittal sheet
def checkTransmittal(myData):
	cltr = 0
	while cltr < len(myControl["Transmittal Sheet"]):
		myField = myControl["Transmittal Sheet"][cltr]["Transaction Item(s)"]
		myStart = int(myFileSpec["Transmittal Sheet"][0][myField][0]["Start"]) - 1
		myLen  = int(myFileSpec["Transmittal Sheet"][0][myField][0]["Length"])
		myDat = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		myTest = myControl["Transmittal Sheet"][cltr]["Test"]
		myVal  = myControl["Transmittal Sheet"][cltr]["Value"]
#		print line 
#		print myDat + myTest + myVal
		myResult = evaluate(myDat, myTest, myVal, myData)
		if myResult:
			print "     passed: " + myControl["Transmittal Sheet"][cltr]["EDCK"]	
		else:
			print "     FAILED: " + myControl["Transmittal Sheet"][cltr]["EDCK"]	
		cltr = cltr + 1
	return()

#perform all the checks for the LAR
def checkLAR(myData):
	cltr = 0
	while cltr < len(myControl["Loan/Application Register (only)"]):
		myField = myControl["Loan/Application Register (only)"][cltr]["Transaction Item(s)"]
		myStart = int(myFileSpec["Loan/Application Register"][0][myField][0]["Start"]) - 1
		myLen  = int(myFileSpec["Loan/Application Register"][0][myField][0]["Length"])
		myDat = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		myTest = myControl["Loan/Application Register (only)"][cltr]["Test"]
		myVal  = myControl["Loan/Application Register (only)"][cltr]["Value"]
		myResult = evaluate(myDat, myTest, myVal, myData)
		if myResult:
			print "     passed: " + myControl["Loan/Application Register (only)"][cltr]["EDCK"]	
		else:
			print "     FAILED: " + myControl["Loan/Application Register (only)"][cltr]["EDCK"]	
		cltr = cltr + 1
	return()

def evaluate(myDat, myTest, myVal, myData):
	if myTest == "TSID":
		#check to see if the Record Identifier = 1
		if myDat == '1':
			myResult = True
		else:
			myResult = False
	if myTest == "LARID":
		#check to see if the Record Identifier = 1
		if myDat == '2':
			myResult = True
		else:
			myResult = False

	if myTest == "eq":
		#check to see if the myDat is equal to myVal
		if myDat == myVal:
			myResult = True
		else:
			myResult = False
	if myTest == "isNum":
		#check to see if the myDat is a number
		if myDat.isdigit():
			myResult = True
		else:
			myResult = False
	if myTest == "NotNone":
		#check to see if myDat is not null
		if myDat is not None:
			myResult = True
		else:
			myResult = False
	if myTest == "In":
		#check to see if myDat is contained with myVal
		if myDat in myVal:
			myResult = True
		else:
			myResult = False
	if myTest == "ZipFormat":
		#check to see if myDat is in the right ZipCode format
		if len(myDat) == 5:
			if myDat.isdigit():		
				myResult = True
		elif len(myDat) == 10:
			myDat = myDat.replace("-","")
			if myDat.isdigit():
				myResult = True
			else:
				myResult = False
		else:
			myResult = False
	if myTest == "EmailFormat":
		#check to make sure the email is properly formatted
		if myDat.count('@') <> 1 or myDat.count('.@') == 1 or myDat.count('@.') == 1:
			myResult = False
		else:
			myResult = True
	if myTest == "ParentName":
		#check to make sure myDat <> Financial Institution name
		myStart = int(myFileSpec["Transmittal Sheet"][0][myVal][0]["Start"]) - 1
		myLen  = int(myFileSpec["Transmittal Sheet"][0][myVal][0]["Length"])
		myVal = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		if myDat <> myVal:
			myResult = True
		else:
			myResult = False		
	if myTest == "CheckParent":
		#check to make sure address, city, state, ZIP is not null
		myStart = int(myFileSpec["Transmittal Sheet"][0][myVal][0]["Start"]) - 1
		myLen  = int(myFileSpec["Transmittal Sheet"][0][myVal][0]["Length"])
		myVal = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )	
		if myVal is not None:
			if myDat is not None:
				myResult = True
			else:
				myResult = False
		else:
			myResult = False	
	return(myResult)
	
#Create Receipt
cnt = 0
try:
	theFile = open(myFile, 'r')
	with open(myFile, 'r') as f:
		for line in f:
			if cnt == 0: #this is the transmittal sheet
				print "checking Transmittal Sheet ..."
				checkTransmittal(line)
				print "checking LAR Data ..."
			if cnt > 0: #this is the LAR data
				checkLAR(line)
			cnt = cnt + 1
except:
	print "an exception happened"
