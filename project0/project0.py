import pandas as pd
import PyPDF2
import re 
import sqlite3
import tempfile
import urllib.request

def fetchincidents(url):
    headers={}
    headers['User-Agent']="Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"                          
    incidents=urllib.request.urlopen(urllib.request.Request(url, headers=headers)).read()
    return incidents

def extractincidents(incidents):
    fp=tempfile.TemporaryFile()
    fp.write(incidents)
    fp.seek(0)
    pdfReader=PyPDF2.pdf.PdfFileReader(fp)
    pagenum=pdfReader.getNumPages()
    #print("number of pages in the pdf",pagenum)

    flist=[]
    for i in range(pagenum):
        page1=pdfReader.getPage(i).extractText()
        list1=page1.split('\n')
        #print(list1.count('\n'),end="--\n")
        #print(list1)
        if i==0:
            list1=list1[5:-3]
        if i==pagenum-1:
            list1=list1[:-2] 
        flist.append(list1)
    
    flist1=[]

    for k in range(0,len(flist)):
        cnt=0
        temp=[]
        #print("flist lenght: ",len(flist[k]))
        i=0
        while(i<=len(flist[k])-5):
            #print(flist[k])
            date_match=re.search(r'(\d+/\d+/\d+)',flist[k][i])
            if(date_match!=None):
                cnt=cnt +1
                #adding to the temp list
                temp.append(flist[k][i])
                ino_match=re.search(r"2022-\w+", flist[k][i+1])

                if(ino_match!=None):
                    cnt=cnt+1
                    #adding to the temp list
                    temp.append(flist[k][i+1])
                    io_match0=re.search("^OK0", flist[k][i+2])
                    io_match1=re.search("^EMS",flist[k][i+2])
                    io_match2=re.search("^14005",flist[k][i+2])
                    #print(io_match2)

                    if(io_match0!=None or io_match1!=None or io_match2!=None):  
                        cnt=cnt + 1
                        #null values are present
                        temp.append('NA')
                        temp.append('NA')
                        temp.append(flist[k][i+2])
                        #print("NA insetion: ",temp)
                    else:
                        cnt=cnt + 3
                        o_match0=re.search("^OK0", flist[k][i+4])
                        o_match1=re.search("^EMS",flist[k][i+4])
                        o_match2=re.search("^14005",flist[k][i+4])

                        # checking if 2nd column data is in newline
                        if(o_match0==None and o_match1==None and o_match2==None):
                            # if 2nd column data has new lines 
                            # append 2nd and 3rd column as single column
                            temp.append(flist[k][i+2]+flist[k][i+3])
                            #append the remaining columns
                            temp.append(flist[k][i+4])
                            temp.append(flist[k][i+5])
                        else:
                            #there are no newlines in 2nd column(index 0)
                            temp.append(flist[k][i+2])
                            temp.append(flist[k][i+3])
                            temp.append(flist[k][i+4]) 
                        #print("normal insetion: ",temp)

            if(cnt==5 or cnt==3):
                i=cnt + i
                #print(cnt)
                flist1.append(temp)
                cnt=0
                temp=[]
            else:
                i=i+1
            #print("i values after : ",i)
        #print(flist1,end="\n")
    #print(len(flist1))
    df=pd.DataFrame(flist1)
    df.columns=["Date / Time","Incident Number","Location", "Nature","Incident ORI"]
    
    return df 
    #print(df.tail(60))

db='norman.db'

def createdb():
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS incidents (
    incident_time TEXT,
    incident_number TEXT,
    incident_location TEXT,
    nature TEXT,
    incident_ori TEXT);""")
    print("database created successfully")
    conn.commit()
    conn.close()

    return db

def populatedb(incidents):
    conn=sqlite3.connect(db)
    c=conn.cursor()
    c.execute('delete from incidents')
    conn.commit()

    for i in range(len(incidents)) :
        final=(incidents.iloc[i, 0], incidents.iloc[i, 1],incidents.iloc[i, 2],incidents.iloc[i, 3],incidents.iloc[i, 4])
        c.execute('insert into incidents values(?,?,?,?,?)',final)
        conn.commit()
    conn.close()

def status():
    conn=sqlite3.connect(db)
    c=conn.cursor()
    try:
        c.execute('select Nature , count(*) from incidents group by Nature order by Nature asc ')
    except e:
        print("unable to write to db")   
    result=c.fetchall()

    for value in result:
        print(str(value[0])+" | "+str(value[1]))
    return result
