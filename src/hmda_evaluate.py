### ---------------------------------------------------------------------------
###   VERSION 0.1 
### hmda_evaluate.py
### Created on: Thirs Aug 28 2014
### Created by: Michael Byrne
### Consumer Finance Protection Bureau 
### ---------------------------------------------------------------------------
### tests controller model the pilot for the pilot of HMDA collection operations
### this portion is the evaluation engine;
### this accepts the data, the test, any values to test agains, and the full line
### and passes back a boolean that it passed or not
### ---------------------------------------------------------------------------

#move this function to a subscript hmda_evaualte
#the arguments are 	        (0) - myDat - the string in the data to be tested (eg start:end) or V1
# 				(1) - myTest - the test to be performed; used in 'case' statements here
#				(2) - myVal - NOT USED IN ALL TESTS
#						the value to test against (if any - like the state list)
#				(3) - myData - the full line of the data incase some other 
#						field needs accessing
#				(4) - myFileSpec - the full json object of the the file spec document
#						used to help splice other field values you might need to 
#						to test

def evaluate(myDat, myTest, myVal, myData, myFileSpec):
	if myTest == "TSID":
		#check to see if the Record Identifier = 1
		if myDat == '1':
			myResult = True
		else:
			myResult = False
	elif myTest == "LARID":
		#check to see if the Record Identifier = 1
		if myDat == '2':
			myResult = True
		else:
			myResult = False
	elif myTest == "eq":
		#check to see if the myDat is equal to myVal
		if myDat == myVal:
			myResult = True
		else:
			myResult = False
	elif myTest == "isNum":
		#check to see if the myDat is a number
		if myDat.isdigit():
			myResult = True
		else:
			myResult = False
	elif myTest == "NotNone":
		#check to see if myDat is not null
		if myDat is not None:
			myResult = True
		else:
			myResult = False
	elif myTest == "In":
		#check to see if myDat is contained with myVal
		if myDat in myVal:
			myResult = True
		else:
			myResult = False
	elif myTest == "ZipFormat":
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
	elif myTest == "EmailFormat":
		#check to make sure the email is properly formatted
		if myDat.count('@') <> 1 or myDat.count('.@') == 1 or myDat.count('@.') == 1:
			myResult = False
		else:
			myResult = True
	elif myTest == "PhoneFormat":
		#check to make sure the phone/fax is properly formatted
		if len(myDat) == 12 and myDat.count('-') == 2 and myDat is not None:
			myResult = True
		else:
			myResult = False
	elif myTest == "TaxIDFormat":
		#check to make sure the TaxID Number is properly formatted
		if len(myDat) == 10 and myDat.count('-') == 1 and myDat <> "99-9999999" and myDat <> "00-0000000":
			myResult = True
		else:
			myResult = False
	elif myTest == "DiffString":
		#check to make sure myDat <> some other value (e.g. Financial Institution) name
		myStart = int(myFileSpec["Transmittal Sheet"][0][myVal][0]["Start"]) - 1
		myLen  = int(myFileSpec["Transmittal Sheet"][0][myVal][0]["Length"])
		myVal = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		if myDat <> myVal:
			myResult = True
		else:
			myResult = False		
	elif myTest == "CheckParent":
		#check to make sure address, city, state, ZIP is not null, if there is a parent
		#name added
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
	elif myTest == "NotBlankOrZero25":
		#check to make sure the value isn't blank or all zero's
		if myDat is not None and myDat <> '0000000000000000000000000':
			myResult = True
		else:
			myResult = False	
	elif myTest == "DateFormat":
		#check to make sure the dateformat is ok
		if myDat.isdigit() and int(myDat[0:2]) == 20 and int(myDat[4:6]) > 0 and int(myDat[4:6]) < 13 and int(myDat[6:8]) > 0 and int(myDat[6:8]) < 32:
			myResult = True
		else:
			myResult = False  
	elif myTest == "IfThenOtherFieldValue":
		#the equation is if F1v = F1tv, then F2v must = F2tv
		#check to see if a value in one field exists, if so the value of another field 
		#needs to be a certain thing
		#F1v = is the value in data (e.g. myDat)
		#F1tv is in myVal
		#F2v is in myVal
		#Ft2v is in myVal
		F1tv = myVal[0]["F1tv"]
		F2 = myVal[0]["F2"]
		F2tv = myVal[0]["F2tv"]
		myStart = int(myFileSpec["Loan Application Register"][0][F2][0]["Start"]) - 1
		myLen   = int(myFileSpec["Loan Application Register"][0][F2][0]["Length"])
		F2v = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		if myDat in (F1tv):
			if F2v in (F2tv):
				myResult = True
			else:
				myResult = False
		else:
			myResult = True	
	elif myTest == "IfAndThenOtherFieldValue":
		#the equation is if F1v = F1tv and F2v = F2tv, then F3v must = F3tv
		#check to see if a value in one field exists
		#OR if another field is a certain value, if so the value of another field 
		#needs to be a certain thing
		#F1v = is the value in data (e.g. myDat)
		#F1tv is in myVal
		#F2v is in myVal; F2tv is in myVal
		#F3v is in myVal; F3tv is in myVal		
		F1tv = myVal[0]["F1tv"]
		F2 = myVal[0]["F2"]
		F2tv = myVal[0]["F2tv"]
		myStart = int(myFileSpec["Loan Application Register"][0][F2][0]["Start"]) - 1
		myLen   = int(myFileSpec["Loan Application Register"][0][F2][0]["Length"])
		F2v = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		F3 = myVal[0]["F3"]
		F3tv = myVal[0]["F3tv"]
		myStart = int(myFileSpec["Loan Application Register"][0][F3][0]["Start"]) - 1
		myLen   = int(myFileSpec["Loan Application Register"][0][F3][0]["Length"])	
		F3v = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		if myDat in (F1tv) and F2v in (F2tv):
			print "F3v: " + F3v + " F3tv: " + F3tv
			if F3v in (F3tv):
				myResult = True
			else:
				myResult = False
		else:
			myResult = True
	elif myTest == "IfOrThenOtherFieldValue":
		#the equation is if F1v = F1tv or F2v = F2tv, then F3v must = F3tv
		#check to see if a value in one field exists
		#OR if another field is a certain value, if so the value of another field 
		#needs to be a certain thing
		#F1v = is the value in data (e.g. myDat)
		#F1tv is in myVal
		#F2v is in myVal; F2tv is in myVal
		#F3v is in myVal; F3tv is in myVal		
		F1tv = myVal[0]["F1tv"]
		F2 = myVal[0]["F2"]
		F2tv = myVal[0]["F2tv"]
		myStart = int(myFileSpec["Loan Application Register"][0][F2][0]["Start"]) - 1
		myLen   = int(myFileSpec["Loan Application Register"][0][F2][0]["Length"])
		F2v = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		F3 = myVal[0]["F3"]
		F3tv = myVal[0]["F3tv"]
		myStart = int(myFileSpec["Loan Application Register"][0][F3][0]["Start"]) - 1
		myLen   = int(myFileSpec["Loan Application Register"][0][F3][0]["Length"])	
		F3v = eval( "myData[" + str(myStart) + ":" + str(myStart + myLen) + "]" )
		if myDat in (F1tv) or F2v in (F2tv):
			print "F3v: " + F3v + " F3tv: " + F3tv
			if F3v in (F3tv):
				myResult = True
			else:
				myResult = False
		else:
			myResult = True

	elif myTest == "NumericGT0":
		#check to make sure the dateformat is ok
		if myDat.isdigit() and int(myDat) > 0:
			myResult = True
		else:
			myResult = False  
	#myDat, myTest, myVal, myData, myFileSpec
#	print "myDat: " + myDat
#	print "myTest: " + myTest
#	print "myVal: " + myVal
#	print "myData: " + myData
#	print "myFileSpec: " + myFileSpec 
	return(myResult)
