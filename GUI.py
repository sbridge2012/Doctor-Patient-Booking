import sys
import sqlite3

from PyQt5 import QtCore, QtWidgets , QtGui
from PyQt5.QtCore import QDateTime, QDate
from PyQt5.QtWidgets import QMainWindow, QAction, QDateTimeEdit , QDateEdit
from datetime import datetime , date , timedelta

import main

class patientViewAppts(QMainWindow): # qmain window displaying a patients booked appointment
    def __init__(self):
        super().__init__() # call parent class ( QMainWindow) constructor

        self.resize(600,800) # set window size
        self.p_appts = QtWidgets.QListWidget(self) # add list widget to window
        self.p_appts.setGeometry(QtCore.QRect(100, 50, 400, 500)) # set size of list widget

        self.apptString = "" # initialze appt string
        self.appts_list = [] # initialie appts list

        self.get_appts = main.getPatientAppts(Layout.logged_in_patientid) # call getPatientApps sql query from main file


        for a,b,c,d in self.get_appts: # loop through query results which are returned as a list of tuples
            self.appt_string = a + " " + b + " " + c + " " + d # build string consisting of variables fro loop
            self.appts_list.append(self.appt_string) # append string to list

        self.p_appts.addItems(self.appts_list)  # add list dat to qlist widget - this is outside of the loop as we only want to add one string to list
        self.p_appts.show() # show the widget on qMainwindow

class patient_book_appts(QMainWindow): # qmain window displaying available appointments for patients to book
    def __init__(self):
        super().__init__() # call parent class ( QMainWindow) constructor

        self.resize(600,800) # set window size
        self.submit = QtWidgets.QPushButton(self) # add button to window
        self.submit.setGeometry(QtCore.QRect(125, 550, 151, 31)) # set button size and location in window
        self.submit.setText("Book") #  add text to button
        self.submit.clicked.connect(self.submit_data) # when button is clicked this will trigger the submit_data method


        self.appts_start = QtWidgets.QLabel(self) # add label to window
        self.appts_start.setGeometry(QtCore.QRect(105,5,63,55)) # set label size and location in window
        self.appts_start.setText("Date/Time") # set label text

        self.appts_end = QtWidgets.QLabel(self)  # add label to window
        self.appts_end.setGeometry(QtCore.QRect(190, 5, 55, 55)) # set label size and location in window
        self.appts_end.setText("End time") # set label text

        self.appts_location = QtWidgets.QLabel(self) # add qlabel to window
        self.appts_location.setGeometry(QtCore.QRect(260, 5, 55, 55)) # set label size and location in window
        self.appts_location.setText("Location") # set label text

        self.appts_doc = QtWidgets.QLabel(self) # add qlabel to window
        self.appts_doc.setGeometry(QtCore.QRect(325, 5, 55, 55)) # set label size and location in window
        self.appts_doc.setText("Doctor") # set label text

        self.qlist = QtWidgets.QListWidget(self) # add qlist to window
        self.qlist.setGeometry(QtCore.QRect(100,50,400,500)) # set qlist size and location in window

        self.get_appts = main.queryAppts() # call get qppts query from main file

        self.list=[] # initialize list
        self.appts_string=""  # initialize string
        for i,j,k,l,m,n,o  in self.get_appts: # loop through query results

            self.appts_string = str(i) + " " + j + " "  + k[11:] + " " + l + " " + " " + m + " " + " " + str(n) + " " + str(o) # append loop variables to string
            list.append(self.appts_string) # append string to list
            print("token is", Layout.logged_in_token)
            print("user id is", Layout.logged_in_patientid)
            self.qlist.addItems(list) # add list items to qlist widget
            self.qlist.show() # show qlist
            self.qlist.itemDoubleClicked.connect(self.press_check) # if qlist item double clicked the presscheck method is called


    def press_check(self): # this method will return the index of the item that has been clicked as a string

        self.get_appt = self.qlist.currentItem().text()[:2] # get the first two characers of the string

        print(type(self.get_appt))

        return int(self.get_appt) # convert the self.get_appt to an int and return it



    def submit_data(self):  # method to submit data to database
         print("patient apps numb", len(main.get_patient_appts(Layout.logged_in_patientid))) # get length of query result for testing purposes
         if len(main.get_patient_appts(Layout.logged_in_PatientID)) == 0:  # if length is 0 insert call update appointments method query from main file
             main.update_appts(Layout.logged_in_patientid, patient_book_appts.press_check(self))
         else:
             self.error_msg = QtWidgets.QMessageBox(self, text="You can only have one appointment booked") # if length of appointment query is not 0 show message saying you can only have one appointment booked at a time
             self.error_msg.show()

