# This Source Code Form is subject to the terms of the MIT Public
# License, v. 2.0. If a copy of the MIT was not distributed with this
# file, You can obtain one at MIT License :: OSI Approved :: MIT License
#Author : Arghadeep Chaudhury,Siddhartha Bhattacharya
#author_email"siddhbhatt@gmail.com,arghadeep.chaudhury@gmail.com"
#Created on Thu Jun 27 15:55:51 2019
# -*- coding: utf-8 -*-

import json
import pandas as pd
import re
from flatten_json import flatten,unflatten
temp=[]
DDF_list=[]
ColList=[]
Domain_Com=[]
MinMaxList=[]
colBuild=''
sqlstring=''
colName=''
ArrayList=[]
Empty_Df=[]

#L2P_builder function convert the logical name to physical name using glossary words 
#separated by '_', if No glossary input has been provided, this has return as is logical name
def L2P_builder(char,Glossarypath):
    if Glossarypath==None or Glossarypath=='':
        try:
            df=pd.DataFrame(columns=['Name','Abbreviation'])
        except:
            print('No Glossary')
    else:
        try:
            df=pd.read_csv(Glossarypath)
        except:
            df=pd.DataFrame(columns=['Name','Abbreviation'])
    q=0
    colval=''
    splitted = re.sub('(?!^)([A-Z][a-z]+)', r' \1', char).split()
    for val in splitted:
        q=q+1
        if q==len(splitted):
            if val[len(val)-2:len(val)]=='ID':
                try:
                    val=df.loc[df.Name == val[0:len(val)-2], 'Abbreviation'].item()
                    val=val+'_ID'
                    colval+=val
                except:
                    val=val[0:len(val)-2]
                    val=val+'_ID'
                    colval+=val
            else:
                try:
                    val=df.loc[df.Name == val, 'Abbreviation'].item()
                    colval+=val
                except:
                    colval+=val
        else:
            try:
                val=df.loc[df.Name == val, 'Abbreviation'].item()
                val=val+'_'
                colval+=val
            except:
                val=val+'_'
                colval+=val
    return colval
#StringEnds: return the last character value from a String with camelcase
def StringEnds(char):
    q=0
    colval=''
    splitted = re.sub('(?!^)([A-Z][a-z]+)', r' \1', char).split()
    for val in splitted:
        q=q+1
        if q==len(splitted):
            return val
#Recursive function to generate the DDL string array using the flatten json 
def sqlStrinNthLevel(json_schema_flat,n,ValStr,Glossarypath):
    sqlstring=''
    ColList=[]
    for keys,vals in json_schema_flat.items():
        try:
            arrayField=keys.split('_')[1]
        except:
            arrayField=None
        if ValStr==None:
            if (keys.endswith('_type') or keys.endswith('_format')) and keys.count('_')==n:
                if vals=='string' and keys.endswith('_type') and keys.count('_')==n:
                    try:
                        maxLength=eval("json_schema_flat['"+keys[:len(keys)-5]+"_maxLength"+"']")
                        sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Varchar2("+str(maxLength)+"),"
                        ColList.append(sqlstring)
                    except Exception as e:
                        if keys[:len(keys)-5].endswith('Date') and keys.count('_')==n:
                            sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Date,"
                            ColList.append(sqlstring)
                        elif (keys[:len(keys)-5].endswith('Timestamp') or keys[:len(keys)-5].endswith('DateTime')) and keys.count('_')==n:
                            sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Timestamp(6),"
                            ColList.append(sqlstring) 
                        else:
                            e
                elif vals=='number' and keys.count('_')==n:
                    Endword=StringEnds(keys.split("_")[n-1])
                    sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Number(38,10),"
                    ColList.append(sqlstring)
                elif vals=='date' and keys.endswith('_format') and keys.count('_')==n:
                    sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Date,"
                    ColList.append(sqlstring)
                elif vals=='date-time' and keys.endswith('_format') and keys.count('_')==n:
                    sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Timestamp(6),"
                    ColList.append(sqlstring)
                elif vals=='boolean' and keys.endswith('_format') and keys.count('_')==n:
                    sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Char(1),"
                    ColList.append(sqlstring)
                elif vals=='object' and keys.count('_')==n:
                    sqlStrinNthLevel(json_schema_flat,n+2,None,Glossarypath)
        elif ValStr!=None and arrayField==ValStr:
            if keys.endswith('_type') and arrayField==ValStr and keys.count('_')==n:
                if vals=='string' and keys.count('_')==n:
                    try:
                        maxLength=eval("json_schema_flat['"+keys[:len(keys)-5]+"_maxLength"+"']")
                        sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Varchar2("+str(maxLength)+"),"
                        ColList.append(sqlstring)
                    except Exception as e:
                        if keys[:len(keys)-5].endswith('Date') and keys.count('_')==n:
                            sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Date,"
                            ColList.append(sqlstring)
                        elif (keys[:len(keys)-5].endswith('Timestamp') or keys[:len(keys)-5].endswith('DateTime')) and keys.count('_')==n:
                            sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Timestamp(6),"
                            ColList.append(sqlstring)
                        else:
                            e
                elif vals=='number' and arrayField==ValStr and keys.count('_')==n:
                    Endword=StringEnds(keys.split("_")[n-1])
                    sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Number(38,10),"
                    ColList.append(sqlstring)
                elif vals=='date' and keys.endswith('_format') and keys.count('_')==n:
                    sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Date,"
                    ColList.append(sqlstring)
                elif vals=='date-time' and keys.endswith('_format') and keys.count('_')==n:
                    sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Timestamp(6),"
                    ColList.append(sqlstring)
                elif vals=='boolean' and keys.endswith('_format') and keys.count('_')==n:
                    sqlstring=L2P_builder(keys.split("_")[n-1],Glossarypath)+" Char(1),"
                    ColList.append(sqlstring)
                elif vals=='object' and arrayField==ValStr and keys.count('_')==n:
                    sqlStrinNthLevel(sqlStrinNthLevel,n+2,ValStr,Glossarypath)
    return ColList

