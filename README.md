# JSON Utils Package (DDLj)
This is a python package having multiple utilities. 
[Github-flavored Markdown](https://github.com/deepstartup/jsonutils/)
DDLj:Convert the JSON schema file into physical DDL file in .sql format.
Below are the input parameter for the package (1.JSON Schema Path,2.Database Name,3.JSON Output Path,4.Glossary File)

1.DDLj : Converts JSON Schema Files into ANSI SQL DDLs (Mostly tested with Oracle)
Also support for 
A.PostgreSQL
B.MYSQL
C.DB2
D.MariaDB
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Usage:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
pip install DDLJ

python

>>> from DDLj import genddl

>>> genddl(*param1,param2,*param3,*param3)

Where 

param1= JSON Schema File

param2=Database (Default Oracle)

Param3= Glossary file

Param4= DDL output script

Note : * indicates mandatory parameters
Please see the Test Folder for example

****************************
APP : Contains a flask application, which generates and downloads DDL script 
Test :  Contains Test files and scripts to run the DDLj
