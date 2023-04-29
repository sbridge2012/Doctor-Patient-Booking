# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import sqlite3

con=sqlite3.connect("DocPatDB")
cur=con.cursor()
new_doctor=''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


class Doctor:
    def __init__(self, name, age, address, specialization):
        self.name = name
        self.age=age
        self.address=address
        self.specialization=specialization

    def make_Doctor(name,age,address,specialization):
        new_Doctor = (name,age,address,specialization)


class Patient:
    def __init__(self, name, age,gender, medical_issue,ethncity,uname,pword, email ,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.medical_issue = medical_issue
        self.ethnicity = ethncity
        self.username = uname
        self.pword = pword
        self.email = email
        self.address = address


#Bobby_G = Doctor("Bobby Gindermack", 45, "123 Clarkesville, USA", "Diabetes")
#Frederick_R = Doctor("Frederick Ripplesburg", 34, "25 Coalmanstreet, USA", "Oncology")
Benson = Patient("Benson Ripplesburg", 34, "Male", "Herpes", "White", "Benson1", "B123" , "benson@hotmail.com" , " 34 benson street ")







def insert_data():

    try:

        cur.execute("INSERT INTO Doctor (NAME, AGE,ADDRESS,SPECIALIZATION) VALUES(?, ?,?,?)",
        (Bobby_G.name, Bobby_G.age,Bobby_G.address,Bobby_G.specialization))
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")

def insert_user_data(Name,Age,Address,Specialization):

    try:

        cur.execute("INSERT INTO Doctor (NAME, AGE,ADDRESS,SPECIALIZATION) VALUES(?,?,?,?)",
        (Name, Age, Address, Specialization))
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")


def insert_puser_data(Name,Age,Gender,Medical_Issue, Ethnicty , Username , Password, Email_Address, Address , Logged_in_Flag):

    try:

        cur.execute("INSERT INTO Patient (NAME, AGE,GENDER,MEDICAL_ISSUE,ETHNICITY, USER_NAME, PASSWORD,EMAIL_ADDRESS, Address , LOGGED_IN_FLAG) VALUES(?,?,?,?,?, ?, ?, ?,?, ?)",
        (Name, Age, Gender, Medical_Issue, Ethnicty, Username, Password,Email_Address, Address, Logged_in_Flag))
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")





def delete_row():

    try:

        cur.execute("DELETE FROM Doctor WHERE ID=1")
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")

def query_db():
    try:

        cur.execute(" SELECT * FROM Doctor")
        rows=cur.fetchall()


        for row in rows:
            print(row)

    except sqlite3.Error as error:
        print("error has occured")

def join():

    try:
        cur.execute(" SELECT NAME FROM Doctor INNER JOIN Appointments ON Doctor.ID = APPOINTMENTS.DOCTOR_ID;")
        rows=cur.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as error:
        print("error has occured")

def queryAppts():
    try:

        cur.execute(" SELECT * FROM Appointments")
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")


def queryDoc():
    try:

        cur.execute(" SELECT ID , NAME FROM Doctor")
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")

def loginCheck(uname):

    try:

        cur.execute(" SELECT USER_NAME ,  PASSWORD , ID  FROM Patient WHERE USER_NAME =?" , (uname,))
        row = cur.fetchall()
        return row

    except sqlite3.Error as error:
        print("error has occured")


def insertApptData(Start, End, Location,Problem, Doc_ID, Patient_ID ):

    try:
        cur.execute("INSERT INTO Appointments (START_TIME, END_TIME,LOCATION,PATIENT_PROBLEM,DOCTOR_ID,PATIENT_ID) VALUES(?,?,?,?,?,?)",
               (Start, End, Location,Problem, Doc_ID, Patient_ID))
        con.commit()

    except sqlite3.Error as error:
            print("error has occured")


def update_appts(pvalue,apptID):
    try:

        cur.execute("UPDATE Appointments SET PATIENT_ID = ? WHERE ID=?" , (pvalue,apptID))
        con.commit()

    except sqlite3.Error as error:
            print("error has occured")

def get_patient_appts(pID):

    try:

        cur.execute("SELECT a.START_TIME, a.END_TIME,a.LOCATION,d.Name FROM Appointments a INNER JOIN Doctor d on A.DOCTOR_ID = d.ID WHERE a.PATIENT_ID=?" , (pID,))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
            print("error has occured")


def get_doctor_appts(Doc_ID,Start_Time):

    try:

        cur.execute("SELECT DOCTOR_ID, strftime('%Y-%m-%d',substr(START_TIME, 1, 10)) FROM Appointments  WHERE DOCTOR_ID=? AND strftime('%Y-%m-%d',substr(START_TIME, 1, 10))=? " , (Doc_ID,Start_Time))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
            print("error has occured")

def get_doctor_appts_etime(Doc_ID,Date):

    try:

        cur.execute("SELECT DOCTOR_ID, START_TIME , END_TIME FROM Appointments  WHERE DOCTOR_ID=? AND strftime('%Y-%m-%d',substr(START_TIME, 1, 10))=? " , (Doc_ID,Date))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
            print("error has occured")

def get_doctor_appts_s_time(Doc_ID,Date):

    try:
        cur.execute("SELECT DOCTOR_ID, START_TIME FROM Appointments  WHERE DOCTOR_ID=? AND strftime('%Y-%m-%d',substr(START_TIME, 1, 10))=? " , (Doc_ID,Date))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")


def checkDocApptsGap(dID,):

    try:

        cur.execute("SELECT DOCTOR_ID, END_TIME  FROM Appointments    WHERE DOCTOR_ID=? " , (dID,))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")


def updateLoggedinFlag(pvalue):

    try:
        cur.execute("UPDATE Patient SET LOGGED_IN_FLAG = 1 WHERE ID=?" , (pvalue,))
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")

def updateLoggedinFlagLogOut(pvalue):

    try:
        cur.execute("UPDATE Patient SET LOGGED_IN_FLAG = 0 WHERE ID=?" , (pvalue,))
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")


def delete_data():

    try:

        cur.execute(" DELETE FROM Patient")
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")

def checkDocApptsGapTest(Start_Time):

    try:
        cur.execute("SELECT DOCTOR_ID, strftime('%Y-%m-%d',substr(START_TIME, 1, 10)) FROM Appointments  WHERE DOCTOR_ID=1 AND strftime('%Y-%m-%d',substr(START_TIME, 1, 10))=? " , (Start_Time,))
        rows = cur.fetchall()
        print(rows)

    except sqlite3.Error as error:
        print("error has occured")

def alter_patient():

    try:

        cur.execute(" ALTER TABLE Patient ADD ADDRESS TEXT NOT NULL ")
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")


#insert_data()
#alter_patient()
#delete_data()
#insert_data2(Frederick_R.name,Frederick_R.age,Frederick_R.address,Frederick_R.specialization)

checkDocApptsGapTest('2007-05-04')




