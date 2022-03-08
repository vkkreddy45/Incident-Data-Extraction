from project0 import project0
import pytest
import PyPDF2
import re
import sqlite3
import tempfile

url="https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-27_daily_incident_summary.pdf"

def test_fetchincidents():
    f = project0.fetchincidents(url)  
    assert f is not None  

def test_extractincidents():

    e = extractedpdfdata()

    assert len(e) != 0
    assert type(e) is list

    for values in e:
        assert len(values)==5  

def test_createdb():
    db = project0.createdb() 
    conn = sqlite3.connect(db)  
    c = conn.cursor()  
    d = c.execute('select * from incidents;')
    assert c.fetchall()==[]  

def test_populatedb(): 
    db = project0.createdb()
    conn = sqlite3.connect(db)
    c = conn.cursor()
    res = c.execute('select * from incidents;')
    assert res != None

def extractedpdfdata():
    a = project0.fetchincidents(url)
    fp = tempfile.TemporaryFile()
    fp.write(a)
    fp.seek(0)
    pdfReader = PyPDF2.pdf.PdfFileReader(fp)
    pagenum = pdfReader.getNumPages()
    #print("number of pages in the pdf",pagenum)

    flist=[]

    for i in range(pagenum):
        page1 = pdfReader.getPage(i).extractText()
        list1 = page1.split('\n')
        #print(list1.count('\n'),end="--\n")
        #print(list1)
        if i==0:
            list1 = list1[5:-3]
        if i == pagenum-1:
            list1= list1[:-2] 
        flist.append(list1)
    
    flist1 = []

    for k in range(0,len(flist)):
        cnt = 0
        temp=[]
        #print("flist lenght: ",len(flist[k]))
        i=0
        while(i<=len(flist[k])-5):
            #print(flist[k])
            date_match = re.search(r'(\d+/\d+/\d+)',flist[k][i])
            if(date_match!=None):
                cnt = cnt +1
                #adding to the temp list
                temp.append(flist[k][i])
                ino_match = re.search(r"2022-\w+", flist[k][i+1])

                if(ino_match!=None):
                    cnt = cnt+1
                    #adding to the temp list
                    temp.append(flist[k][i+1])
                    io_match0 = re.search("^OK0", flist[k][i+2])
                    io_match1 = re.search("^EMS",flist[k][i+2])
                    io_match2 = re.search("^14005",flist[k][i+2])
                    #print(io_match2)

                    if(io_match0!=None or io_match1!=None or io_match2!=None):  
                        cnt = cnt + 1
                        #null values are present
                        temp.append('NA')
                        temp.append('NA')
                        temp.append(flist[k][i+2])
                        #print("NA insetion: ",temp)
                    else:
                        cnt = cnt + 3
                        o_match0 = re.search("^OK0", flist[k][i+4])
                        o_match1 = re.search("^EMS",flist[k][i+4])
                        o_match2 = re.search("^14005",flist[k][i+4])

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
                i = cnt + i
                #print(cnt)
                flist1.append(temp)
                cnt = 0
                temp = []
            else:
                i = i+1
        return flist1

def test_status():
    res = project0.status()
    assert type(res) == list
