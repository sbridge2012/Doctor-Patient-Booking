import sqlite3

con=sqlite3.connect("DocPatDB")
cur=con.cursor()


def create_tables():

    cur.execute(""" CREATE TABLE Doctor (
                ID INTEGER PRIMARY KEY NOT  NULL ,
                NAME VARCHAR(255) NOT NULL,
                AGE INT NOT NULL,
                ADDRESS TEXT NOT NULL,
                SPECIALIZATION TEXT NOT NULL
            ); """)

    cur.execute("""CREATE TABLE Patient
       (ID INTEGER PRIMARY KEY NOT NULL ,   
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       GENDER       TEXT NOT NULL ,
       MEDICAL_ISSUE TEXT NOT NULL ,
       ETHNICITY TEXT NOT NULL
       );""")



def drop_table():
    cur.execute(""" DROP TABLE Appointments""")
    con.close()
def create_appointments():
    cur.execute("""CREATE TABLE Appointments
               (ID INTEGER PRIMARY KEY NOT NULL ,   
               START_TIME   TEXT    NOT NULL,
               END_TIME TEXT NOT NULL,
               LOCATION TEXT     NOT NULL,
               PATIENT_PROBLEM TEXT,
               DOCTOR_ID INTEGER,
               PATIENT_ID INTEGER ,
               FOREIGN KEY (DOCTOR_ID) REFERENCES Doctor (ID),
               FOREIGN KEY (PATIENT_ID) REFERENCES Patient (ID)
               );""")
    con.close()

def alter_table():
    cur.execute("""ALTER TABLE Patient
    ADD
    LOGGED_IN_FLAG
    INT NOT NULL""")
    con.close()

def appttest(Start, End, Location, Problem, ):
        cur.execute(
            "INSERT INTO Appointments (START_TIME, END_TIME,LOCATION,PATIENT_PROBLEM,DOCTOR_ID,PATIENT_ID) VALUES(?,?,?,?)",
            (Start, End, Location, Problem, ))
        con.commit()

def drop_column():
   cur.execute("""ALTER
    TABLE
    Patient
    DROP
    COLUMN
    LOGGED_IN_FLAG """)

def delete_rows():
    cur.execute(""" DELETE FROM Appointments """)
    con.commit()



#alter_table()
#create_tables()
#create_appointments()
#drop_table()
#appttest("10am","1020am","Baber","Gout",3)
#drop_column()
delete_rows()
