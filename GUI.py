import sys
import time

import Email
import sqlite3
import re
import smtplib

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QDateTime, QEvent, QObject, QDate, QModelIndex, QAbstractTableModel ,QAbstractItemModel ,
from PyQt5.QtWidgets import QMainWindow, QAction, QDateTimeEdit , QDateEdit , QTableWidget ,QTableWidgetItem , QActionGroup ,QAbstractButton, QRadioButton,QButtonGroup , QCheckBox , QAbstractItemView , QLayout , QFormLayout , QMessageBox , QStyledItemDelegate
from datetime import datetime , date , timedelta




import main



class firstScreen(QMainWindow): #  class that shows window when user has logged in
    def __init__(self):
        super().__init__() #  call parent class constructor

        self.resize(300,200) # set size of window
        self.setWindowTitle( "Welcome to Patient/Doctor app ") #  set title

        self.register= QtWidgets.QPushButton(self) # add book appointments button to window
        self.register.setGeometry(QtCore.QRect(80, 40, 150, 30)) # set size and location of button
        self.register.setText("Register") #  set button text

        self.login = QtWidgets.QPushButton(self) #  add view appointments button
        self.login.setGeometry(QtCore.QRect(80, 100, 150, 30)) # set size and location of view appointments button
        self.login.setText("Login") #  set text for view appointments button

        self.login1= QtWidgets.QPushButton(self)  # add view appointments button
        self.login1.setGeometry(QtCore.QRect(80, 160, 150, 30))  # set size and location of view appointments button
        self.login1.setText("Admin login")  # set text for view appointments button
        self.login1.clicked.connect(self.admin_appts)


        self.register.clicked.connect(self.regscreeninit) # open loginscreen
        self.login.clicked.connect(self.loginscreeninit)  # open register screen

    def admin_appts(self):  # this method is called when the menu button "admin area" is pressed

        #self.al= adminLoginScreen()
       # self.al.show()
        self.aa = QMainWindow(self)
        self.aa.resize(300, 200)  # set size of window
        self.aa.setWindowTitle("Admin Login ")  # set title

        self.aa.p_label = QtWidgets.QLabel(self.aa)  # add password text edit to screen
        self.aa.p_label.setGeometry(QtCore.QRect(70, 30, 150, 30))  # set size and location of button
        self.aa.p_label.setText("Enter Admin Password")

        self.aa.p_word = QtWidgets.QLineEdit(self.aa)  # add password text edit to screen
        self.aa.p_word.setGeometry(QtCore.QRect(70, 100, 150, 30))  # set size and location of button
        self.aa.p_word.setEchoMode(2)

        self.aa.Login = QtWidgets.QPushButton(self.aa)  # add view appointments button
        self.aa.Login.setGeometry(QtCore.QRect(70, 160, 150, 30))  # set size and location of view appointments button
        self.aa.Login.setText("Admin Login")  # set text for view appointments buttonlo
        self.aa.show()

        self.aa.Login.clicked.connect(self.check_password)

    def check_password(self):

        print(self.aa.p_word.text())

        if self.aa.p_word.text() == "Admin123*":

            self.show_admin = AdminLoggedIn()
            self.show_admin.show()
        else:
            qm = QtWidgets.QMessageBox(self)
            qm.setText("Password wrong")
            qm.show()



        #self.aa = admin_bk_appts()  # make instance of admin_bk_appts class
        #self.aa.show()  # call show method on admin_bk_appts

    def loginscreeninit(self):
        self.lg = loginScreen()
        self.lg.show()


    def regscreeninit(self):
        self.close()
        self.rs = Layout()
        self.rs.show()


class adminLoginScreen(QtWidgets.QWidget): #  class that shows window when user has logged in

    def __init__(self):
        super().__init__() #  call parent class constructor


        self.resize(300,200) # set size of window
        self.setWindowTitle( "Admin Login ") #  set title

        self.p_label = QtWidgets.QLabel(self)  # add password text edit to screen
        self.p_label.setGeometry(QtCore.QRect(70, 30, 150, 30))  # set size and location of button
        self.p_label.setText("Enter Admin Password")



        self.p_word = QtWidgets.QLineEdit(self)  # add password text edit to screen
        self.p_word.setGeometry(QtCore.QRect(70, 100, 150, 30))  # set size and location of button
        self.p_word.setEchoMode(2)


        self.Login = QtWidgets.QPushButton(self) #  add view appointments button
        self.Login.setGeometry(QtCore.QRect(70, 160, 150, 30)) # set size and location of view appointments button
        self.Login.setText("A Login") #  set text for view appointments buttonlo

        self.Login.clicked.connect(self.check_password)

    def check_password(self):
        print(self.p_word.text())

        if self.p_word.text()=="Admin123*":

            self.show_admin =  admin_bk_appts()
            self.show_admin.show()
        else:
            qm = QtWidgets.QMessageBox(self)
            qm.setText("Password wrong")
            qm.show()






