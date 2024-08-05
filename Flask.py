"""
Title
Date
Author
"""

from flask import Flask, render_template, request, redirect
import csv


### VARIABLES
FILENAME = "Flask.csv"
app = Flask(__name__)

### FLASK
@app.route('/', methods={"GET", "POST"})

def index():
    ALERT = ""
    HEADER, CONTACTS = readFile(FILENAME)
    if request.form:
        FIRST_NAME = (request.form.get("first_name"))
        LAST_NAME = (request.form.get("last-Name"))
        EMAIL = (request.form.get("email"))
        if checkContent(EMAIL):
            createContact(FIRST_NAME, LAST_NAME, EMAIL)
            ALERT = "Contact has been successfully added."
        else:
            ALERT = "Contact email already exists"
    return render_template("index.html", alert=ALERT, contacts=CONTACTS)

### CSV
@app.route('/delete/<id>')
def deleteContactPage(id):
    deleteContact(id)
    return redirect('/')



def readFile(FILE_NAME):
    '''
    Opens our csv file and reads the contents to an array, If the File has not been created yet it does so
    :param FILE_NAME:
    :return: HEADER, DATA
    '''
    try:
        with open(FILENAME, newline="") as FILE:
            READER = csv.reader(FILE)
            HEADER = next(READER)
            DATA = []
            for ROW in READER:
                DATA.append(ROW)
        return HEADER, DATA
    except:
        with open(FILENAME, "w", newline="") as FILE:
            WRITER = csv.writer(FILE)
            HEADER = ["First Name", "Last Name", "Email"]
            WRITER.writerow(HEADER)
        return readFile(FILENAME)

def createContact(FIRST_NAME, LAST_NAME, EMAIL):
    """
    creates an contact and adds it to the csv file using the data recieved
    :param FIRST_NAME: str
    :param Last_Name: str
    :param Email: str
    :return: none
    """
    CONTACT = [FIRST_NAME, LAST_NAME, EMAIL]
    with open(FILENAME, "a", newline="") as FILE:
        WRITER = csv.writer(FILE)
        WRITER.writerow(CONTACT)
    pass

def checkContent(EMAIL):
    """
    Checks if email already exists
    :param EMAIL: str
    :return: bool
    """
    with open(FILENAME, newline="") as FILE:
        READER = csv.reader(FILE)
        for ROW in READER:
            if ROW[2] == EMAIL:
                return False
        return True

def deleteContact(EMAIL):
    """
    Deltes a Contact
    :param EMAIL:
    :return:
    """
    NEW_DATA = []
    with open(FILENAME, newline="") as FILE:
        READER = csv.reader(FILE)
        for ROW in READER:
            if ROW[2] != EMAIL:
                NEW_DATA.append(ROW)
    with open(FILENAME, "w", newline="") as FILE:
        WRITER = csv.writer(FILE)
        WRITER.writerows(NEW_DATA)




### maincode

app.run()


