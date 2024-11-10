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


class Doctor: # create doctr class
    def __init__(self, name, age, address, specialization):
        self.name = name
        self.age=age
        self.address=address
        self.specialization=specialization

    def make_Doctor(name,age,address,specialization):
        new_Doctor = (name,age,address,specialization)


class Patient: # create Patient class
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
Benson = Patient("Benson Ripplesburg", 34, "Male", "Herpes", "White", "Benson1", "B123" , "benson@hotmail.com" , " 34 benson street ") # make instance of Patient class to test that it works


def insert_doc_data(Name, DOB, Specialization, SURNAME): # this is a method i used to test inserting data into the Doctor table

    try:

        cur.execute("INSERT INTO Doctor (NAME,SPECIALIZATION, DOB, SURNAME) VALUES(?,?,?,?)",
                    (Name, Specialization,DOB, SURNAME))
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")

def insert_user_data(Name,Age,Address,Specialization): # this method is called from the GUI file to input input from the user into the Doctor table

    try:

        cur.execute("INSERT INTO Doctor (NAME, AGE,ADDRESS,SPECIALIZATION) VALUES(?,?,?,?)", # ? acts as a placeholder and then Name , Age , Address and specialization from the next set of brackets are passed into the query
        (Name, Age, Address, Specialization))
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")


def insert_puser_data(Name,Age,Gender,User,Password, Email , Address, Surname ): # this method is called from the GUI file to input input from the user into the Patient table

    try:

        cur.execute("INSERT INTO Patient (NAME, AGE,GENDER, USER_NAME, PASSWORD,EMAIL_ADDRESS, ADDRESS ,Surname) VALUES(?,?,?,?,?, ?, ?,?)", # ? acts as a placeholder and then the variables  from the next set of brackets are passed into the query
        (Name, Age, Gender, User, Password,Email, Address, Surname ))
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")

def delete_row(): # used when i was testing SQLS delete function
    try:

        cur.execute("DELETE FROM Doctor WHERE ID=1")
        con.commit()

    except sqlite3.Error as error:
        print("error has occured")

def check_user_name(user_name): #

    try:
        cur.execute("SELECT USER_NAME FROM Patient   WHERE USER_NAME=? " , (user_name,))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print(" user name check - error has occured")

def query_db(): # used when i wanted to view all data in the doctor table
    try:

        cur.execute(" SELECT * FROM Doctor")
        rows=cur.fetchall() # call the fetchall method which will return the result set as tuples

        for row in rows: # loop through the tuples and print them
            print(row)

    except sqlite3.Error as error:
        print("error has occured")

def join(): # testing my sql skills with a join query

    try:
        cur.execute(" SELECT NAME FROM Doctor INNER JOIN Appointments ON Doctor.ID = APPOINTMENTS.DOCTOR_ID;")
        rows=cur.fetchall()
        for row in rows:
            print(row)

    except sqlite3.Error as error:
        print("error has occured")

def queryAppts(): # querying all of the data in the appointments table
    try:

        cur.execute("SELECT  a.START_TIME, a.END_TIME,a.LOCATION,d.Name , d.ID FROM Appointments a INNER JOIN Doctor d on A.DOCTOR_ID = d.ID WHERE a.PATIENT_ID = ''   ")
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")


def admin_view_appts(): # querying all of the data in the appointments table
    try:

        cur.execute("SELECT  a.START_TIME, a.END_TIME,a.LOCATION,d.Name , p.Name FROM Appointments a INNER JOIN Doctor d on A.DOCTOR_ID = d.ID  LEFT JOIN Patient p on P.ID =A.PATIENT_ID")
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")
def filter_appts(date): # querying all of the data in the appointments table
    try:

        cur.execute("SELECT  a.START_TIME, a.END_TIME,a.LOCATION,d.Name , d.ID FROM Appointments a INNER JOIN Doctor d on A.DOCTOR_ID = d.ID WHERE substr( START_TIME, 1, 10 ) =?",(date,))

        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")

def selected_admin_delete_appt_id(start, end , location, ): # querying all of the data in the appointments table
    try:

        cur.execute("SELECT ID FROM Appointments WHERE START_TIME  =? AND  END_TIME =? AND  LOCATION =? ", (start,end,location))

        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")


def admin_delete_appt(appt_id): # querying all of the data in the appointments table
    try:

        cur.execute("DELETE FROM APPOINTMENTS WHERE ID  =?",(appt_id,))

        rows = cur.fetchall()
        con.commit()
        return rows

    except sqlite3.Error as error:
        print("error has occured")




def queryDoc(): # query the id and name from the doctor table
    try:

        cur.execute(" SELECT ID , NAME FROM Doctor")
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")

def loginCheck(uname): # this function is called from the GUI file when a user trys to login - the users username is passed in and the username and password that match the username in the Patient table are returned

    try:

        cur.execute(" SELECT USER_NAME ,  PASSWORD , ID  FROM Patient WHERE USER_NAME =?" , (uname,))
        row = cur.fetchall()
        return row

    except sqlite3.Error as error:
        print("error has occured")