class loginScreen(QMainWindow): #  class that shows window when user has logged in
    logged_in_patientid = 0
    def __init__(self):
        super().__init__() #  call parent class constructor


        self.resize(300,200) # set size of window
        self.setWindowTitle( "Login ") #  set title





        self.u_name= QtWidgets.QTextEdit(self) # add usern name text edit box
        self.u_name.setGeometry(QtCore.QRect(70,30, 150, 30)) # set size and location of usernme text edit field
        self.u_name.setText("Enter Username")

        self.p_word = QtWidgets.QLineEdit(self)  # add password text edit to screen
        self.p_word.setGeometry(QtCore.QRect(70, 100, 150, 30))  # set size and location of button
        self.p_word.setEchoMode(2)
        self.p_word.setText("Enter Password")


        self.Login = QtWidgets.QPushButton(self) #  add view appointments button
        self.Login.setGeometry(QtCore.QRect(70, 160, 150, 30)) # set size and location of view appointments button
        self.Login.setText("Login") #  set text for view appointments buttonlo
        self.Login.clicked.connect(self.logged_in_check)

    def logged_in_check(self):  # this class sets the qmain window for when the user clicks log in
        print("user name is ",self.u_name.toPlainText())  # print the logged in users user name for testing purposes
        self.get_login = main.loginCheck(self.u_name.toPlainText())  # call function with sql query that will retreive the users user name and password
        print(self.get_login)  # print the results of above query for testing purposes
        if len(self.get_login) == 0:
            fail = QtWidgets.QMessageBox(self,
                                             text="Login fail")  # pop up message box telling user their  username / password is wrong
            fail.show()  # show the message box

        else:

            for u, p, r in self.get_login:  # set up for loop to go retrieve users log in details - thinking about this it doesn't really need a loop as there should only be one row of data returned in a tuple inside a list
                print(u, p, r, "loop variables")  # print loop variables for testing purposes
                print(self.get_login, " self login")
                if self.p_word.text() == p:  # if text in password matches password from loop execute the below
                    Layout.logged_in_token = 1  # set the logged in token to 1
             # set logged in patient id to id from the loop
                    print("login success!")
                    loginScreen.logged_in_patientid = r

                    main.updateLoggedinFlag(
                            r)  # update the logged in flag in the patient table to 1 to show that user is logged in
                    self.l = LoggedIn()  # make instance of LoggedIn class
                    self.l.show()  # call the show method to display the logged in class
                elif self.pword.text() != p:  # if password is wrong execute the following

                    fail = QtWidgets.QMessageBox(self,
                                                     text="Login fail")  # pop up message box telling user their password is wrong
                    fail.show()  # show the message box
                elif len(self.login) == 0:
                    fail.show()
                    loginScreen.logged_in_patientid = r
            print("patient id global var is ", self.logged_in_patientid)




class TableModel(QAbstractTableModel):
    def __init__(self,data):
        super().__init__() # call parent class ( QAbstractTableModel) constructor
        self.data = data

        #self.headers = [''] * 5 # create list to contain header values
        #self.st = ''

        #self.setHeaderData(0,QtCore.Qt.Horizontal,"Start Date and Time")
        #self.setHeaderData(1, QtCore.Qt.Horizontal, "End Date and Time")
        #self.setHeaderData(2, QtCore.Qt.Horizontal, "Location")
        #self.setHeaderData(3, QtCore.Qt.Horizontal, "Doctor")
        #self.setHeaderData(4, QtCore.Qt.Horizontal, "Patient")

    def rowCount(self, parent=QModelIndex, *args, **kwargs):

        return len(self.data)

    def columnCount(self, parent=QModelIndex, *args, **kwargs):
         return len(self.data[0])

    def data(self, QModelIndex, role= QtCore.Qt.DisplayRole):


        if role == QtCore.Qt.DisplayRole: # if role is string
            try:
                print(QModelIndex.parent(), 'has parent')
                return  self.data[QModelIndex.row()][QModelIndex.column()]  # return the data at each required index ( this has no relation to the underyling list that is in the model)


            except IndexError:
                print("error has occured")

    def removeRows(self, p_int, p_int_1, parent=QModelIndex, *args, **kwargs):

        self.beginRemoveRows(QModelIndex(),p_int,p_int_1)
        del(self.data[p_int])
        self.endRemoveRows()

        return True

    def headerData(self, p_int, Qt_Orientation, role=QtCore.Qt.DisplayRole):

        if Qt_Orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:  # if orientation is horizontal and DisplayRole is string
            try:
                #return self.headers[p_int]

                # return 'cheese'

                print("error has occured")
                if p_int == 0:
                    return "Start Date and Time"
                if p_int == 1:
                    return 'End Date and Time'
                if p_int == 2:
                    return 'Location'
                if p_int == 3:
                    return 'Doctor'
                if p_int == 4:
                    return"Patient"
            except:
                IndexError

    #def setHeaderData(self, p_int, Qt_Orientation, Value, role=QtCore.Qt.DisplayRole):

        #if Qt_Orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole: # if header orientation is horizontal and the role is text
            #try:
                #self.headers[p_int] = Value # set each list index (HorizontalHeaders) to Value
                #except IndexError:
    #    print("error has occured")