class admin_bk_appts(QMainWindow): # inherit class QMainWindow
    def __init__(self):
        super().__init__()  # call parent class constructor

        self.gapLength = 0 # initialize gap length and set to 0

        self.resize(400,600) # set size of window
        self.submit = QtWidgets.QPushButton(self) # add submit button
        self.submit.setGeometry(QtCore.QRect(125, 500, 151, 31)) # set size and location of button
        self.submit.setText("Submit details") # set button text
        self.lunch_start = None # initialize lunch_start variable and set it to non type
        self.lunch_end = None # initialize lunch_end variable and set it to non type

        self.s_time = QtWidgets.QLabel(self) # add start time label to window
        self.s_time.setGeometry(QtCore.QRect(45, 155, 125, 15)) # set size and location of start time label
        self.s_time.setText('Start time') # add text to start time label

        self.start_time = QDateTimeEdit(self, calendarPopup = True) # add qdatetime edit ti window and seet the calender pop to true , this will allow users to select a date from a calender pop up widget
        self.start_time.setGeometry(QtCore.QRect(175, 145, 150, 30)) # set size and location of start time widget
        self.start_time.dateTimeChanged.connect(self.check_time) # if the user changes the date/time then check_time method is triggered
        self.submit.clicked.connect(self.submit_details) # if submit button is clicked this will trigger the submit_details method
        print(" datetime is", self.start_time.dateTime()) # print the default date time for testing purposes

        #self.eTime = QtWidgets.QLabel(self)
        #self.eTime.setGeometry(QtCore.QRect(45, 190, 125, 30))
        #self.eTime.setText('End Time')

        #self.end_time = QDateTimeEdit(self, calendarPopup=True, date=QDate.currentDate())
        #self.end_time.setGeometry(QtCore.QRect(175, 190, 150, 30))
        #self.et = self.end_time.dateTime()
       # self.et_string = self.et.toString(self.end_time.displayFormat())
        #self.et = self.end_time.dateTimeChanged.connect(lambda: checkTime())

        self.location = QtWidgets.QTextEdit(self) # add location text field
        self.location.setGeometry(QtCore.QRect(175, 230, 125, 30)) # set size and location of text field

        self.location_label = QtWidgets.QLabel(self) # add location label to window
        self.location_label.setGeometry(QtCore.QRect(45, 230, 125, 30)) # set size and location of location label
        self.location_label.setText('Location') # set location label text

        self.choose_doctor = QtWidgets.QComboBox(self) # add combo box (drop down list ) for choosing doctors
        self.choose_doctor.setGeometry(QtCore.QRect(175, 270, 135, 40)) # set size and location of combo box
        self.choose_doctor.currentIndexChanged.connect(self.get_index) # when doctor is chosen get the trigger get_index method which will return index of chosen doctor

        self.appt_length = QtWidgets.QComboBox(self) # add another combo box so that appointment lengths can be set
        self.appt_length.setGeometry(QtCore.QRect(175, 310, 135, 40)) # set size and location of combo box
        self.apptLengthOptions = ["15","30"] # add options for appointment lengths to a list - these will later be converted to int
        self.appt_length.addItems(self.apptLengthOptions) # add list to combo box


        self.get_doc = main.queryDoc() # call sql query method from main file and set it to variable
        print(self.get_doc) # print the variable for testing purposes
        self.doc_list = [] # initialize list
        self.doc_string = "" # initialize doc string
        for i , n in self.getDoc: # loop through results of sql query
            doc_string = str(i) + " " + n # add loop variables to string
            self.doc_list.append(doc_string) # add doc_string to list
        self.choose_doctor.addItems(self.doc_list) # add doc_string to list

        self.choose_doctor_label = QtWidgets.QLabel(self) # add choose doctor label to window
        self.choose_doctor_label.setGeometry(QtCore.QRect(45, 270, 125, 30)) # set size and location of choose doctor label
        self.choose_doctor_label.setText('Choose doctor') # set text for choose doctor label


    def check_time(self): # this method is triggered when the subtmit button is clicked

        self.time_changed = self.start_time.dateTime() # get the date and time from start time field
        self.time_value = QDateTime(self.time_changed) # convert time_changed to QDateTime object
        print(self.time_value) # print the time_value object for testing purposes
        print(type(self.time_value) , "type of time value is <<<") # print the type of time_value for testing purposes
        self.py_start_date = self.time_value.toPyDateTime() # convert time value to python date time object
        self.start_date_string = self.py_start_date.strftime(("%Y-%m-%d, %H:%M:%S")) # convert python date time object to string representation of python datetime object and set format style
        self.convert_date_string = datetime.strptime(self.start_date_string, "%Y-%m-%d, %H:%M:%S") #  convert start_date_string representation of  python datetime object back into string representation of python date time object for testing purposes
        self.end_time = self.py_start_date + timedelta(seconds=1800) # set end time to start date + 30 minutes (1800 seconds) using method from time delta clss
        self.sEndTime = self.end_time.strftime(("%Y-%m-%d, %H:%M:%S")) # convert end time python datetime object to string representation of date time object


    def get_index(self): #

        self.doc_id = self.choose_doctor.currentText()[:2] # get the text value from the chosen doctor and get the first two characters



    def submit_details(self):  # this method is triggered when the submit button is pressed

        self.get_doc_appts = main.get_doctor_appts(self.doc_id, self.start_date_string[:10]) # call method with sql query
        if len(self.get_doc_appts) == 0: # if length of query is 0 call method with sql query and enter detials
            main.insertApptData(self.start_date_string, self.sEndTime, self.location.toPlainText(), "", self.doc_id, "")

        elif len(self.get_doc_appts) >= 1: # if length of query is greater to or equal to 1 call the get_end_dates method

            self.get_end_dates()

    def get_end_dates(self):
        self.appts = [] # initialize list
        self.start_dates = [] # initialize list
        print(self.doc_id, "doc id", self.start_date_string) # print doc id and start date string for testing purposes
        self.get_doc_appts_end_time = main.get_doctor_appts_etime(self.doc_id, self.start_date_string[:10]) # call method with sql query from main file and slice the string as we only want the date part of the string
        print(self.get_doc_appts_end_time, "end time") # print the variable with the query for testing purposes

        for ID , s_date ,  e_date in self.get_doc_appts_end_time: # set up for loop to get id, start date and end date
            print("loop entered") # for testing purposes to see if loop is executing
            self.end_date_string_to_date_obj = datetime.strptime(e_date, "%Y-%m-%d, %H:%M:%S") # get the end date from the loop and convert it to python datetime object
            self.appts.append(self.end_date_string_to_date_obj) # add datetime objec to list
            self.start_date_string_to_date_obj = datetime.strptime(s_date, "%Y-%m-%d, %H:%M:%S") # get the start dte from the loop and convert it to python datetime object
            self.start_dates.append(self.start_date_string_to_date_obj) # python datetime object to list

        self.last_appt = self.appts.pop() # get the last end date from the list
        self.last_appt_start = self.start_dates.pop() # get the last start date from the list

        print(self.last_appt) # print last appt end time for testing purposes
        print(self.last_appt_start) # prnt last start time for testing purposes

        if len(self.get_doc_appts) <= 16:  # if length of query is less than 16 go to next if statement , if not go to the else statement
            print("check passed")

            if self.check_time_gap( self.last_appt_start) >= 35 : # call check time ga method with argumebt of last appointment start time, if a value greater to or equal to 35 is returned go to the next if , if not go to the else statement

                if self.py_start_date > self.four_hour_check()[0] and self.py_start_date  < self.four_hour_check()[1]: #  call four hour check method and check if the first element of the returned tuple  is greater than the start date time that is entered by the user and check that it is less than the second element of the returned tuple
                    self.error_msg = QtWidgets.QMessageBox(self, text="Appointment can not be booked in Doctors lunch hour") #  call message box method and set text  to say that appointments can not be set between doctors lunch hour
                    self.error_msg.show() # show error message as pop up

                else: # if user has chosen a datetime that is not between the doctors lunch then enter call the method with sql  query from the main file
                    main.insertApptData(self.start_date_string, self.sEndTime, self.location.toPlainText(), "", self.doc_id,
                                        "")

            else: # if user has selected time that is less than 35 mins after the start time of the latest start time in the database show user a message to say there must be at least 5 minutes between appointments ( appointments are 30 mins plus 5 at least 5 mins before the next appt)
                self.error_msg = QtWidgets.QMessageBox(self, text="There must be at least 5 minutes between appointments") # call message box widget and set text
                self.error_msg.show()  #  show error message widget

        else: # if length of query is greater than 16
            self.error_msg = QtWidgets.QMessageBox(self, text="Doctors can only have 16 appointments per day") #  call message box widget and set text
            self.erro_msg.show()  #  show error message widget


    def check_time_gap(self , appt): # method that checks gap (difference) between two times

        self.time_difference = self.py_start_date - appt # calculate difference between user selected datetime and appt( this is is the last appointment start time)
        self.gapLength = (self.time_difference.total_seconds() / 60) # call total seconds method on the caclulated result from above and divide by 60 get number of minutes
        print(self.gapLength, "gap length is")  # print result from above for testing purposes
        return self.gapLength # return gaplength

    def four_hour_check(self): #  this method calculates when the doctors lunch hour should be (4 hours after first appointment of day)

        self.s_appts = [] #  initialize list
        self.get_doc_appts_start_time = main.get_doctor_appts_s_time(self.doc_id, self.start_date_string[:10]) #  call function with sql query from main file

        for id, start in self.get_doc_appts_start_time: #  set up for loop to go through returned list of tuples from sql query

            self.start_date_string_to_date_obj = datetime.strptime(start, "%Y-%m-%d, %H:%M:%S") #  turn each date string into a python date time object
            self.s_appts.append( self.start_date_string_to_date_obj) #  append python date time object to s_appts list
            print(self.appts, "apps date") #  print s appts list for testing purposes

        self.first_appt = self.s_appts[0] #  get the first element of the list
        print(self.first_appt) #  print first element for testing purposes

        self.time_check = self.py_start_date - self.first_appt #  take away the user selected datetime from the s_appts first element and set it to variable
        self.s_gap_length = (self.time_check.total_seconds() / 60) #  call time deltas total seconds method on the above time_check variable and then divide by 60 to get the total seconds
        print(self.s_gap_length, "gap length is") #  print the above variable for testing purposes

        self.lunch_start = self.first_appt + timedelta(seconds=14400) #  calculate 4 hours from first appointment time and set it to variable
        self.lunch_end = self.lunch_start + timedelta(seconds=3600) #  calculate one hour from above variable and set it to variable
        print(self.lunch_end, " this is lunch end time <<<") #  print lunch end variable for testing purposes
        print(self.lunch_start, "lunch start") #  print lunch start variable for testing purposes

        return self.lunch_start , self.lunch_end # return lunch start and lunch end variables as a tuple

