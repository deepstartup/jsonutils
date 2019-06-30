# JSON Utils Package (DDLj)

This is a python package having multiple utilities. 
[Github-flavored Markdown](https://github.com/deepstartup/jsonutils/)
DDLj:Convert the JSON schema file into physical DDL file in .sql format.
Below are the input parameter for the package (1.JSON Schema Path,2.DataBase(Default Oracle),3.JSON Output Path,4.Glossary File)

(base) C:\Users\Desktop\original upload>pip install DDLJ
Collecting DDLJ
  Downloading https://files.pythonhosted.org/packages/40/d7/a3f10017c08799dee95863fc8e92e5de6057c396f2d7a5bd1392d76646fd/DDLJ-0.0.1-py3-none-any.whl
Requirement already satisfied: flatten-json in c:\users\appdata\local\continuum\anaconda3\lib\site-packages (from DDLJ) (0.1.7)
Requirement already satisfied: pandas in c:\users\appdata\local\continuum\anaconda3\lib\site-packages (from DDLJ) (0.24.2)
Requirement already satisfied: numpy>=1.12.0 in c:\users\appdata\local\continuum\anaconda3\lib\site-packages (from pandas->DDLJ) (1.16.2)
Requirement already satisfied: python-dateutil>=2.5.0 in c:\users\appdata\local\continuum\anaconda3\lib\site-packages (from pandas->DDLJ) (2.8.0)
Requirement already satisfied: pytz>=2011k in c:\users\appdata\local\continuum\anaconda3\lib\site-packages (from pandas->DDLJ) (2018.9)
Requirement already satisfied: six>=1.5 in c:\users\appdata\local\continuum\anaconda3\lib\site-packages (from python-dateutil>=2.5.0->pandas->DDLJ) (1.12.0)
Installing collected packages: DDLJ
Successfully installed DDLJ-0.0.1

(base) C:\Users>python
>>> from DDLj import genddl
>>> genddl('C:/Users/TestFiles/TestJsonSchema.json','','C:/Users/TestFiles/GlossaryTestFile.csv','C:/Users/TestFiles/GenDDLGlossary.sql')
>>>                                                                                                                     