class patientViewAppts(QMainWindow): # qmain window displaying a patients booked appointment
    def __init__(self):
        super().__init__() # call parent class ( QMainWindow) constructor

        self.resize(600,400) # set window size
        #self.p_appts = QtWidgets.QListWidget(self) # add list widget to window
        #self.p_appts.setGeometry(QtCore.QRect(100, 50, 400, 500)) # set size of list widget
        self.qtable = QtWidgets.QTableView(self)
        self.qtable.setGeometry(QtCore.QRect(50, 50, 500, 250))


        self.qtable.show()

        self.apptString = "" # initialze appt string
        self.appts_list = [] # initialie appts list
        self.qtabrow= 0
        print(loginScreen.logged_in_patientid , "patient ID")
        self.view_appts = main.get_patient_appts(loginScreen.logged_in_patientid) # call getPatientApps sql query from main file
        if len(self.view_appts) == 0:
            self.no_appts = QMessageBox(self)
            self.no_appts.setText("You do not have any booked appointments")
            self.no_appts.show()
        else:

            self.view_appts_data_model = TableModel(self.view_appts)
            self.qtable.setModel(self.view_appts_data_model)
            self.submit = QtWidgets.QPushButton(self)
            self.submit.setText("Email me my appointment")
            self.submit.setGeometry(QtCore.QRect(220,325,200,65))
            self.get_email = main.get_patient_email(loginScreen.logged_in_patientid)
            self.submit.clicked.connect(self.send_email)


    def send_email(self):
        self.appt_string =""
        for start, end , location ,doctor in self.view_appts:
            self.appt_string += start +" " + end + " "+ location + " " + doctor

        print(self.appt_string)
        for email in self.get_email:
            self.patient_email = email
            print("get emaail" , self.patient_email[0])
            self.send_appts(self.patient_email[0] , self.appt_string)


        #self.p_appts.addItems(self.appts_list)  # add list dat to qlist widget - this is outside of the loop as we only want to add one string to list
        #self.p_appts.show() # show the widget on qMainwindow

    def send_appts(self, email_address, appointments):

        email = 'your email here'
        password = 'your password here'
        smpt_object = smtplib.SMTP('smtp.gmail.com', 587)
        smpt_object.ehlo()
        smpt_object.starttls()
        smpt_object.login(email, password)
        from_address = email
        p_email = email_address

        subject = "Your appointments"
        msg = " Dear Patient, please find your appointment listed below"  +'\n' + appointments
        email_message = 'Subject: {}\n\n{}'.format(subject, msg)

        try:

            smpt_object.sendmail(from_address, p_email, email_message)
            time = True

        except:
            fail = QMessageBox(self)
            fail.setText("Email failed to send")
            fail.show()

        else:
            success =  QMessageBox(self)
            success.setText("Email sent")
            success.show()






