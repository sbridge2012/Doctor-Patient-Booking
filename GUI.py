import sys
import time


import Email
import sqlite3
import re
import smtplib

from PyQt5 import QtCore, QtWidgets ,QtGui
from PyQt5.QtCore import QDateTime, QEvent, QObject, QDate, QModelIndex, QAbstractTableModel ,QAbstractItemModel
from PyQt5.QtWidgets import QMainWindow, QAction, QDateTimeEdit, QDateEdit, QTableWidget, QTableWidgetItem, QDockWidget,QActionGroup, QAbstractButton, QRadioButton, QButtonGroup, QCheckBox, QAbstractItemView, QLayout, QFormLayout, \
    QMessageBox, QStyledItemDelegate, QTextEdit
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


class adminLoginScreen(QtWidgets.QWidget ): #  class that shows window when user has logged in

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
        self.u_name= QTextEdit(self)
        self.u_name.setGeometry(QtCore.QRect(70,30, 150, 30)) # set size and location of usernme text edit field
        self.u_name.setText("Enter Username")
        self.u_name.viewport().installEventFilter(self)


        self.p_word = QtWidgets.QLineEdit(self) #   add password text edit to screen
        self.p_word.setGeometry(QtCore.QRect(70, 100, 150, 30))  # set size and location of button
        self.p_word.setEchoMode(2)
        self.p_word.setText("Enter Password")
        self.p_word.installEventFilter(self)


        self.Login = QtWidgets.QPushButton(self) #  add view appointments button
        self.Login.setGeometry(QtCore.QRect(70, 160, 150, 30)) # set size and location of view appointments button
        self.Login.setText("Login") #  set text for view appointments buttonlo
        self.Login.clicked.connect(self.logged_in_check)


    def eventFilter(self, QObject, QEvent):

        if QObject == self.u_name.viewport():
            if QEvent.type() == QEvent.MouseButtonPress:
                self.u_name.setText("")
                return True
        if QObject == self.p_word:
            if QEvent.type() == QEvent.MouseButtonPress:
                self.p_word.setText("")
                return True
        return False





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
                print(self.p_word.text())
                if self.p_word.text() == p:  # if text in password matches password from loop execute the below
                    Layout.logged_in_token = 1  # set the logged in token to 1
             # set logged in patient id to id from the loop
                    print("login success!")
                    loginScreen.logged_in_patientid = r

                    main.updateLoggedinFlag(
                            r)  # update the logged in flag in the patient table to 1 to show that user is logged in
                    self.l = LoggedIn()  # make instance of LoggedIn class
                    self.l.show()  # call the show method to display the logged in class
                elif self.p_word.text() != p:  # if password is wrong execute the following

                    fail = QtWidgets.QMessageBox(self,
                                                     text="Password wrong")  # pop up message box telling user their password is wrong
                    fail.show()  # show the message box
                elif len(self.login) == 0:
                    fail.show()
                    loginScreen.logged_in_patientid = r
            print("patient id global var is ", self.logged_in_patientid)




