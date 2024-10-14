class patient_book_appts(QMainWindow): # qmain window displaying available appointments for patients to book
    def __init__(self):
        super().__init__() # call parent class ( QMainWindow) constructor

        self.resize(825,800) # set window size
        self.get_appts = main.queryAppts()
        self.list=[] # initialize list
        self.appts_string=""  # initialize string
        self.date_picker = QtWidgets.QDateTimeEdit(self,calendarPopup= True)
        self.date_picker.setGeometry((QtCore.QRect(325, 50, 150, 75)))
        self.date_picker.setDate(QDate.currentDate())

        self.table = QtWidgets.QTableView(self)
        self.table.setGeometry(QtCore.QRect(50, 150, 700, 505))
        self.submit_btn = QtWidgets.QPushButton(self)
        self.submit_btn.setGeometry(QtCore.QRect(350,675,75,45))
        self.submit_btn.setText("Submit")

        #data = [

                #["1","2","3","4","6"],

        # ["10","20","30","40","60"],
        # ["20", "30", "40", "50", "80"]

                #]


        self.tab_row = 0
        #print(self.get_appts)
        #self.data_model = TableModel(data)
        #self.table.setModel(self.data_model)
        #self.table.show()




        self.qb = QButtonGroup(self.table)
        for self.data in self.get_appts:
            self.table.setRowCount(len(self.get_appts))
            self.table.setColumnCount(len(self.get_appts[0]))
            self.table.setItem(self.tab_row, 0, QTableWidgetItem(self.data[0]))
            self.table.setItem(self.tab_row, 1,QTableWidgetItem(self.data[1]))
            self.table.setItem(self.tab_row, 2, QTableWidgetItem(self.data[2]))
            self.table.setItem(self.tab_row, 3, QTableWidgetItem(self.data[3]))
            self.table.setHorizontalHeaderLabels(["Start Time", "End Time", "Location", "Doctor", "Select one"])
            self.table.setColumnWidth(0, 160)
            self.table.setColumnWidth(1,160)
            self.table.setColumnWidth(2,120)
            self.table.setColumnWidth(3, 140)

            self.item = QTableWidgetItem(self.tab_row[0])
            self.item.setFlags(QtCore.Qt.ItemIsUserCheckable |
                          QtCore.Qt.ItemIsEnabled)
            self.item.setCheckState(QtCore.Qt.Unchecked)

            self.table.setItem(self.tab_row,4)

            #self.cb = QCheckBox(self.table)
            #self.check_item = (QTableWidgetItem(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled))
            #self.check_item.setCheckState(QtCore.Qt.Unchecked)

            #self.cb.show()
            #self.qb.addButton(self.cb)
            #elf.table.setCellWidget(self.tab_row, 4, self.cb)

            #if self.cb.isChecked():
                #print("yes it is checked")
            #self.cb.clicked.connect(self.change)
            #self.tab_row += 1

            #self.date_picker.dateChanged.connect(self.appt_date_filter)
            #self.table.cellClicked.connect(self.change)
            #elf.submit_btn.clicked.connect(self.submitted)



    def appt_date_filter(self):
        self.date_filter = self.date_picker.date()
        self.filter_date_py = self.date_filter.toPyDate()
        self.filter_date_string = self.filter_date_py.strftime("%Y-%m-%d")
        print(self.filter_date_string, "filter date")

        self.get_filt_apps = main.filter_appts(self.filter_date_string)

        self.tab_row1 = 0

        for filt_data in self.get_filt_apps:
            self.table.setRowCount(len(self.get_filt_apps))
            self.table.setColumnCount(len(self.get_filt_apps[0]))
            self.table.setItem(self.tab_row1, 0, QTableWidgetItem(filt_data[0]))
            self.table.setItem(self.tab_row1, 1,QTableWidgetItem(filt_data[1]))
            self.table.setItem(self.tab_row1, 2, QTableWidgetItem(filt_data[2]))
            self.table.setItem(self.tab_row1, 3, QTableWidgetItem(filt_data[3]))

            self.cb1 = QCheckBox(self.table)

            self.cb1.show()
            self.qb.addButton(self.cb1)
            # self.table.setCellWidget(self.tab_row1, 4, self.cb)

            self.tab_row1 += 1

            self.table.cellClicked.connect(self.change)
            self.submit_btn.clicked.connect(self.submitted)

    def change(self):

        #if self.cb.isChecked():

        self.checkboxclicked = self.cb.sender()
        self.index = self.table.indexAt(self.checkboxclicked.pos())
        print(self.index.row(), "row of index in submitted")

            #else:

            #self.filtered_checkboxclicked = self.cb1.sender()
            #self.filtered_index = self.table.indexAt(self.checkboxclicked.pos())
            # print(self.table.item(current_row,2).text(), ' this is the selection')
            # print(self.docid, "doc id in change")


    def submitted(self):

        # print(self.checkboxclicked, "checkbox clicked")
        self.chosen_appt_start = self.table.item(self.index.row(), 0).text()
        self.chosen_appt_location = self.table.item(self.index.row(), 2).text()
        print(self.chosen_appt_start, " ", self.chosen_appt_location)
        self.start_and_doc = main.get_selected_appts_id(self.chosen_appt_start, self.chosen_appt_location)



        for id  in self.start_and_doc:
         self.start_and_doc_selc = (id)
        print(self.start_and_doc_selc[0])
        main.update_appts(loginScreen.logged_in_patientid,self.start_and_doc_selc[0])



    def filtered_change(self):

        self.filtered_checkbox_clicked = self.cb1.sender()
        self.filtered_index = self.table.indexAt(self.filtered_checkbox_clicked.pos())

    def filtered_submitted(self):
        print("filtered subbmitted")

        # print(self.checkboxclicked, "checkbox clicked")
        self.filtered_appt_start = self.table.item(self.index.row(), 0).text()
        self.filtered_appt_location = self.table.item(self.index.row(), 2).text()

        self.filtered_start_and_doc = main.get_selected_appts_id(self.filtered_appt_start, self.filtered_appt_location)
        print(self.start_and_doc, "appts id is  +")

        for id in self.filtered_start_and_doc:
            self.start_and_doc_selc = (id)
        print(self.start_and_doc_selc[0])
        main.update_appts(loginScreen.logged_in_patientid, self.start_and_doc_selc[0])



    def press_check(self): # this method will return the index of the item that has been clicked as a string

        self.get_appt = self.qlist.currentItem().text()[:2] # get the first two characers of the string

        print(type(self.get_appt))

        return int(self.get_appt) # convert the self.get_appt to an int and return it



    def submit_data(self):  # method to submit data to database
         print("patient apps numb", len(main.get_patient_appts(loginScreen.logged_in_patientid))) # get length of query result for testing purposes
         if len(main.get_patient_appts(loginScreen.logged_in_patientid)) == 0:  # if length is 0 insert call update appointments method query from main file
             main.update_appts(loginScreen.logged_in_patientid, self.apptid)
         else:
             self.error_msg = QtWidgets.QMessageBox(self, text="You can only have one appointment booked") # if length of appointment query is not 0 show message saying you can only have one appointment booked at a time
             self.error_msg.show()