class patient_book_appts(QtWidgets.QWidget): # qmain window displaying available appointments for patients to book
    def __init__(self):
        super().__init__() # call parent class ( QMainWindow) constructor

        self.resize(825,800) # set window size
        self.get_appts = main.queryAppts()
        self.list=[] # initialize list
        self.appts_string=""  # initialize string
        self.date_picker = QtWidgets.QDateTimeEdit(self,calendarPopup= True)
        self.date_picker.setGeometry((QtCore.QRect(325, 50, 150, 75)))
        self.date_picker.setDate(QDate.currentDate())

        self.table = QtWidgets.QTableView(self, 	)

        self.table.setGeometry(QtCore.QRect(50, 150, 700, 505))
        self.submit_btn = QtWidgets.QPushButton(self)
        self.submit_btn.setGeometry(QtCore.QRect(350,675,75,45))
        self.submit_btn.setText("Submit")
        self.table.setSelectionBehavior(1)
        self.table.setSelectionMode(1)

        self.appt_list = []
        self.appt_list_string = ''
        for start, end , location , doc , id in self.get_appts:
            self.appt_list_string += start + '' + end + '' + location + '' + doc
            print('the doc id is ', id)  # for debugging





            self.appt_list.append((start,end,location,doc))
        print(self.appt_list, 'appt list')




        self.tab_row = 0
        #print(self.get_appts)
        self.data_model = TableModel(self.appt_list)
        self.table.setModel(self.data_model)
        col = 0
        for col in range(len(self.get_appts[0])):
            self.table.setColumnWidth(col,175)
            col += 1

        self.table.setRowHeight(0,40)

        self.table.show()




        self.date_picker.dateChanged.connect(self.appt_date_filter)
            #self.table.cellClicked.connect(self.change)
        self.submit_btn.clicked.connect(self.submit_data)



    def appt_date_filter(self):
        self.date_filter = self.date_picker.date()
        self.filter_date_py = self.date_filter.toPyDate()
        self.filter_date_string = self.filter_date_py.strftime("%Y-%m-%d")
        #print(self.filter_date_string, "filter date")

        self.get_filt_apps = main.filter_appts(self.filter_date_string)


        self.submit_btn.clicked.connect(self.submitted)


        self.data_model = TableModel(self.get_filt_apps)
        self.table.setModel(self.data_model)
        self.table.setColumnWidth(0, 150)
        self.table.setRowHeight(0, 40)

        self.table.show()




    def press_check(self): # this method will return the index of the item that has been clicked as a string

        self.get_appt = self.qlist.currentItem().text()[:2] # get the first two characers of the string

        print(type(self.get_appt))

        return int(self.get_appt) # convert the self.get_appt to an int and return it



    def submit_data(self):  # method to submit data to database
        self.index = self.table.selectionModel().currentIndex()

        self.s_date = self.index.siblingAtColumn(0).data()
        self.location = self.index.siblingAtColumn(2).data()

        #self.get_date_filter = self.date_picker.date()
        #self.filter_appt_date_py = self.get_date_filter.toPyDate()
        #self.appt_filter_date_string = self.filter_appt_date_py.strftime("%Y-%m-%d")

        self.get_appt_id = main.get_selected_appts_id(self.s_date,self.location)

        for id  in self.get_appt_id:
            self.get_appt_id1 = id[0]

        print(self.get_appt_id1)


        print(loginScreen.logged_in_patientid, 'appt id')


        # print("patient apps numb", len(main.get_patient_appts(loginScreen.logged_in_patientid))) # get length of query result for testing purposes
        if len(main.get_patient_appts(loginScreen.logged_in_patientid)) == 0:  # if length is 0 insert call update appointments method query from main file
           main.update_appts(loginScreen.logged_in_patientid,self.get_appt_id1)
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

        self.add_appt_form= QFormLayout(self)
        self.add_appt_form.setGeometry(QtCore.QRect(10, 10, 75, 100))


        self.add_appt_form.insertRow(1, QtWidgets.QLabel("Name", self.add_doc), self.doc_name)
        self.add_doc_form.addRow(QtWidgets.QLabel("Date of birth", self.add_doc), self.doc_dob_cal)
        self.add_doc_form  .addRow(QtWidgets.QLabel("Specialization", self.add_doc), self.doc_specialization)
        self.doc_sbmt = QtWidgets.QPushButton("Submit", self.add_doc)
        self.doc_sbmt.setGeometry(QtCore.QRect(95, 140, 100, 35))
        # self.sbmt.clicked.connect(self.sbmtfunc)
        self.add_doc.show()

        self.location = QtWidgets.QTextEdit(self) # add location text field
        self.location.setGeometry(QtCore.QRect(175, 230, 125, 30)) # set size and location of text field

        self.location_label = QtWidgets.QLabel(self) # add location label to window
        self.location_label.setGeometry(QtCore.QRect(45, 230, 125, 30)) # set size and location of location label
        self.location_label.setText('Location') # set location label text

        self.choose_doctor = QtWidgets.QComboBox(self) # add combo box (drop down list ) for choosing doctors
        self.choose_doctor.setGeometry(QtCore.QRect(175, 270, 135, 40)) # set size and location of combo box
        self.choose_doctor.currentIndexChanged.connect(self.get_index) # when doctor is chosen get the trigger get_index method which will return index of chosen doctor

        self.appt_label = QtWidgets.QLabel(self)
        self.appt_label.setGeometry(QtCore.QRect(45, 315, 125, 30))
        self.appt_label.setText('Appointment length')

        self.appt_length = QtWidgets.QComboBox(self) # add another combo box so that appointment lengths can be set
        self.appt_length.setGeometry(QtCore.QRect(175, 310, 135, 40)) # set size and location of combo box
        self.apptLengthOptions = ["15","30"] # add options for appointment lengths to a list - these will later be converted to int
        self.appt_length.addItems(self.apptLengthOptions) # add list to combo box


        self.get_doc = main.queryDoc() # call sql query method from main file and set it to variable
        print(self.get_doc) # print the variable for testing purposes
        self.doc_list = [] # initialize list
        self.doc_string = "" # initialize doc string
        for i , n in self.get_doc: # loop through results of sql query
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
        self.get_time = self.time_value.time()
        self.hr = self.get_time.hour()
        self.min = self.get_time.minute()
        print(type(self.hr), 'type is')
        print(self.get_time, ' this is the get time')




    def get_index(self): #

        self.doc_id = self.choose_doctor.currentText()[:2] # get the text value from the chosen doctor and get the first two characters



    def submit_details(self):  # this method is triggered when the submit button is pressed
        current_year = QtCore.QDate.year(QtCore.QDate.currentDate())
        min_time = QtCore.QTime(8, 32)
        max_time = QtCore.QTime(16,30)

        if self.time_value.date() < QtCore.QDate.currentDate():
            self.appt_error = QMessageBox(self)
            self.appt_error.setText("You cannot  book appointments in the past")
            self.appt_error.show()

            if self.time_value.time() < min_time or  self.time_value.time() > max_time:
                self.appt_error = QMessageBox(self)
                self.appt_error.setText("You cannot  book appointments before 8am or after 4pm")
                self.appt_error.show()

        else:
            self.get_doc_appts = main.get_doctor_appts(self.doc_id, self.start_date_string[:10]) # call method with sql query

            if len(self.get_doc_appts) == 0: # if length of query is 0 call method with sql query and enter detials
                try:
                    main.insertApptData(self.start_date_string, self.sEndTime, self.location.toPlainText(), "", self.doc_id, "")
                    success = QMessageBox(self)
                    success.setText("Appointment entered succesfully")
                except:
                    fail = QMessageBox(self)
                    fail.setText("Appointment not entered")

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

         # show error message as pop up


        if self.check_duplicate_apps() >0:
            error_msg1 = QtWidgets.QMessageBox(self,
                                                    text="Duplicate appointments are not allowed")  # call message box method and set text  to say that appointments can not be set between doctors lunch hour
            error_msg1.show()




        elif len(self.get_doc_appts) <= 16:  # if length of query is less than 16 go to next if statement , if not go to the else statement
            print("check passed")

            if self.check_time_gap( self.last_appt_start) >= 35 : # call check time ga method with argumebt of last appointment start time, if a value greater to or equal to 35 is returned go to the next if , if not go to the else statement

                    if self.py_start_date > self.four_hour_check()[0]  and self.py_start_date  < self.four_hour_check()[1]: #  call four hour check method and check if the first element of the returned tuple  is greater than the start date time that is entered by the user and check that it is less than the second element of the returned tuple
                            self.error_msg = QtWidgets.QMessageBox(self, text="Appointment can not be booked in Doctors lunch hour") #  call message box method and set text  to say that appointments can not be set between doctors lunch hour
                            self.error_msg.show() # show error message as pop up

                    else: # if user has chosen a datetime that is not between the doctors lunch break then enter call the method with sql  query from the main file
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

    def check_duplicate_apps(self):

        print(self.start_date_string)

        self.check_doc_appts = main.get_selected_appts_id(self.start_date_string,self.location.toPlainText())
        print(self.check_doc_appts, ' check doca apppts fig')
        print(self.start_date_string,self.location.toPlainText(),' deets to pass')

        return len(self.check_doc_appts)



    # sql query to search appointment table for appts with that date , time and location , if query returns 0 then ok , if returns > 0 then deny