class LoggedIn(QMainWindow): #  class that shows window when user has logged in
    def __init__(self):
        super().__init__() #  call parent class constructor

        self.resize(300,200) # set size of window
        self.setWindowTitle( "Patient/Doctor app  - Logged in") #  set title

        self.book_appointments = QtWidgets.QPushButton(self) # add book appointments button to window
        self.book_appointments.setGeometry(QtCore.QRect(70, 50, 150, 30)) # set size and location of button
        self.book_appointments.setText("Book appointment") #  set button text

        self.view_appointments = QtWidgets.QPushButton(self) #  add view appointments button
        self.view_appointments.setGeometry(QtCore.QRect(70, 100, 150, 30)) # set size and location of view appointments button
        self.view_appointments.setText("View appointments") #  set text for view appointments button

        self.book_appointments.clicked.connect(self.p_book_appts) # if book appoints button is called the pbookappts method will be triggered
        self.view_appointments.clicked.connect(self.view_appts) # if view appoints button is called the view_appts method will be triggered

    def p_book_appts(self): #  method to create instance of screen for patient to book appts class
        self.p = patient_book_appts() # make instance of class
        self.p.show()  # show class

    def view_appts(self): #  method to create instance of screen for patient to view booked  appsts class
        self.v = patientViewAppts() # make instane of class
        self.v.show() #  show class

        #self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(self)

        # def retranslateUi(self):
        # _translate = QtCore.QCoreApplication.translate

