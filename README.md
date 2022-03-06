# cs5293sp22-project0
Text Analytics Project 0

Author: Vudumula Kranthi Kumar Reddy

# About

In this project we deal with python, Linux commands, and some of the extract information tools to extract the data from the pdf files. Usually, The files present in the NPD (Norman Police Deparment) Activity Reports are of three types arrests, incidents, and case summaries. In this project we download the incidents data and extract the required data from the pdfs like Date / Time, Incident Number, Location, Nature and Incident ORI. Then after sorting the data we create a database in SQLite and store the data into the database.

Required Output: Print each nature and the number of times it appears.

# Required Packages

The below mentioned are the required list of packages for this project:

-argparse
-Pandas
-PyPDF2
-re
-sqlite3
-tempfile
-urllib

From the above mentioned packages,

-install PyPDF2 and Pandas with the command [pipenv install package]
-other all are the standard libraries which can be installed in python.

# Description

In this project Initially we should downlaod a Incident PDF File from the Norman Police Department Activity Reports.

After that, Create two files with files names as main.py and project0.py.

1. main.py

This file is used for the processing of the data and to get the output. Generally, there are five functions implemented in this file such as,

- fetchincidents() : 

- extractincidents() :  

- createdb() : 

- populatedb() : 

- status() : 

2. project0.py

- fetchincidents(url) : 

- extractincidents(incidents) :  

- createdb() : 

- populatedb(incidents) : 

- status() :