class AdminLoggedIn(QMainWindow): #  class that shows window when user has logged in
    def __init__(self):
        super().__init__() #  call parent class constructor

        self.resize(300,200) # set size of window
        self.setWindowTitle( "Admin area") #  set title

        self.add_doc = QtWidgets.QPushButton(self) # add book appointments button to window
        self.add_doc.setGeometry(QtCore.QRect(70, 50, 150, 30)) # set size and location of button
        self.add_doc.setText("Add Doctor") #  set button text

        self.add_doc_appointments = QtWidgets.QPushButton(self) #  add view appointments button
        self.add_doc_appointments.setGeometry(QtCore.QRect(70, 100, 150, 30)) # set size and location of view appointments button
        self.add_doc_appointments.setText("Add appointments") #  set text for view appointments button

        self.view_appts = QtWidgets.QPushButton(self)  # add view appointments button
        self.view_appts.setGeometry(
            QtCore.QRect(70, 150, 150, 30))  # set size and location of view appointments button
        self.view_appts.setText("View appointments")  # set text for view appointments button


        self.add_doc.clicked.connect(self.d_add_doc) # if book appoints button is called the pbookappts method will be triggered
        self.add_doc_appointments.clicked.connect(self.admin_book) # if view appoints button is called the view_appts method will be triggered
        self.view_appts.clicked.connect(self.admin_view_appts)

    def admin_book (self):
        self.admin_bk = admin_bk_appts()
        self.admin_bk.show()

    def d_add_doc(self):  # method to create instance of screen for patient to book appts class
        self.add_doc = QtWidgets.QWidget()
        self.add_doc.resize(250, 200)
        self.add_doc.setWindowTitle("Add doctor")
        self.add_doc_form = QFormLayout(self.add_doc)
        self.add_doc_form.setGeometry(QtCore.QRect(10, 10, 75, 100))
        self.doc_name = QtWidgets.QLineEdit()
        self.doc_dob_cal = QtWidgets.QDateEdit(calendarPopup = True)
        self.doc_specialization = QtWidgets.QLineEdit()

        self.add_doc_form.insertRow(1, QtWidgets.QLabel("Name", self.add_doc), self.doc_name)
        self.add_doc_form.addRow(QtWidgets.QLabel("Date of birth", self.add_doc), self.doc_dob_cal)
        self.add_doc_form.addRow(QtWidgets.QLabel("Specialization", self.add_doc), self.doc_specialization)
        self.doc_sbmt = QtWidgets.QPushButton("Submit", self.add_doc)
        self.doc_sbmt.setGeometry(QtCore.QRect(95, 140, 100, 35))
        # self.sbmt.clicked.connect(self.sbmtfunc)
        self.add_doc.show()





        self.doc_dob_cal.dateChanged.connect(self.get_doc_dob_date)

        self.doc_sbmt.clicked.connect(self.submit_doc)


    def get_doc_dob_date(self):
        self.doc_qdate = self.doc_dob_cal.date()
        self.doc_date_py = self.doc_qdate.toPyDate()
        self.doc_date_string =  self.doc_date_py.strftime("%Y-%m-%d")


        return self.doc_date_string


    def submit_doc(self):
        self.doc_name_widg = self.add_doc_form.itemAt(0, 1)  # prints house no
        self.doc_name_widget = self.doc_name_widg.widget()
        self.doc_name_widget_data = self.doc_name_widget.text()
        print(self.doc_name_widget_data, "doctor name")


        self.doc_dob = self.add_doc_form.itemAt(1, 1)  # prints house no
        self.doc_dob_widget = self.doc_dob.widget()
        self.doc_dob_widget_data = self.doc_dob_widget.text()
        print(self.doc_dob_widget_data, "date from form!")

        self.doc_spec = self.add_doc_form.itemAt(2, 1)  # prints house no
        self.doc_spec_widget = self.doc_spec.widget()
        self.doc_spec_widget_data = self.doc_spec_widget.text()
        print(self.doc_spec_widget_data, "doctor spec")


        self.doc_name_match = re.search("^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?$)", self.doc_name_widget_data)

        self.doc_spec_match = re.search("^[A-Za-z]{1,35}(?:\s+[A-Za-z]{0,35})*\s*$", self.doc_spec_widget_data)

        self.doc_error_list = []
        self.doc_msgbox = QMessageBox()

        if self.doc_name_match is not None:
            pass


        else:
            self.doc_error_list.append("Invalid doctor name")

        if self.doc_spec_match is not None:
            pass


        else:
            self.doc_error_list.append("Invalid specialization")

        if len(self.doc_error_list) == 0:
            main.insert_doc_data(self.doc_name_widget_data, self.get_doc_dob_date(), self.doc_spec_widget_data)
            self.doc_msgbox.setText("Doctor details succesfully entered")
            self.doc_msgbox.show()
            self.add_doc.close()

        else:
            self.doc_msgbox.setText('\n'.join(self.doc_error_list))
            self.doc_msgbox.show()


    def admin_view_appts(self): #  method to create instance of screen for patient to view booked  appsts class

        self.view_appts_table = QtWidgets.QWidget()

        self.view_appts_table.resize(825, 800)  # set window size
        self.get_all_appts = main.admin_view_appts()
        self.list = []  # initialize list
        self.appts_string = ""  # initialize string
        self.date_picker = QtWidgets.QDateTimeEdit(self, calendarPopup=True)
        self.date_picker.setGeometry((QtCore.QRect(325, 50, 150, 75)))
        self.date_picker.setDate(QDate.currentDate())

        self.table = QtWidgets.QTableView(self.view_appts_table, selectionBehavior=1)
        self.table.setGeometry(QtCore.QRect(50, 150, 700, 505))




        self.view_appt_list = []
        self.appt_list_string = ''
        for start, end, location, doc, p_name in self.get_all_appts:
            self.appt_list_string += start + '' + end + '' + location + '' + doc
            print('the doc id is ', id)  # for debugging

            self.view_appt_list.append((start, end, location, doc,p_name))
        print(self.view_appt_list, 'appt list')

        self.tab_row = 0
        # print(self.get_appts)
        self.appts_data_model = TableModel(self.view_appt_list)
        self.table.setModel(self.appts_data_model)
        col = 0
        for col in range(len(self.get_all_appts[0])):
            self.table.setColumnWidth(col, 175)
            col += 1

        self.table.setRowHeight(0, 40)





        self.delete_appt = QtWidgets.QPushButton(self.view_appts_table)
        self.delete_appt.setGeometry(QtCore.QRect(250, 700, 225, 75))
        self.delete_appt.setText("Delete appointment")
        self.delete_appt.show()


        self.view_appts_table.show()
        self.delete_appt.clicked.connect(self.delete_appointment)



    def delete_appointment(self):

        self.index = self.table.selectionModel().currentIndex()


        self.s_date = self.index.siblingAtColumn(0).data()
        self.e_date = self.index.siblingAtColumn(1).data()
        self.location = self.index.siblingAtColumn(2).data()

        print(self.s_date, self.e_date, self.location) # for testing

        self.get_appt_id =main.selected_admin_delete_appt_id(self.s_date,self.e_date,self.location) # call sql query to get appointment id

        for id  in self.get_appt_id:
            self.get_appt_id1 = id[0]

        main.admin_delete_appt(self.get_appt_id1) # call sql query to delete record in db
        self.appts_data_model.removeRow(self.table.currentIndex().row(),QModelIndex()) # currentIndex is a method from QAbstractItemView of type QModelIndex that returns the index of current item. The .row method then returns the row relating to the item













    def admin_appts(self):  # this method is called when the menu button "admin area" is pressed

        # self.al= adminLoginScreen()
        # self.al.show()
        self.aa = QMainWindow(self)
        self.aa.resize(300, 200)  # set size of window
        self.aa.setWindowTitle("Admin Login ")  # set title

        self.aa.p_label = QtWidgets.QLabel(self.aa)  # add password text edit to screen
        self.aa.p_label.setGeometry(QtCore.QRect(70, 30, 150, 30))  # set size and location of button
        self.aa.p_label.setText("Enter Admin Password")

        self.aa.p_word = QtWidgets.QLineEdit(self.aa)  # add password text edit to screen
        self.aa.p_word.setGeometry(QtCore.QRect(70, 100, 150, 30))  # set size and location of button
        self.aa.p_word.setEchoMode(2)

        self.aa.Login = QtWidgets.QPushButton(self.aa)  # add view appointments button
        self.aa.Login.setGeometry(QtCore.QRect(70, 160, 150, 30))  # set size and location of view appointments button
        self.aa.Login.setText("Admin Login")  # set text for view appointments buttonlo
        self.aa.show()





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
        self.v = patientViewAppts() # make instance of class
        self.v.show() #  show class



        #self.retranslateUi()
        #QtCore.QMetaObject.connectSlotsByName(self)

        # def retranslateUi(self):
        # _translate = QtCore.QCoreApplication.translate