class TableModel(QAbstractTableModel):
    def __init__(self,data):
        super().__init__() # call parent class ( QAbstractTableModel) constructor
        self.data = data



    def rowCount(self, parent=QModelIndex, *args, **kwargs):

        return len(self.data)

    def columnCount(self, parent=QModelIndex, *args, **kwargs):
         return len(self.data[0])

    def data(self, QModelIndex, role= QtCore.Qt.DisplayRole):


        if role == QtCore.Qt.DisplayRole: # if role is string
            try:

                return  self.data[QModelIndex.row()][QModelIndex.column()]  # return the data at each required index ( this has no relation to the underyling list that is in the model)


            except IndexError:
                print("error has occured")

    def removeRows(self, p_int, p_int_1, parent=QModelIndex, *args, **kwargs): # this method removes rows from model

        self.beginRemoveRows(parent,p_int, p_int_1) # begin remove row operation at specified row (p_int)
        del(self.data[p_int] )
        # delete data at specified row (p_int)
        self.endRemoveRows() # call method end row removal operation

        return True

    def headerData(self, p_int, Qt_Orientation, role=QtCore.Qt.DisplayRole): # set the header data for the model and in the view

        if Qt_Orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:  # if orientation is horizontal and DisplayRole is string
            try:

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
            self.no_appts = QMessageBox()
            self.no_appts.setText("You do not have any booked appointments")
            self.no_appts.show()
        else:

            self.view_appts_data_model = TableModel(self.view_appts)
            self.qtable.setModel(self.view_appts_data_model)
            self.submit = QtWidgets.QPushButton(self)
            self.submit.setText("Email me my appointment")
            self.submit.setGeometry(QtCore.QRect(220,325,200,65))
            self.get_email = main.get_patient_email(loginScreen.logged_in_patientid) # get patients email adddress from database
            self.submit.clicked.connect(self.send_email)

            #dock_widg = QDockWidget(self)
            #dock_widg.setAllowedAreas(QtCore.Qt.BottomDockWidgetArea)
            #dock_widg.setWidget(self.submit)

            #self.addDockWidget(QtCore.Qt.BottomDockWidgetArea,dock_widg)
            #self.setCentralWidget(self.qtable)


    def send_email(self):
        self.appt_string =""
        for start, end , location ,doctor in self.view_appts: # get patients appts from database
            self.appt_string += start +" " + end + " "+ location + " " + doctor # append appointment details to string

        print(self.appt_string)
        for email in self.get_email: #  loop through the sql query resykts
            self.patient_email = email
            print("get emaail" , self.patient_email[0])
            self.send_appts(self.patient_email[0] , self.appt_string) # call the send appointments email method


        #self.p_appts.addItems(self.appts_list)  # add list dat to qlist widget - this is outside of the loop as we only want to add one string to list
        #self.p_appts.show() # show the widget on qMainwindow

    def send_appts(self, email_address, appointments):

        email = 'your email here' # email to log into
        password = 'your password here' # password to log into email account
        smpt_object = smtplib.SMTP('smtp.gmail.com', 587)
        smpt_object.ehlo() # identify self to smpt serer
        smpt_object.starttls() # puts the SMTP connection in to security mode. All SMPT commands will be encrypred
        smpt_object.login(email, password) # login to email account
        from_address = email
        p_email = email_address
        print(p_email)

        subject = "Your appointments"
        msg = " Dear Patient, please find your appointment listed below"  +'\n' + appointments
        email_message = 'Subject: {}\n\n{}'.format(subject, msg)

        try:

            smpt_object.sendmail(from_address, p_email, email_message) # send email message
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
        self.date_picker = QtWidgets.QDateEdit(self,calendarPopup= True)
        self.date_picker.setGeometry((QtCore.QRect(325, 50, 150, 75)))
        self.date_picker.setDate(QDate.currentDate())


        self.table = QtWidgets.QTableView(self)

        self.table.setGeometry(QtCore.QRect(50, 150, 700, 505))
        self.submit_btn = QtWidgets.QPushButton(self)
        self.submit_btn.setGeometry(QtCore.QRect(350,675,75,45))
        self.submit_btn.setText("Submit")
        self.close_window = QtWidgets.QPushButton(self)
        self.close_window.setGeometry(QtCore.QRect(550, 675, 75, 45))
        self.close_window.setText("Close")
        self.submit_btn.setText("Submit")
        self.table.setSelectionBehavior(1)
        self.table.setSelectionMode(1)
        self.date_picker.dateChanged.connect(self.appt_date_filter)

        col = 0
        for col in range(len(self.get_appts[0])):
            self.table.setColumnWidth(col, 175)
        col += 1


        self.appt_list = []
        self.appt_list_string = ''
        for start, end , location , doc , id in self.get_appts:
            self.appt_list_string += start + '' + end + '' + location + '' + doc
            print('the doc id is ', id)  # for debugging

            self.appt_list.append((start,end,location,doc))
            print(self.appt_list, 'appt list')

        self.tab_row = 0

        self.data_model = TableModel(self.appt_list)
        self.table.setModel(self.data_model)


        self.table.setRowHeight(0,40)

        self.table.show()

        self.submit_btn.clicked.connect(self.submit_data)
        self.close_window.clicked.connect(self.close_win)





    def appt_date_filter(self):


        filt_error = QMessageBox(self)
        self.date_filter = self.date_picker.date()
        self.filter_date_py = self.date_filter.toPyDate()
        self.filter_date_string = self.filter_date_py.strftime("%Y-%m-%d")
        #print(self.filter_date_string, "filter date")

        self.get_filt_apps = main.filter_appts(self.filter_date_string)
        self.filt_appt_list =[]
        self.filt_appt_list_string = ''

        for start, end, location, doc, id in self.get_filt_apps:
            self.filt_appt_list_string += start + '' + end + '' + location + '' + doc

            self.filt_appt_list.append((start, end, location, doc))

        if len(self.filt_appt_list) == 0:



             filt_error.setText("No appointments on this day")
             filt_error.show()


        else:


            self.data_model = TableModel(self.filt_appt_list)
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
        self.appt_conf = QMessageBox(self)
        self.appt_conf.setText("Appointment booked")
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
           self.appt_conf.show()
           self.close()
        else:
          self.error_msg = QtWidgets.QMessageBox(self, text="You can only have one appointment booked") # if length of appointment query is not 0 show message saying you can only have one appointment booked at a time
          self.error_msg.show()

    def close_win(self):
        self.close()
        print('closed?')

