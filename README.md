# cs5293sp22-project0
Text Analytics Project 0

Author: Vudumula Kranthi Kumar Reddy

# About

In this project we deal with python, Linux commands, and some of the extract information tools to extract the data from the pdf files. Usually, The files present in the NPD (Norman Police Deparment) Activity Reports are of three types arrests, incidents, and case summaries. In this project we download the incidents data and extract the required data from the pdfs like Date / Time, Incident Number, Location, Nature and Incident ORI. Then after sorting the data we create a database in SQLite and store the data into the database.

Required Output: Print each nature and the number of times it appears.

# Required Packages

The below mentioned are the required list of packages for this project:

- argparse
- pandas
- PyPDF2
- re
- sqlite3
- tempfile
- urllib

From the above mentioned packages,

- install PyPDF2 and Pandas with the command [pipenv install package].

- other all are the standard libraries which can be installed in python.

# Description

In this project Initially we should downlaod a Incident PDF File from the Norman Police Department Activity Reports.

After that, Create two files with files names as main.py and project0.py. Additionally, we have to create a test_data.py for testing purpose. 

1. main.py

This file is used for the processing of the data and to get the output. Generally, there are five functions implemented in this file such as,

a. project0.fetchincidents(url) : is used to fetch data from the incidents reports url.
 
b. project0.extractincidents(incidents) : is used to extract and parse the data and store the data in the form lists to insert into the database.
 
c. project0.createdb() : is used to create a new datbase. 

d. project0.populatedb(incidents) : is used to insert the data that is present in the form of lists into a database.

e. project0.status() : is used to fetch the required output.

2. project0.py

a. fetchincidents(url) :

This method is used to input different incident url's where we take url as the input. The urllib package that we use in this method is used to read the data from the provided input url.   

b. extractincidents(incidents) :

This method takes incidents as the input and then reads the data from the input and writes it into a temporary file. In this method, PyPdf2 is used to extract the data from the pdf file that we get from the url. 

Then, after reading the data we store the entire data into a list by splitting them with a newline. Later, I am slicing the data because there is some unwanted data which has to be removed.

After removing the unwanted data, still there is some data irregularities in the data like at some places there is no data present  which has to be filled with some Null Values. So, I have inserted 'NA' values in place of the empty spaces.

Lastly, I have appended all the data with count 5 splitting in different lists. Using Pandas I have arranged the data in the form of rows and columns.

c. createdb() :

This method is usually used for creating a database by connecting to SQLite3. Then, after the connection is established we create a cursor object and call its execute method to perform the passed SQL commands. Then at last we commit and save the changes made.

d. populatedb(incidents) : 

This method is used to connect to a database and stores the data that we take as a input into the incidents database.


e. status() : 

In this method we connect to the database and output the Nature field with their count's.

3. test_data.py

a. fetchincidents(url) : 

This method is used to test fetchincidents(url) in project0.py. Here, I am trying to verify whether the returned data is empty or not.

b. extractincidents(incidents) :

This method is used for testing the extractincidents(incidents) in project0.py. Here, I am checking whether the list is empty or not, if the return type is list or not and if the length of each incident is equal to 5 or not.

c. createdb() : 

This method is used for testing the createdb() in project0.py. Here, In this method I am trying to check whether the table that is created is empty or not.

d. populatedb(incidents) : 

This method is used for testing the populatedb(incidents) in project0.py. Here, In this method I am trying to check whether the data that we are receiving is properly inserted or not.

e. status() : 

This method is used for testing the status() in project0.py. Here, In this method I am trying to verify whether the data that we have received in the extractincidents(incidents) is of list type or not.

# How to run the Project

- Command:

pipenv run python project0/main.py --incidents https://www.normanok.gov/sites/default/files/documents/2022-02/2022-02-27_daily_incident_summary.pdf

- Output: [ Nature Column Data | Count of Data in Nature Column ]

Example, Cardiac Respritory Arrest|4

# How to run the test cases

- Command:

pipenv run python -m pytest -v

- Output: 

![output](https://user-images.githubusercontent.com/98420519/157361278-a717fb8d-4517-4836-8da9-6e393b8cf3be.png)

