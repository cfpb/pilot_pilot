hmda_model_flow.md
==================

- open a .dat file
- open the controller.json file (has the edit rules)
	- look at the structure of the controller file
	- 3 nodes (metadata, transmittal sheet, LAR)
	- nodes for TS and LAR follow the edit doc structure
		- Item, Number, Edit Desc; Error Desc plus
		- Test; Value

- open the file_spec.json file (has the structure of the fixed field data file)
	- look at the structure of file spec document
	- 3 nodes (metadata, transmittal sheet, LAR)
	- nodes for TS and LAR follow the file spec doc structure
		- Element; Label; Start; End; Length; Data Type; Comment

- open and read each line of the .dat file
	- if it is a transmittal sheet row, perform those tests
	- if is is a LAR row, perform those tests

- each test has a taxonomy
	- eq; isNum; NotNone; In; ZipFormat; DiffString; IfThenOtherField; 
	- IfThenOtherFieldValue; IfOrThenOtherFieldValue; 
	
- for each test, pass the
	- value to test
	- the test taxonomy
	- the accepted values (not in all tests)
	- the full line data (in case you need for IfThenOtherField)
	- the file spec document (in case you need for IfThenOtherField)

- for each test return
	- passed; edit check number; value	
