import json
import pandas as pd
import re
from flatten_json import flatten,unflatten
import xml.etree.ElementTree as et
temp=[]
DDF_list=[]
ColList=[]
Domain_Com=[]
MinMaxList=[]
colBuild=''
sqlstring=''
colName=''
ArrayList=[]
df=pd.read_csv('C:/Users/ArghadeepChaudhury/Desktop/ddl/raw_glossary_latest.csv')
ldm_xml='C:/Users/ArghadeepChaudhury/Desktop/ML/FundUtility_Ph2_LDM_Model_20190320_V4.0.ldm'
#file_path='C:/Users/ArghadeepChaudhury/Desktop/ML/FINANCIAL_TRANSACTION.json'
xtree = et.parse(ldm_xml)
xroot = xtree.getroot()
for child in xroot:
    if child.tag == '{http:///com/ibm/db/models/logical/logical.ecore}AtomicDomain':
        Domain_Com=[child.attrib.get("name"),child.attrib.get("baseType")]
        DDF_list.append(Domain_Com)
DomainDF=pd.DataFrame(DDF_list,columns=['Name','Value'])

def L2P_builder(char):
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

def StringEnds(char):
    q=0
    colval=''
    splitted = re.sub('(?!^)([A-Z][a-z]+)', r' \1', char).split()
    for val in splitted:
        q=q+1
        if q==len(splitted):
            return val

def LDMDomainDataType(PhyColName):
    try:
        PhyDataType=DomainDF.loc[df.Name == PhyColName, 'Value'].item()
    except Exception as e:
        PhyDataType='Number(38,10)'
    return PhyDataType
with open(file_path) as json_data:
    json_schema=json.load(json_data)
json_schema_flat = flatten(json_schema)
def sqlStrinNthLevel(n,ValStr):
    sqlstring=''
    #ColList=[]
    for keys,vals in json_schema_flat.items():
        try:
            arrayField=keys.split('_')[1]
        except:
            arrayField=None
        if ValStr==None:
            if keys.endswith('_type') and keys.count('_')==n:
                if vals=='string' and keys.count('_')==n:
                    try:
                        maxLength=eval("json_schema_flat['"+keys[:len(keys)-5]+"_maxLength"+"']")
                        sqlstring=L2P_builder(keys.split("_")[n-1])+" Varchar2("+str(maxLength)+"),"
                        ColList.append(sqlstring)
                    except Exception as e:
                        if keys[:len(keys)-5].endswith('Date') and keys.count('_')==n:
                            sqlstring=L2P_builder(keys.split("_")[n-1])+" Date,"
                            ColList.append(sqlstring)
                        elif (keys[:len(keys)-5].endswith('Timestamp') or keys[:len(keys)-5].endswith('DateTime')) and keys.count('_')==n:
                            sqlstring=L2P_builder(keys.split("_")[n-1])+" Timestamp(6),"
                            ColList.append(sqlstring)
                        else:
                            e
                elif vals=='number' and keys.count('_')==n:
                    Endword=StringEnds(keys.split("_")[n-1])
                    sqlstring=L2P_builder(keys.split("_")[n-1])+" "+LDMDomainDataType(Endword)+","
                    ColList.append(sqlstring)
                elif vals=='object' and keys.count('_')==n:
                    sqlStrinNthLevel(n+2,None)
        elif ValStr!=None and arrayField==ValStr:
            if keys.endswith('_type') and arrayField==ValStr and keys.count('_')==n:
                if vals=='string' and keys.count('_')==n:
                    try:
                        maxLength=eval("json_schema_flat['"+keys[:len(keys)-5]+"_maxLength"+"']")
                        sqlstring=L2P_builder(keys.split("_")[n-1])+" Varchar2("+str(maxLength)+"),"
                        ColList.append(sqlstring)
                    except Exception as e:
                        if keys[:len(keys)-5].endswith('Date') and keys.count('_')==n:
                            sqlstring=L2P_builder(keys.split("_")[n-1])+" Date,"
                            ColList.append(sqlstring)
                        elif (keys[:len(keys)-5].endswith('Timestamp') or keys[:len(keys)-5].endswith('DateTime')) and keys.count('_')==n:
                            sqlstring=L2P_builder(keys.split("_")[n-1])+" Timestamp(6),"
                            ColList.append(sqlstring)
                        else:
                            e
                elif vals=='number' and arrayField==ValStr and keys.count('_')==n:
                    Endword=StringEnds(keys.split("_")[n-1])
                    sqlstring=L2P_builder(keys.split("_")[n-1])+" "+LDMDomainDataType(Endword)+","
                    ColList.append(sqlstring)
                elif vals=='object' and arrayField==ValStr and keys.count('_')==n:
                    sqlStrinNthLevel(n+2,ValStr)
    return ColList
def GenDDL(JsonSchemaFilePath):
    f=sqlStrinNthLevel(2,None)
    f = list(dict.fromkeys(f))
    ColList=[]
    print(f)
    for p,q in json_schema_flat.items():
        if q=='array':
            ArrayList.append(p.split('_')[1])
    for Array_DDLs in ArrayList:
        f=sqlStrinNthLevel(6,Array_DDLs)
        f = list(dict.fromkeys(f))
        ColList=[]
        print(f)
    return f
if __name__ == "__main__": 
    GenDDL(JsonSchemaFilePath)