class Layout(QMainWindow): #  class to show initial screen of app
    logged_in_token = 0 # class variable to hold logged in status ( 1 or 0)
    logged_in_patientid = 0 # class variable to hold patient id

    def __init__(self): # class constructor
        super().__init__() # call parent class constructor

        self.setObjectName("Patient/Doctor booking app") # set title of window
        self.resize(750, 1000) # set size of window

        self.menu = self.menuBar() # add menu to window
        self.file_menu = self.menu.addMenu('Admin area') # set name of menu
        self.enter_appointments = QAction('Enter appointments', self) # add option to drop down menu
        self.file_menu.addAction(self.enter_appointments) # add Qaction to file menu widget

        self.enter_appointments.triggered.connect(self.admin_appts) # when enter appointments option clicked call admin_appts method

        self.pr_button = QtWidgets.QRadioButton(self) # add patient radio radio button to screen
        self.pr_button.setGeometry(QtCore.QRect(400, 65, 65, 28)) # set size and location of patient radio button
        self.pr_button.setText("Patient") # set text for patient radio button

        self.dr_button = QtWidgets.QRadioButton(self) # add doctor radio button to window
        self.dr_button.setGeometry(QtCore.QRect(20, 65, 65, 28)) # set size and location of doctor radio button
        self.dr_button.setText("Doctor") # set text for doctor radio button

        self.submit = QtWidgets.QPushButton(self) # add submit button to window
        self.submit.setGeometry(QtCore.QRect(220,550,151,31)) # set size and location of submit button
        self.submit.setText("Submit details") # set submit button text

        self.login = QtWidgets.QLabel(self) #  add log in label to window
        self.login.setGeometry(QtCore.QRect(260, 650, 151, 31)) # set size and location of login label
        self.login.setText("Patient Login") # set login label texte

        self.d_name_label = QtWidgets.QLabel(self) # add doctor name label to window
        self.d_name_label.setGeometry(QtCore.QRect(2, 150, 125, 15)) # set size and location of doctor name label
        self.d_name_label.setText('Doctor name') # set text for doctor name label

        self.doc_name = QtWidgets.QTextEdit(self) # add doctor name text edit
        self.doc_name.setGeometry(QtCore.QRect(145, 150, 125, 30)) # set size and location of doctor text edit

        self.d_dob = QDateEdit(self) # add doctor dob date edit field
        self.d_dob.setGeometry(QtCore.QRect(145, 190, 150, 30)) # set size and location of doctor dob date edit field
        self.d_dob.editingFinished.connect(self.get_d_age) # if date value in field changed get trigger the get_d_age method

        self.d_dob_label = QtWidgets.QLabel(self) # add doctor date of birth label
        self.d_dob_label.setGeometry(QtCore.QRect(2, 190, 125, 30)) # set size and location of doctor date of birth label
        self.d_dob_label.setText('Doctor date of birth') # set text for doctor date of birth label

        self.d_address = QtWidgets.QTextEdit(self) # add doctor address field
        self.d_address.setGeometry(QtCore.QRect(145, 230, 125, 30)) # set size and location of doctor address text edit

        self.d_address_label = QtWidgets.QLabel(self) # add doctor
        self.d_address_label.setGeometry(QtCore.QRect(2, 230, 125, 30)) # set size and location of doctor address label
        self.d_address_label.setText('Doctor address') # set text for doctor address label

        self.d_specialization = QtWidgets.QTextEdit(self) # add doctor specialization text edit
        self.d_specialization.setGeometry(QtCore.QRect(145, 270, 125, 30)) # set size and location of doctor specialization field

        self.specializaiton_label = QtWidgets.QLabel(self) # add doctor specialization label
        self.specializaiton_label.setGeometry(QtCore.QRect(1, 270, 128, 30)) # set size and location of doctor specialization label
        self.specializaiton_label.setText('Doctor specialization') #  set text for doctor specialization label

        self.p_name_label= QtWidgets.QLabel(self)  # add patient name label
        self.p_name_label.setGeometry(QtCore.QRect(350, 150, 125, 15)) # set size and location of patient name label
        self.p_name_label.setText('Name') # set patient name text

        self.p_name = QtWidgets.QTextEdit(self) # add patient name text field
        self.p_name.setGeometry(QtCore.QRect(450, 150, 125, 30)) # set size and location of patient text field

        self.p_dob = QDateEdit(self)  # add qdate edit for patient dob
        self.p_dob.setGeometry(QtCore.QRect(450, 190, 150, 30)) # set size and location of qdate edit
        self.p_dob.editingFinished.connect(self.get_p_age) # if date is changed call get_p_age method

        self.p_dob_label = QtWidgets.QLabel(self)  # add patient dob label
        self.p_dob_label.setGeometry(QtCore.QRect(355, 190, 125, 30)) # set size and location of patient dob label
        self.p_dob_label.setText('Date of birth') # set text

        self.p_address_label = QtWidgets.QLabel(self)  # add patient email label
        self.p_address_label.setGeometry(QtCore.QRect(355, 230, 125, 30))  # set size and location of patient email label
        self.p_address_label.setText('Address')  # set text

        self.p_address = QtWidgets.QTextEdit(self)  # add qdate edit for patient dob
        self.p_address.setGeometry(QtCore.QRect(450, 230, 125, 30))  # set size and location of qdate edit

        self.p_email_label = QtWidgets.QLabel(self)  # add patient email label
        self.p_email_label.setGeometry(QtCore.QRect(355, 270, 125, 30))  # set size and location of patient email label
        self.p_email_label.setText('Email')  # set text

        self.p_email = QtWidgets.QTextEdit(self)  # add qdate edit for patient dob
        self.p_email.setGeometry(QtCore.QRect(450, 270, 125, 30))  # set size and location of qdate edit


        self.p_gender = QtWidgets.QTextEdit(self) # add patient gender text edit
        self.p_gender.setGeometry(QtCore.QRect(450, 310, 125, 30)) # set size and location of patient gender text edit

        self.p_gender_label = QtWidgets.QLabel(self) # add patient gender label
        self.p_gender_label.setGeometry(QtCore.QRect(350, 310, 125, 30)) # set label size and location
        self.p_gender_label.setText('Gender') # set label text

        self.p_medical_issue = QtWidgets.QTextEdit(self) # add patient medical issue field
        self.p_medical_issue.setGeometry(QtCore.QRect(450, 350, 125, 30)) # set size and location of patient medical issue widget

        self.p_medical_issue_label = QtWidgets.QLabel(self) # add patient medical issue label
        self.p_medical_issue_label.setGeometry(QtCore.QRect(310, 350, 130, 30)) # set size and location of patient medical issue
        self.p_medical_issue_label.setText('Medical issue') # set text for patient medical issue

        self.p_ethnicity = QtWidgets.QTextEdit(self) # add patient ethnicity widget
        self.p_ethnicity.setGeometry(QtCore.QRect(450, 390, 125, 30)) # set size and location of patient ethnicity widget

        self.p_ethnicity_label = QtWidgets.QLabel(self) # add patient ethnicty label
        self.p_ethnicity_label.setGeometry(QtCore.QRect(345, 390, 125, 30)) # set size and location of patient ethnicity label
        self.p_ethnicity_label.setText('Ethnicity') # set patient ethnicity label text

        self.p_uname = QtWidgets.QTextEdit(self) # add patient user name text edit
        self.p_uname.setGeometry(QtCore.QRect(450, 430, 125, 30)) # set size and location of patient username text dit

        self.p_uname_label = QtWidgets.QLabel(self) # add patient user name label
        self.p_uname_label.setGeometry(QtCore.QRect(335, 430, 125, 30)) # set size and location of patient user name label
        self.p_uname_label.setText('Username') # set patient user name label text

        self.p_password = QtWidgets.QLineEdit(self) # add patient password text field
        self.p_password.setGeometry(QtCore.QRect(450, 470, 125, 30)) # set size and location of line edit
        self.p_password.setEchoMode(2) # add asteriks to disguise password

        self.p_password_label = QtWidgets.QLabel(self) # add patient password label to window
        self.p_password_label.setGeometry(QtCore.QRect(335, 470, 125, 30)) # set size and location of patient password label
        self.p_password_label.setText('Password') # set text for patient password label

        # this section of code disables the patient and doctor fields upon initial running of the application
        self.p_name.setDisabled(True)
        self.p_medical_issue.setDisabled(True)
        self.p_dob.setDisabled(True)
        self.p_email.setDisabled(True)
        self.p_ethnicity.setDisabled(True)
        self.p_gender.setDisabled(True)
        self.p_uname.setDisabled(True)
        self.p_password.setDisabled(True)
        self.d_dob.setDisabled(True)
        self.d_address.setDisabled(True)
        self.d_specialization.setDisabled((True))
        self.doc_name.setDisabled(True)
       #
    # login area

        self.u_name_login = QtWidgets.QTextEdit(self) # add username text field
        self.u_name_login.setGeometry(QtCore.QRect(110, 750, 125, 30)) # set size and location of user name login field

        self.u_name_loginl_label = QtWidgets.QLabel(self) # add user name login babel
        self.u_name_loginl_label.setGeometry(QtCore.QRect(110, 720, 125, 30)) # set size and location of user name login field
        self.u_name_loginl_label.setText('Patient Username') # set text or user name login label

        # self.passwordlogin = QtWidgets.QTextEdit(self)

        #self.passwordlogin.setGeometry(QtCore.QRect(400, 750, 125, 30))
        #self.qline = QtWidgets.QLineEdit.setEchoMode()
        #self.passwordlogin.s
        self.pword = QtWidgets.QLineEdit(self) # add password line edit
        self.pword.setGeometry(QtCore.QRect(400, 750, 125, 30)) # set size and location of password line edit
        self.pword.setEchoMode(2) # disguise password with asteriks

        self.password_login_label = QtWidgets.QLabel(self) # add password login label
        self.password_login_label.setGeometry(QtCore.QRect(400, 720, 125, 30)) # set password login label size and location
        self.password_login_label.setText('Patient Password') # set password login label text

        self.submit_login = QtWidgets.QPushButton(self) # add submit login details button
        self.submit_login.setGeometry(QtCore.QRect(220, 800, 151, 31)) # set size and location of submmit login details button
        self.submit_login.setText("Login")

        self.submit_logout = QtWidgets.QPushButton(self) # add logout button
        self.submit_logout.setGeometry(QtCore.QRect(375, 800, 151, 31)) # set size and location of log out utton
        self.submit_logout.setText("Logout") # set text for logout button

        #self.retranslateUi()
    # QtCore.QMetaObject.connectSlotsByName(self)

        self.dr_button.clicked.connect(self.dr_button_clicked) # if dr radio button clicked then trigger rubbonclicked method
        self.pr_button.clicked.connect(self.p_button_clicked) # if patient radio button clicked then trigger pubbonclicked method
        self.submit.clicked.connect(self.submit_details)  # if submit details button pressed then trigger submit details method
        self.submit_login.clicked.connect(self.logged_in_screen) # if submit login button pressed then trigger logged in screen method
        self.submit_logout.clicked.connect(self.logout) # if logout button clicked then trigger logout method

        self.time = QtWidgets.QLabel(self) # add time label
        self.time.setGeometry(QtCore.QRect(220, 5, 200, 25)) # set size and location of time label
        timer = QtCore.QTimer(self) # add QTimer object

        # date_time = current_time.strftime("%m/%d/%Y, %H:%M:%S")
        timer.timeout.connect(lambda: self.time.setText(QDateTime.currentDateTime().toString())) # add QDateTime object to QTimer object
        #timer.timeout.connect(lambda: self.time.setText(current_time.strftime("%m/%d/%Y, %H:%M:%S")))

        # update the timer every second
        timer.start(1000)

        self.show() # call qMainWindow's show method, without this nothing will show


    def get_p_age(self): # calculate patient age

        self.get_p_age = self.p_dob.date() # get date value from patient dob field
        self.py_date_age = self.get_p_age.toPyDate() # convert qdate to python date object
        print("py date is ", self.py_date_age) # print python date object for testing purposes
        self.date_now = date.today().year # get the current year
        self.p_calc_age = (self.date_now - self.py_date_age.year) # calculate age by taking away the current year from the year entered by the user


    def test(self): # used for testing
        print("trigger test")

        # def retranslateUi(self):
        #   translate = QtCore.QCoreApplication.translate
        # self.setWindowTitle(_translate("", "Patient/Doctor booking app"))
        # self.pushButton.setText(_translate("", "Click"))

    # this section of code disables the patient fields if the doctor radio button is clicked
    def dr_button_clicked(self):
        self.doc_name.setDisabled(False)
        self.d_dob.setDisabled(False)
        self.d_address.setDisabled(False)
        self.d_specialization.setDisabled(False)

        if self.dr_button.isChecked():
            self.p_name.setDisabled(True)
            self.p_medical_issue.setDisabled(True)
            self.p_dob.setDisabled(True)
            self.p_ethnicity.setDisabled(True)
            self.p_gender.setDisabled(True)
            self.p_uname.setDisabled(True)
            self.p_password.setDisabled(True)

    # this section of code disables the doctor fields if the patient radio button is clicked
    def p_button_clicked(self):
        self.p_name.setDisabled(False)
        self.p_dob.setDisabled((False))
        self.p_medical_issue.setDisabled((False))
        self.p_ethnicity.setDisabled((False))
        self.p_gender.setDisabled(False)
        self.p_uname.setDisabled(False)
        self.p_password.setDisabled(False)
        self.p_email.setDisabled(False)
        if self.pr_button.isChecked():
            self.d_dob.setDisabled(True)
            self.d_address.setDisabled(True)
            self.d_specialization.setDisabled((True))
            self.doc_name.setDisabled(True)


    def submit_details(self):
        if self.dr_button.isChecked(): # if dr radio button is clicked
            self.name = self.doc_name.toPlainText() # get text value from text field
            self.age = self.d_calcAge # get age value from age field
            self.address = self.d_address.toPlainText() # get address value from address text field
            self.specialization = self.d_specialization.toPlainText() # get specialization text value from specialization fieldff
        #main.insert_user_data(dname_text,dage_int,daddress_text,dspecialization_text)

            self.d1 = main.Doctor(self.name,self.age,self.address,self.specialization) # create Doctor object from "main" file
            main.insert_user_data(self.d1.name,self.d1.age,self.d1.address,self.d1.specialization) # call function with sql query from main and insert the doctor object attributes

        elif self.pr_button.isChecked(): # if patient radio button checked do the same as what above except for patient

            self.p_name1 = self.p_name.toPlainText()
            self.p_dob = self.p_calc_age
            self.p_email = self.p_email.toPlainText()
            self.pa_gender1 = self.p_gender.toPlainText()
            self.p_medical_issue = self.p_medical_issue.toPlainText()
            self.p_address1 = self.p_address.toPlainText()
            self.pethncity1 = self.p_ethnicity.toPlainText()
            self.p_uname = self.p_uname.toPlainText()
            self.ppword = self.p_password.text()



            self.patientinput= main.Patient(self.p_name1, self.p_dob, self.pa_gender1,self.p_medical_issue,self.pethncity1 , self.p_uname, self.ppword , self.p_email,self.p_address1)
            main.insert_puser_data(self.patientinput.name, self.patientinput.age, self.patientinput.gender, self.patientinput.medical_issue,self.patientinput.ethnicity ,self.patientinput.username,self.patientinput.pword,self.patientinput.email, self.patientinput.address,0)

            self.data_sub = QtWidgets.QMessageBox(text = "Thank you data submitted")
            self.data_sub.show()

    def logged_in_screen(self): # this class sets the qmain window for when the user clicks log in
        print("usner name is ", self.u_name_login.toPlainText()) # print the logged in users user name for testing purposes
        self.get_login = main.loginCheck(self.u_name_login.toPlainText()) # call function with sql query that will retreive the users user name and password
        print(self.getLogin) # print the results of above query for testing purposes

        for u,p, r in self.get_login: # set up for loop to go retrieve users log in details - thinking about this it doesn't really need a loop as there should only be one row of data returned in a tuple inside a list
            print(u,p ,r) # print loop variables for testing purposes
            if self.pword.text() == p: # if text in password matches password from loop execute the below
                Layout.logged_in_token = 1 # set the logged in token to 1
                Layout.logged_in_patientid = r # set logged in patient id to id from the loop
                main.updateLoggedinFlag(r) # update the logged in flag in the patient table to 1 to show that user is logged in
                self.l = LoggedIn() # make instance of LoggedIn class
                self.l.show() # call the show method to display the logged in class
            else: # if password is wrong execute the following

                fail = QtWidgets.QMessageBox(self,text = "Login fail") # pop up message box telling user their password is wrong
                fail.show() # show the message box

    def logout(self): # function to log out the user
        main.updateLoggedinFlagLogOut(self.logged_in_patientid) # update the logged in field in the user base to 0
        self.logged_in_patientid = 0 # set logged in patient id to 0
        self.logged_in_token = 0 # set the logged in token to 0
        print(self.logged_in_patientid) # print patient id for testing purposes
        print(self.logged_in_token) # print logged in token for testing purposes


    def admin_appts(self): # this method is called when the menu button "admin area" is pressed
        self.aa = admin_bk_appts() # make instance of admin_bk_appts class
        self.aa.show() # call show method on admin_bk_appts

    def get_d_age(self): # this method is triggered when the date in the qdate edit field is changed
        self.get_d_age = self.d_age.date() # get the date from the qdate edit
        self.py_drate_age = self.get_d_age.toPyDate() # convert the date to a python date object
        print("py date is ", self.py_drate_age) # print python date for testing
        self.date_now = date.today().year # get the current year

        self.d_calc_age = (self.date_now - self.py_drate_age.year) # calculate birth year from current year to get age
        print("this is the age", self.d_calcAge) # print age variable for testing purposes

    def closeEvent(self, QCloseEvent): # this method will trigger when the qmain window from the layout class is closed
        print("window closed without logging out")
        main.updateLoggedinFlagLogOut(self.logged_in_patientid) # update the logged in status field in the database to show user has closed the window and logged out
        self.logged_in_patientid = 0 # set logged in patient id to 0
        self.logged_in_token = 0 # set logged in token to 0


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    l = Layout() # make instance of layout class as this will be the class that is launched upon running the programme
    sys.exit(app.exec_())