#Writing to the outputfile path
def callMain(file_path,Database,Glossarypath,outputfilePath):
    with open(file_path) as json_data:
        json_schema=json.load(json_data)
    json_schema_flat = flatten(json_schema)
    if Glossarypath==None or Glossarypath=='':
        try:
            df=pd.DataFrame(columns=['Name','Abbreviation'])
        except:
            print('no glossary')
    else:
        try:
            df=pd.read_csv(Glossarypath)
        except:
            df=pd.DataFrame(columns=['Name','Abbreviation'])
    try:
        FileOpen=open(outputfilePath, "w+")
        f=sqlStrinNthLevel(json_schema_flat,2,None,Glossarypath)
        f = list(dict.fromkeys(f))
        for flat_x,flat_y in json_schema_flat.items():
            if flat_x=='title':
                Table_Name=flat_y
        DDLout='Create Table '+Table_Name+' ('
        for ddlTxt in f:
            #Default Database is Oracle,Supported for below as well
            if Database in ('PostgreSQL','MYSQL','DB2','MariaDB'):
                ddlTxt=ddlTxt.replace(' Varchar2',' Varchar')
                ddlTxt=ddlTxt.replace(' Number(38,10)',' NUMERIC(38,10)')
                ddlTxt=ddlTxt.replace(' Timestamp(6)',' Timestamp')
                ddlTxt=ddlTxt.replace(' Char(1)',' boolean')
            DDLout=DDLout+ddlTxt+'\n'
        DDLout=DDLout[:len(DDLout)-2]+');'
        FileOpen.write(DDLout)
        for p,q in json_schema_flat.items():
            if q=='array':
                ArrayList.append(p.split('_')[1])
        for Array_DDLs in ArrayList:
            DDLoutChild='\n\n'
            First=sqlStrinNthLevel(json_schema_flat,6,Array_DDLs,Glossarypath)
            First = list(dict.fromkeys(First))
            DDLoutChild='\nCreate Table '+Array_DDLs[:len(Array_DDLs)-5]+' ('
            for listFst in First:
                DDLoutChild=DDLoutChild+listFst+'\n'
            DDLoutChild=DDLoutChild[:len(DDLoutChild)-2]+');'
            FileOpen.write(DDLoutChild)
        FileOpen.close()
    except:
        df=pd.DataFrame(columns=['Name','Abbreviation'])
def genddl(file_path,Database,Glossarypath,outputfilePath):
    try:
        with open(file_path) as json_data:
            json_schema=json.load(json_data)
        json_schema_flat = flatten(json_schema)
        callMain(file_path,Database,Glossarypath,outputfilePath)
    except Exception as e:
        print(e)
if __name__ == '__main__':
    genddl(file_path,Database,Glossarypath,outputfilePath)