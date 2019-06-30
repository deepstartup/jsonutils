
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