def insertApptData(Start, End, Location,Problem, Doc_ID, Patient_ID ): # this function is called from the GUI file to insert user data into the Appointments table

    try:
        cur.execute("INSERT INTO Appointments (START_TIME, END_TIME,LOCATION,PATIENT_PROBLEM,DOCTOR_ID,PATIENT_ID) VALUES(?,?,?,?,?,?)",
               (Start, End, Location,Problem, Doc_ID, Patient_ID))
        con.commit()

    except sqlite3.Error as error:
            print("error has occured")


def update_appts(pvalue,apptID): # this function is called from the GUI file to insert the patient id into the appointments table when they have booked an appointment
    try:

        cur.execute("UPDATE Appointments SET PATIENT_ID = ? WHERE ID=?" , (pvalue,apptID))
        con.commit()

    except sqlite3.Error as error:
            print("error has occured")

def get_patient_appts(pID): # this function is called from the GUI file to display a users booked appointment - (users can only have one appointment)

    try:

        cur.execute("SELECT a.START_TIME, a.END_TIME,a.LOCATION,d.Name FROM Appointments a INNER JOIN Doctor d on A.DOCTOR_ID = d.ID WHERE a.PATIENT_ID=?" , (pID,))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
            print("error has occured")

def get_patient_email(pID): # this function is called from the GUI file to display a users booked appointment - (users can only have one appointment)

    try:

        cur.execute("SELECT EMAIL_ADDRESS FROM Patient  WHERE ID=?" , (pID,))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
            print("error has occured")


def get_doctor_appts(Doc_ID,Start_Time): # this function is called from the GUI file to display a doctors appointments

    try:

        cur.execute("SELECT DOCTOR_ID, strftime('%Y-%m-%d',substr(START_TIME, 1, 10)) FROM Appointments  WHERE DOCTOR_ID=? AND strftime('%Y-%m-%d',substr(START_TIME, 1, 10))=? " , (Doc_ID,Start_Time)) # get doctor appointments where substring (Year Month Day) of Start_Time arguement match start date records in datbaase
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
            print("error has occured")

def get_doctor_appts_etime(Doc_ID,Start_Date): # called from the GUI file to retrieve the start date and end date  of doctors appointments where the Start_Date arguement matches start date records in the appointments table

    try:

        cur.execute("SELECT DOCTOR_ID, START_TIME , END_TIME FROM Appointments  WHERE DOCTOR_ID=? AND strftime('%Y-%m-%d',substr(START_TIME, 1, 10))=? " , (Doc_ID,Start_Date))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
            print("error has occured")

def get_doctor_appts_s_time(Doc_ID,Date): # called from the GUI file to retrieve the start date  of doctors appointments where the Start_Date arguement matches start date records in the appointments table

    try:
        cur.execute("SELECT DOCTOR_ID, START_TIME FROM Appointments  WHERE DOCTOR_ID=? AND strftime('%Y-%m-%d',substr(START_TIME, 1, 10))=? " , (Doc_ID,Date))
        rows = cur.fetchall()
        return rows

    except sqlite3.Error as error:
        print("error has occured")



def get_selected_appts_id(start,location): # called from the GUI file to retrieve the start date  of doctors appointments where the Start_Date arguement matches start date records in the appointments table

    try:
        cur.execute("SELECT a.ID FROM Appointments a  WHERE START_TIME=? AND  LOCATION=? " , (start,location))
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


def get_doctor_appts_wembley():

    try:

        cur.execute("SELECT DOCTOR_ID, START_TIME , END_TIME FROM Appointments  WHERE DOCTOR_ID=1 AND LOCATION='Bexley'")
        rows = cur.fetchall()
        print(rows)
        return rows

    except sqlite3.Error as error:
            print("error has occured")


#insert_data()
#alter_patient()
#delete_data()
#insert_data2(Frederick_R.name,Frederick_R.age,Frederick_R.address,Frederick_R.specialization)

#checkDocApptsGapTest('2007-05-04')

#get_doctor_appts_wembley()

def drop_col():
    cur.execute("UPDATE Patient SET EMAIL_ADDRESS ='sbridge11@googlemail.com' WHERE ID=2;")
    rows = cur.fetchall()
    con.commit()
    print(rows)
    print("Patients")

def delete_dat():

    cur.execute(" DELEtE FROM Appointments")
    print("duck")
    con.commit()
    con.close()

def filter_appts2(): # querying all of the data in the appointments table
    try:

        cur.execute("SELECT substr( START_TIME, 1, 10 ) FROM Appointments")

        rows = cur.fetchall()
        print(rows)
        return rows

    except sqlite3.Error as error:
        print("error has occured")







def add_col():
    cur.execute("ALTER TABLE Doctor ADD COLUMN SURNAME TEXT  ;")
    rows = cur.fetchall()
    con.commit()
    print(rows)
    print("Patients")









