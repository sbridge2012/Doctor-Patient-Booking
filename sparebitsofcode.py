import sys

from PyQt5 import QtCore, QtWidgets , QtGui
from PyQt5.QtWidgets import QMainWindow, QAction, QDateTimeEdit , QDateEdit , QApplication


class screen(QMainWindow): #  class that shows window when user has logged in
    def __init__(self):
        super().__init__() #  call parent class constructor


        self.resize(300,600)
        self.setWindowTitle("cheese house")

        self.setObjectName("efefw")


    #self.resize(300, 200)  # set size of window
    #self.setWindowTitle("Welcome to Patient/Doctor app ")  # set title

        self.register = QtWidgets.QPushButton(self)  # add book appointments button to window
        self.register.setGeometry(QtCore.QRect(80, 40, 150, 30))  # set size and location of button
        self.register.setText("Register chn")  # set button text


        self.register.clicked.connect(self.showwidg)

    def showwidg(self):
        print("cheesey1")
        self.widg = QtWidgets.QWidget()
        self.widg.resize(200,200)
        self.setWindowTitle("new tab")
        rum = QtWidgets.QPushButton(self.widg)
        rum.setGeometry(QtCore.QRect(80, 40, 150, 30))


        self.widg.show()





        #self.login = QtWidgets.QPushButton(self)  # add view appointments button
        #self.login.setGeometry(QtCore.QRect(80, 100, 150, 30))  # set size and location of view appointments button
        #self.login.setText("Login")  # set text for view appointments button

        #login1 = QtWidgets.QPushButton(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # enter main event loop
    # l = Layout() # make instance of layout class as this will be the class that is launched upon running the programme
    S = screen()
    S.show()
    sys.exit(app.exec_())
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

   def sbmtfunc(self):
        self.add_list = []
        for row in range(self.form_layout.rowCount()):

            self.get_add_data = self.form_layout.itemAt(row,1) # prints house no
            self.widget = self.get_add_data.widget()
            self.add_data = self.widget.text()
            self.add_list.append(self.add_data)

            self.get_post_code = self.form_layout.itemAt(4, 1)  # prints house no
            self.post_widget = self.get_post_code.widget()
            self.post_data = self.post_widget.text()

            if self.post_data == "1":
                print("cool")


            if self.add_data == "":
                print("Empty string")

                self.validate_box = QMessageBox(self)
                self.validate_box.setText("Please complete all address fields")
                self.validate_box.show()

            else:
                    self.msg_box = QMessageBox(self)
                    self.msg_box.setText("Address data submitted")
                    self.msg_box.exec_()
                    self.address_window.close()
                    for i in self.add_list:
                        print(i)
                        print(len(self.add_list), "length")




        #return super().setHeaderData(p_int, Qt_Orientation, Value, role) # return the set header data method from abstractitemmodel class which abstract table model inherits from
        # return super().headerData(p_int, Qt_Orientation, role) # return the parent class (abstract item model) method
