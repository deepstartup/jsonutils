# JSON Utils Package (DDLj)
This is a python package having multiple utilities for handling JSON Files. 

1.DDLj : Converts JSON Schema Files into ANSI SQL DDLs
Supports foll databases: 
A.PostgreSQL
B.MYSQL
C.DB2
D.MariaDB
E.Oracle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Usage:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install DDLJ

python

>>> from DDLj import genddl

>>> genddl(*param1,param2,*param3,*param4)

Where 

param1= JSON Schema File

param2=Database (Default Oracle)

Param3= Glossary file

Param4= DDL output script

Note : * indicates mandatory parameters

It also includes a Flask module for front-end if used as a standalone tool. Refer to App directory.
*******************************************
Example:
Input JSON schema as:
{
	"schema": "Http://Json-Schema.Org/Draft-07/Schema#",
	"type": "object",
	"title": "TableNameTest",
	"additionalProperties": false,
	"properties": {
		"ColumnNameOne": {
			"type": "string",
			"maxLength": 10
		},
		"ColumnNameTwo": {
			"type": "string",
			"format": "date-time"
		},
		"ColumnNameThree": {
			"type": "string",
			"maxLength": 200
		},
		"ColumnNameFour": {
			"type": "string",
			"maxLength": 300
		},
		"ColumnNameFive": {
			"type": "string",
			"format": "date"
		},
		"ColumnNameSix": {
			"type": "number"
		},
		"ColumnNameSeven": {
			"type": "number"
		},
		"ColumnNameEight": {
			"type": "string",
			"maxLength": 1000
		},
		"ColumnNameNine": {
			"type": "string",
			"maxLength": 2000
		},
		"ColumnNameTen": {
			"type": "number"
		}
	}
}

Code Usage:
>>> from DDLj import genddl
>>> genddl('TestJsonSchema.json','Oracle','GlossaryTestFile.csv','GenDDLGlossary.sql')

Output:
Create Table TableNameTest (COL_NAM_One Varchar2(10),
COL_NAM_Two Timestamp(6),
COL_NAM_Three Varchar2(200),
COL_NAM_Four Varchar2(300),
COL_NAM_Five Date,
COL_NAM_Six Number(38,10),
COL_NAM_Seven Number(38,10),
COL_NAM_Eight Varchar2(1000),
COL_NAM_Nine Varchar2(2000),
COL_NAM_Ten Number(38,10));

Please see the Test Folder for JSON schema, glossary file and output.
****************************