class admin_bk_appts(QtWidgets.QWidget): # inherit class QMainWindow
    def __init__(self):
        super().__init__()  # call parent class constructor

        self.gapLength = 0 # initialize gap length and set to 0

        self.resize(300,200) # set size of window
        #self.submit = QtWidgets.QPushButton(self) # add submit button
        #self.submit.setGeometry(QtCore.QRect(125, 500, 151, 31)) # set size and location of button
        #self.submit.setText("Submit details") # set button text
        self.lunch_start = None # initialize lunch_start variable and set it to non type
        self.lunch_end = None # initialize lunch_end variable and set it to non type

        #self.s_time = QtWidgets.QLabel(self) # add start time label to window
        #self.s_time.setGeometry(QtCore.QRect(45, 155, 125, 15)) # set size and location of start time label
        #self.s_time.setText('Start time') # add text to start time label


        self.start_time = QDateTimeEdit(self, calendarPopup = True) # add qdatetime edit ti window and seet the calender pop to true , this will allow users to select a date from a calender pop up widget
        #self.start_time.setGeometry(QtCore.QRect(175, 145, 150, 30)) # set size and location of start time widget
        self.start_time.dateTimeChanged.connect(self.check_time) # if the user changes the date/time then check_time method is triggered
        #self.submit.clicked.connect(self.submit_details) # if submit button is clicked this will trigger the submit_details method
        print(" datetime is", self.start_time.dateTime()) # print the default date time for testing purposes
        self.start_time.setDateTime(QDateTime.currentDateTime())

        #self.eTime = QtWidgets.QLabel(self)
        #self.eTime.setGeometry(QtCore.QRect(45, 190, 125, 30))
        #self.eTime.setText('End Time')

        #self.end_time = QDateTimeEdit(self, calendarPopupad=True, date=QDate.currentDate())
        #self.end_time.setGeometry(QtCore.QRect(175, 190, 150, 30))
        #self.et = self.end_time.dateTime()
       # self.et_string = self.et.toString(self.end_time.displayFormat())
        #self.et = self.end_time.dateTimeChanged.connect(lambda: checkTime())

        self.add_appt_form= QFormLayout(self)
        self.add_appt_form.setGeometry(QtCore.QRect(75, 50, 250, 250))

        self.location = QtWidgets.QLineEdit(self)
        self.choose_doctor = QtWidgets.QComboBox(self)
        self.choose_doctor.currentIndexChanged.connect(self.get_index)



        self.add_appt_form.insertRow(1, QtWidgets.QLabel("Location", self), self.location)
        self.add_appt_form.addRow(QtWidgets.QLabel("Start time", self), self.start_time)
        self.add_appt_form.addRow(QtWidgets.QLabel("Choose doctor", self), self.choose_doctor)

        self.add_appt_sbmt = QtWidgets.QPushButton("Submit", self)
        self.add_appt_sbmt.setGeometry(QtCore.QRect(110, 155, 75, 45))
        self.add_appt_sbmt.show()
        self.add_appt_sbmt.clicked.connect(self.submit_details)


        self.get_doc = main.queryDoc() # call sql query method from main file and set it to variable
        print(self.get_doc) # print the variable for testing purposes
        self.doc_list = [] # initialize list
        self.doc_string = "" # initialize doc string
        for i , n , sn in self.get_doc: # loop through results of sql query
            doc_string = str(i) + " " + n  +" " + sn# add loop variables to string
            self.doc_list.append(doc_string) # add doc_string to list
        self.choose_doctor.addItems(self.doc_list) # add doc_string to list




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
        min_time = QtCore.QTime(8, 29)
        max_time = QtCore.QTime(16,30)
        lunch_start = QtCore.QTime(13,00)
        lunch_end = QtCore.QTime(14, 00)
        self.errors = 0

        self.location_widg= self.add_appt_form.itemAt(0, 1)
        self.location_name_widget = self.location_widg.widget()
        self.location_name_widget_data = self.location_name_widget.text()
        print(self.location_name_widget_data , 'location from wiidget')


        if not self.location_name_widget_data:
            self.appt_error = QMessageBox(self)
            self.appt_error.setText("You must provide a location name")
            self.appt_error.show()
            self.errors += 1

        print(self.time_value.currentDateTime(), 'current date time test')

        if self.time_value.currentDateTime() < QtCore.QDateTime.currentDateTime():
            print(self.time_value.time(), ' set time iz')
            print(QtCore.QTime.currentTime(), ' current time iz')
            self.appt_error = QMessageBox(self)
            self.appt_error.setText("Cannot set time in the past")
            self.appt_error.show()
            self.errors += 1
            print(self.errors,'errors')

        if self.time_value.time() > lunch_start and  self.time_value.time() < lunch_end:
            self.appt_error = QMessageBox(self)
            self.appt_error.setText("You cannot book appointments in lunch hour")
            self.appt_error.show()
            self.errors += 1
            print(self.errors, 'errors')




        if self.time_value.time() < min_time or  self.time_value.time() > max_time :
            self.appt_error = QMessageBox(self)
            self.appt_error.setText("You cannot  book appointments before 8am or after 4pm or between 1-2pm")
            self.appt_error.show()
            self.errors += 1
            print(self.errors, 'errors')

        elif self.errors == 0:
            self.get_doc_appts = main.get_doctor_appts(self.doc_id, self.start_date_string[:10]) # call method with sql query

            if len(self.get_doc_appts) == 0: # if length of query is 0 call method with sql query and enter detials
                try:
                    main.insertApptData(self.start_date_string, self.sEndTime, self.location_name_widget_data, "", self.doc_id, "")
                    success = QMessageBox(self)
                    success.setText("Appointment entered succesfully")
                    success.show()
                    self.close()
                except:
                    fail = QMessageBox(self)
                    fail.setText("Appointment not entered")

            elif len(self.get_doc_appts) >= 1: # if length of query is greater to or equal to 1 call the get_end_dates method

                self.get_end_dates()

    def get_end_dates(self):
        self.clash = 0
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

            if self.py_start_date >= self.start_date_string_to_date_obj and  self.py_start_date <= self.end_date_string_to_date_obj +timedelta(minutes=5):
                self.clash += 1


            #if self.py_start_date >=  self.four_hour_check()[0] and  self.py_start_date <= self.four_hour_check()[1]:
                #self.clash +=1


        if self.clash > 0:
            self.error1 = QMessageBox(self)
            self.error1.setText("Selected time clashes with another appointment or lunch hour")
            self.error1.show()



        else: # if user has chosen a datetime that is not between the doctors lunch break then enter call the method with sql  query from the main file
            main.insertApptData(self.start_date_string, self.sEndTime, self.location.text(), "", self.doc_id,"")
            self.errors = 0
            self.appt_conf = QMessageBox(self,text = "Appointment entered succesfully")
            self.appt_conf.show()
            self.close()

    # self.last_appt = self.appts.pop() # get the last end date from the list
    # self.last_appt_start = self.start_dates.pop() # get the last start date from the list
    # print(self.last_appt,'last appointment end time') # print last appt end time for testing purposes
    # print(self.last_appt_start, 'last appointment start time') # prnt last start time for testing purposes
    # def check_time_gap(self , appt): # method that checks gap (difference) between two times

        # self.time_difference = self.py_start_date - appt # calculate difference between user selected datetime and appt( this is is the last appointment start time)
         # self.gapLength = (self.time_difference.total_seconds() / 60) # call total seconds method on the caclulated result from above and divide by 60 get number of minutes


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
        self.add_doc = QtWidgets.QWidget() # create instance of QWidget
        self.add_doc.resize(250, 200) # resize QWidget
        self.add_doc.setWindowTitle("Add doctor") # set title for QWidet
        self.add_doc_form = QFormLayout(self.add_doc) # create QFormLayout and add it to QWidget
        self.add_doc_form.setGeometry(QtCore.QRect(10, 10, 75, 100)) # set size and location of QFormLayout
        self.doc_name = QtWidgets.QLineEdit() # add widgets to form
        self.doc_lname = QtWidgets.QLineEdit()
        self.doc_dob_cal = QtWidgets.QDateEdit(calendarPopup = True) # ad dob field and allow calendar pop up for ease of dob entry by user
        self.doc_specialization = QtWidgets.QLineEdit()

        self.add_doc_form.insertRow(1, QtWidgets.QLabel("First Name", self.add_doc), self.doc_name) # add widgets to QFormLayout and add labels
        self.add_doc_form.addRow(QtWidgets.QLabel("Last Name", self.add_doc), self.doc_lname)
        self.add_doc_form.addRow(QtWidgets.QLabel("Date of birth", self.add_doc), self.doc_dob_cal)
        self.add_doc_form.addRow(QtWidgets.QLabel("Specialization", self.add_doc), self.doc_specialization)
        self.doc_sbmt = QtWidgets.QPushButton("Submit", self.add_doc)
        self.doc_sbmt.setGeometry(QtCore.QRect(95, 155, 100, 35))
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
        self.doc_name_widg = self.add_doc_form.itemAt(0, 1) # locate widget on QFormLayout at position
        self.doc_name_widget = self.doc_name_widg.widget() # return the widget type
        self.doc_name_widget_data = self.doc_name_widget.text() # get the text from the widget
        print(self.doc_name_widget_data, "First name")

        self.doc_surname_widg = self.add_doc_form.itemAt(1, 1)
        self.doc_surname_widget = self.doc_surname_widg.widget()
        self.doc_surname_widget_data = self.doc_surname_widget.text()

        self.doc_dob = self.add_doc_form.itemAt(2, 1)
        self.doc_dob_widget = self.doc_dob.widget()
        self.doc_dob_widget_data = self.doc_dob_widget.text()
        print(self.doc_dob_widget_data, "date from form!")

        self.doc_spec = self.add_doc_form.itemAt(3, 1)
        self.doc_spec_widget = self.doc_spec.widget()
        self.doc_spec_widget_data = self.doc_spec_widget.text()
        print(self.doc_spec_widget_data, "doctor spec")


        self.doc_name_match = re.search("^[A-Za-z]{1,20}$", self.doc_name_widget_data)

        self.doc_surname_match = re.search("^[A-Za-z]{1,20}$",
                                        self.doc_surname_widget_data )

        self.doc_spec_match = re.search("^[A-Za-z]{1,35}(?:\s+[A-Za-z]{0,35})*\s*$", self.doc_spec_widget_data)

        self.doc_error_list = []
        self.doc_msgbox = QMessageBox()

        if self.doc_name_match is not None:
            pass


        else:
            self.doc_error_list.append("Invalid first name")

        if self.doc_surname_match is not None:
            pass


        else:
            self.doc_error_list.append("Invalid last name")

        if self.doc_spec_match is not None:
            pass


        else:
            self.doc_error_list.append("Invalid specialization")

        if len(self.doc_error_list) == 0:
            main.insert_doc_data(self.doc_name_widget_data, self.get_doc_dob_date(), self.doc_spec_widget_data,self.doc_surname_widget_data)
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
        self.get_appointments = main.queryAppts()
        if len(self.get_appointments) == 0:
            self.no_appts = QMessageBox()
            self.no_appts.setText("There are currently no appointments available")
            self.no_appts.show()
            self.close()
        else:

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



        self.setWindowTitle("Patient registration") # set title of window
        self.patient_form = QFormLayout(self) # create instance of a QFormLayout
        self.patient_form.setFormAlignment(QtCore.Qt.AlignCenter) # set alignment of QFormLayout on the QWidget to center
        self.patient_form.setGeometry(QtCore.QRect(150, 150, 300, 300)) # set size and location of QFormLayout
        self.first_name= QtWidgets.QLineEdit() # add  widgets to form
        self.surname = QtWidgets.QLineEdit()
        self.gender= QtWidgets.QComboBox()
        self.gender.addItem("Male")
        self.gender.addItem("Female")
        self.email = QtWidgets.QLineEdit()
        self.p_uname = QtWidgets.QLineEdit()
        self.p_password1 = QtWidgets.QLineEdit()
        self.p_password1.setEchoMode(2) # echomode 2 masks the password




        self.dob= QtWidgets.QDateEdit(calendarPopup = True) # set the dob field to have a pop up calendar allowing the user to easily input their dob

        self.enter_add = QtWidgets.QPushButton()
        self.enter_add.setText("Enter address")
        self.sbmt_details = QtWidgets.QPushButton(self)
        self.sbmt_details.setGeometry(QtCore.QRect(150,375,100,50))
        self.sbmt_details.setText("Submit data")
        self.sbmt_details.show()
        self.sbmt_details.setDisabled(True)


        self.patient_form.insertRow(1, QtWidgets.QLabel("First name", self), self.first_name) # add widgets to form and add labels for them
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





    def get_p_age(self): # calculate patient age

        self.get_p_age = self.dob.date() # get date value from patient dob field
        self.py_date_age = self.get_p_age.toPyDate() # convert qdate to python date object
        print("py date is ", self.py_date_age) # print python date object for testing purposes
        self.date_now = date.today().year # get the current year
        self.p_calc_age = (self.date_now - self.py_date_age.year) # calculate age by taking away the current year from the year entered by the user




    def test(self): # used for testing
        print("trigger test")


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




        self.p_name = self.patient_form.itemAt(0, 1) # locate widget item in form
        self.p_name_widget = self.p_name.widget() # get the widget type
        self.p_name_text = self.p_name_widget.text() # return the text from widget
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
            self.add_line += line + " "


        self.preg_error_string = [] # set up error string list
        self.preg_list = [] # set up list to hold registration data
        self.patient_details = QMessageBox() # set up message box to show user input error guidance


        self.fname_match = re.search("^[A-Za-z]{1,20}$", self.p_name_text) # search text field for regex pattern



        if self.fname_match is not None: # if a match is found in the reg ex pattern
            print("Valid first name")
            print(self.fname_match)
            self.preg_list.append(self.p_name_text) # append text from field to string


        else:
            print("First name not valid")
            print(self.fname_match)
            self.preg_error_string.append("Invalid first name") # if pattern is not found append this message to the error string

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

        self.pword_match = re.search("^[A-Z]{1}\w{1,10}[!]$", self.p_password_text)

        if self.pword_match is not None:
            print("Valid password")
            print(self.pword_match)
            self.preg_list.append(self.p_password_text)


        else:
            print("Password not valid")
            print(self.p_password_text, 'password is')
            print(self.pword_match)
            self.preg_error_string.append("Password must start with a capital and end with a ! and be less than 10 characters")


        print(len(self.preg_error_string),' preg error string')

        self.p_user_check= main.check_user_name(self.p_user_text) # call method that checks database for matching usernames

        if len(self.preg_error_string) == 0 : # if the patient details string has 0 errors

            if len(self.p_user_check) == 0: # if user name is unique





                main.insert_puser_data(self.p_name_text,self.p_calc_age, self.p_gender_text1,self.p_user_text,self.p_password_text,self.p_email_text, self.add_line,self.p_surname_text)  # call function with sql query from main and insert the doctor object attributes
                self.details_success = QMessageBox()
                self.details_success.setText("Details entered successfully") # tell user that details have been succesfully entered
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