class Layout(QtWidgets.QWidget): #  class to show initial screen of app

    logged_in_token = 0 # class variable to hold logged in status ( 1 or 0)


    def __init__(self): # class constructor
        super().__init__() # call parent class constructor otherwise there will be an error

        self.resize(400,450)



        self.setWindowTitle("Patient registration")
        self.patient_form = QFormLayout(self)
        self.patient_form.setFormAlignment(QtCore.Qt.AlignCenter)
        self.patient_form.setGeometry(QtCore.QRect(150, 150, 300, 300))
        self.first_name= QtWidgets.QLineEdit()
        self.surname = QtWidgets.QLineEdit()
        self.gender= QtWidgets.QComboBox()
        self.gender.addItem("Male")
        self.gender.addItem("Female")
        self.email = QtWidgets.QLineEdit()
        self.p_uname = QtWidgets.QLineEdit()
        self.p_password1 = QtWidgets.QLineEdit()




        self.dob= QtWidgets.QDateEdit(calendarPopup = True)

        self.enter_add = QtWidgets.QPushButton()
        self.enter_add.setText("Enter address")
        self.sbmt_details = QtWidgets.QPushButton(self)
        self.sbmt_details.setGeometry(QtCore.QRect(150,375,100,50))
        self.sbmt_details.setText("Submit data")
        self.sbmt_details.show()
        self.sbmt_details.setDisabled(True)


        self.patient_form.insertRow(1, QtWidgets.QLabel("First name", self), self.first_name)
        self.patient_form.addRow(QtWidgets.QLabel("Surname", self), self.surname)
        self.patient_form.addRow(QtWidgets.QLabel("Gender", self), self.gender)
        self.patient_form.addRow(QtWidgets.QLabel("Date of birth", self), self.dob)
        self.patient_form.addRow(QtWidgets.QLabel("Email", self), self.email)
        self.patient_form.addRow(QtWidgets.QLabel("Address", self), self.enter_add)
        self.patient_form.addRow(QtWidgets.QLabel("Username", self), self.p_uname)
        self.patient_form.addRow(QtWidgets.QLabel("Password", self), self.p_password1)

        self.dob.dateChanged.connect(self.get_p_age)

        self.enter_add.clicked.connect(self.enter_address)





        self.sbmt_details.clicked.connect(self.submit_details)

    # login area
        #self.retranslateUi()
    # QtCore.QMetaObject.connectSlotsByName(self)


        self.time = QtWidgets.QLabel(self) # add time label
        self.time.setGeometry(QtCore.QRect(160, 25, 120, 35)) # set size and location of time label
        timer = QtCore.QTimer(self) # add QTimer object



        # date_time = current_time.strftime("%m/%d/%Y, %H:%M:%S")
        timer.timeout.connect(self.add_time)
        #timer.timeout.connect(lambda: self.time.setText(QDateTime.currentDateTime().toString()))# add QDateTime object to QTimer object
        #timer.timeout.connect(lambda: self.time.setText(current_time.strftime("%m/%d/%Y, %H:%M:%S")))

        # update the timer every second
        timer.start(1000)

        self.show()



    def add_time(self):
        self.timeo = self.time.setText(QDateTime.currentDateTime().toString())


    def eventFilter(self, QObject, QEvent): # implement the eventFilter method which will handle the mouse click on the address tex edit
        if QObject == self.p_address.viewport():

            if QEvent.type() == QEvent.MouseButtonPress:
                Layout.enter_address(self)

            return True
        else:

            return self.eventFilter(QObject, QEvent)


    def get_p_age(self): # calculate patient age

        self.get_p_age = self.dob.date() # get date value from patient dob field
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

    def validate_data(self, password):

        if str(password)[0].istitle() and str(password)[-1] =="!":
            return True
            print("Password accepted")
        else:
            print("Password rejected")
            return False



    def logout(self): # function to log out the user
        main.updateLoggedinFlagLogOut(self.logged_in_patientid) # update the logged in field in the user base to 0
        self.logged_in_patientid = 0 # set logged in patient id to 0
        self.logged_in_token = 0 # set the logged in token to 0
        print(self.logged_in_patientid) # print patient id for testing purposes
        print(self.logged_in_token) # print logged in token for testing purposes





    def get_d_age(self): # this method is triggered when the date in the qdate edit field is changed
        self.get_d_age = self.d_age.date() # get the date from the qdate edit
        self.py_drate_age = self.get_d_age.toPyDate() # convert the date to a python date object
        print("py date is ", self.py_drate_age) # print python date for testing
        self.date_now = date.today().year # get the current year

        self.d_calc_age = (self.date_now - self.py_drate_age.year) # calculate birth year from current year to get age
        print("this is the age", self.d_calcAge) # print age variable for testing purposes

    def closeEvent(self, QCloseEvent): # this method will trigger when the qmain window from the layout class is closed
        print("window closed without logging out")
        #main.updateLoggedinFlagLogOut(self.logged_in_patientid) # update the logged in status field in the database to show user has closed the window and logged out
        self.logged_in_patientid = 0 # set logged in patient id to 0
        self.logged_in_token = 0 # set logged in token to 0




    def enter_address(self):
        self.address_window = QtWidgets.QWidget()
        self.address_window.resize(400,400)
        self.address_window.setWindowTitle("Address details")
        self.form_layout = QFormLayout(self.address_window)
        self.form_layout.setGeometry(QtCore.QRect(10, 10, 75, 100))
        self.house_no = QtWidgets.QLineEdit()
        self.street_name = QtWidgets.QLineEdit()
        self.town_name = QtWidgets.QLineEdit()
        self.county_name = QtWidgets.QLineEdit()
        self.post_code = QtWidgets.QLineEdit()
        self.form_layout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.form_layout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.form_layout.insertRow(1,QtWidgets.QLabel("House number",self.address_window),self.house_no)
        self.form_layout.addRow( QtWidgets.QLabel("Street name",self.address_window), self.street_name)
        self.form_layout.addRow(QtWidgets.QLabel("Town", self.address_window), self.town_name)
        self.form_layout.addRow(QtWidgets.QLabel("County", self.address_window), self.county_name)
        self.form_layout.addRow(QtWidgets.QLabel("Post code", self.address_window), self.post_code)
        self.sbmt_add = QtWidgets.QPushButton("Submit", self.address_window)
        self.sbmt_add.setGeometry(QtCore.QRect(175, 300, 100, 55))
        self.sbmt_add.clicked.connect(self.sbmtfunc)
        self.address_window.show()






    def sbmtfunc(self):
        self.add_list = []

        invalid_data = QMessageBox(self)

        self.hse_num = self.form_layout.itemAt(0, 1)  # prints house no
        self.hse_num_widget = self.hse_num.widget()
        self.hse_num_data = self.hse_num_widget.text()
        print("hse num is", self.hse_num_data)


        self.hse_num_match = re.search("^\d{1,3}$", self.hse_num_data)

        self.road_name = self.form_layout.itemAt(1, 1)  # prints house no
        self.road_name_widget = self.road_name.widget()
        self.road_name_data = self.road_name_widget.text()
        print("road name is ", self.road_name_data)

        self.road_match = re.search("^[A-Za-z]{1,35}(?:\s+[A-Za-z]{0,35})*\s*$", self.road_name_data)

        self.post_code = self.form_layout.itemAt(4, 1)  # prints house no
        self.post_widget = self.post_code.widget()
        self.post_code_data = self.post_widget.text()
        print("Post code is " , self.post_code_data)

        self.match = re.search("[A-Z]{2}[0-9]{1,2}[^\S\n\t][0-9]{1}[A-Z]{2}$", self.post_code_data)

        self.town_name = self.form_layout.itemAt(2, 1)  # prints house no
        self.town_name_widget = self.town_name.widget()
        self.town_name_data = self.town_name_widget.text()
        print("road name is ", self.town_name_data)

        self.town_match = re.search("^[A-Za-z]{1,20}$" ,  self.town_name_data)

        self.county_name = self.form_layout.itemAt(3, 1)  # prints house no
        self.county_name_widget = self.county_name.widget()
        self.county_name_data = self.county_name_widget.text()
        print("road name is ", self.county_name_data)

        self.county_match = re.search("^[A-Za-z]{1,10}$", self.county_name_data)








        error_string =[]

        if self.match is not None:
            print("Valid post code")
            print(self.match)
            self.add_list.append(self.post_code_data)



        else:
            print("Post code not valid")

            print(self.match)
            error_string.append("Invalid postcode")


        if self.hse_num_match is not None:
            self.add_list.append(self.hse_num_data)


        else:
            print("House number must be numbers only")


            error_string.append("House number must be numbers only")




        if self.road_match is not None:
            self.add_list.append(self.road_name_data)



        else:
            print("Road name numbers only")


            error_string.append("Road name invalid")




        if self.town_match is not None:
            self.add_list.append(self.town_name_data)



        else:
            print("Town name invalid")


            error_string.append("Town name invalid")




        if self.county_match is not None:
            self.add_list.append(self.county_name_data)



        else:
            print("County name invalid")

            error_string.append("County name invalid")


        print(self.add_list , 'this is the address list')

        if  len(error_string) ==0:
            self.address_window.close()
            address_success = QMessageBox(self)
            address_success.setText("Address data valid")
            address_success.show()
            self.enter_add.setDisabled(True)
            self.sbmt_details.setDisabled(False)


        else:



            invalid_data.setText('\n'.join(error_string))
            invalid_data.show()


    def submit_details(self):

        # if address details not greyed out show msg box






        self.p_name = self.patient_form.itemAt(0, 1)
        self.p_name_widget = self.p_name.widget()
        self.p_name_text = self.p_name_widget.text()
        print(self.p_name_text)

        self.p_surname = self.patient_form.itemAt(1, 1)
        self.p_surname_widget = self.p_surname.widget()
        self.p_surname_text = self.p_surname_widget.text()
        print(self.p_surname_text)

        self.p_gender = self.patient_form.itemAt(2, 1)
        self.p_gender_text = self.p_gender.widget()
        self.p_gender_text1 = self.p_gender_text.currentText()

        print(self.p_gender_text1)

        self.p_email = self.patient_form.itemAt(4, 1)
        self.p_email_widget = self.p_email.widget()
        self.p_email_text = self.p_email_widget.text()
        print(self.p_email_text)

        self.p_dob = self.patient_form.itemAt(3, 1)
        self.dob_widget = self.p_dob.widget()
        self.p_dob_text = self.dob_widget.text()
        print(self.p_dob_text, "this is date")

        self.p_user = self.patient_form.itemAt(6, 1)
        self.p_user_widget = self.p_user.widget()
        self.p_user_text = self.p_user_widget.text()
        print(self.p_user_text, "this is user")

        self.p_password2 = self.patient_form.itemAt(7, 1)
        self.p_password_widget = self.p_password2.widget()
        self.p_password_text = self.p_password_widget.text()
        print(self.p_password_text)


        self.add_line = " "
        for line in self.add_list:
            self.add_line += line


        self.preg_error_string = []
        self.preg_list = []
        self.patient_details = QMessageBox()


        self.fname_match = re.search("^[A-Za-z]{1,20}$", self.p_name_text)



        if self.fname_match is not None:
            print("Valid first name")
            print(self.fname_match)
            self.preg_list.append(self.p_name_text)


        else:
            print("First name not valid")
            print(self.fname_match)
            self.preg_error_string.append("Invalid first name")

        self.surname_match = re.search("^[A-Za-z]{1,20}$", self.p_surname_text)

        if self.surname_match is not None:
            print("Valid surname")
            print(self.surname_match)
            self.preg_list.append(self.p_surname_text)


        else:
            print("Surname not valid")
            print(self.surname_match_match)
            self.preg_error_string.append("Invalid surname")

        self.email_match = re.search("[a-z0-9\.-_]+[@][a-z0-9-_]+[\.][a-z0-9\.]{2,5}$", self.p_email_text)

        if self.email_match is not None:
            print("Valid email")
            print(self.email_match)
            self.preg_list.append(self.p_email_text)


        else:
            print("Email not valid")
            print(self.email_match)
            self.preg_error_string.append("Invalid email")

        self.uname_match = re.search("^\w{1,12}$", self.p_user_text)

        if self.uname_match is not None:
            print("Valid username")
            print(self.email_match)
            self.preg_list.append(self.p_user_text)


        else:
            print("Username not valid")
            print(self.uname_match)
            self.preg_error_string.append("Username must be up to 12 characters")

        self.pword_match = re.search("^[A-Z]{1}\w{1,5}[!]$", self.p_password_text)

        if self.pword_match is not None:
            print("Valid password")
            print(self.pword_match)
            self.preg_list.append(self.p_password_text)


        else:
            print("Password not valid")
            print(self.pword_match)
            self.preg_error_string.append("Password must start with a capital and end with a !")


        print(len(self.preg_error_string),' preg error string')

        self.p_user_check= main.check_user_name(self.p_user_text)

        if len(self.preg_error_string) == 0 :

            if len(self.p_user_check) == 0:





                main.insert_puser_data(self.p_name_text,self.p_calc_age, self.p_gender_text1,self.p_user_text,self.p_password_text,self.p_email_text, self.add_line,self.p_surname_text)  # call function with sql query from main and insert the doctor object attributes
                self.details_success = QMessageBox()
                self.details_success.setText("Details entered successfully")
                self.details_success.show()
                self.close()

            else:
                user_error = QMessageBox(self)
                user_error.setText("User name is taken, choose another!")
                user_error.show()


        else:
            self.patient_details.setText('\n'.join(self.preg_error_string))
            self.patient_details.show()




        #if self.add_data == "":
            #print("Empty string")

            #self.validate_box = QMessageBox(self)
            #self.validate_box.setText("Please complete all address fields")
            #self.validate_box.show()


            #else:
                #self.msg_box = QMessageBox(self)
                #self.msg_box.setText("Address data submitted")
                #self.msg_box.exec_()
        # self.address_window.close()
















        #self.form_layout.addRow( QtWidgets.QLabel("Road name",self.add_window), QtWidgets.QLineEdit(self.add_window))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) # enter main event loop
    #l = Layout() # make instance of layout class as this will be the class that is launched upon running the programme
    fs = firstScreen()
    fs.show()



    sys.exit(app.exec_())


