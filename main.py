from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMessageBox
from views.Visualiser import plot_robdd
from views.main_window import Ui_MainWindow
from views.InputPage import Ui_INPUT
from views.OutputPage import Ui_Output
from views.ROBDD_Logic import Evaluate
import re
import itertools

"""This file contains the main window and its corresponding classes.
It also contains the second window and its corresponding classes.
The third window is the one that displays the results."""


class ThirdWindow(QMainWindow):
    """Class for the second window."""
    def __init__(self,result,expr1,expr2,vorder1,vorder2,BDD1,BDD2,ROBDD1,ROBDD2):
        super().__init__()
        self.ui = Ui_Output()
        self.ui.setupUi(self)
        self.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QLabel {
                color: black;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }  
            QMainWindow {
                 background-color: #F5F5F5;
            }
        """)
        happy = "Images/happy_spongebob.png"
        sad = "Images/sad_spongebob.png"
        self.ui.Function1.setText(expr1)
        self.ui.Function2.setText(expr2)
        self.ui.Vorder1.setText(vorder1)
        self.ui.Vorder2.setText(vorder2)
        self.ui.equiv.setText("The two Boolean functions are equivalent." if result == "True" else "The two Boolean functions are not equivalent.")
        if result == "True":
            self.ui.equiv.setStyleSheet("color: green;")
            self.ui.spongebob.setPixmap(QPixmap(happy))
            print("the 2 boolean functions are equivalent")
        else:
            self.ui.equiv.setStyleSheet("color: red;")
            self.ui.spongebob.setPixmap(QPixmap(sad))
            print("the 2 boolean functions are NOT equivalent")
        self.ui.TryAgain.clicked.connect(self.open_second_window)
        self.ui.ShowBDD1.clicked.connect(lambda: self.visualise(BDD1,"BDD1"))
        self.ui.ShowBDD2.clicked.connect(lambda: self.visualise(BDD2,"BDD2"))
        self.ui.ShowROBDD1.clicked.connect(lambda: self.visualise(ROBDD1, "ROBDD1"))
        self.ui.ShowROBDD2.clicked.connect(lambda: self.visualise(ROBDD2,"ROBDD2"))

    def visualise(self,data,figname):
        plot_robdd(data,figname)

    def open_second_window(self):
        """Open the second window."""
        self.ui = SecondWindow()
        self.close()
        self.ui.show()

"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""
"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""
"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""
"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""


class SecondWindow(QMainWindow):
    """Class for the second window."""
    def __init__(self):
        super().__init__()
        self.ui = Ui_INPUT()
        self.ui.setupUi(self)
        self.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QLabel {
            color: black;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
            QMainWindow {
                background-color: #F5F5F5;
            }
        """)

        # Connect the Start button to open the second window
        self.ui.Calcul.clicked.connect(self.open_third_window)

        # Connect Save buttons to their functions
        self.ui.savef1.clicked.connect(lambda: self.save_function(self.ui.Func1, self.ui.Vorder1,self.ui.Error1))
        self.ui.savef2.clicked.connect(lambda: self.save_function(self.ui.Func2, self.ui.Vorder2,self.ui.Error2))



    def save_function(self, line_edit, combo_box, error_label):
        """Save function input, generate variable orderings, and display errors if needed."""
        # Get text from the line edit
        function_text = line_edit.text()

        # Validate the function input
        if not re.match(r'^[A-Za-z()&|+~!]+$', function_text):
            # Display the error message
            error_label.setText("Error: Invalid input! Only Alphabetical variables and these symbols '()&|+~!' are allowed.")
            error_label.setStyleSheet("color: red;")
            error_label.show()

            # Clear the line edit
            line_edit.clear()
            return
        else:
            # Clear error label if the input is valid
            error_label.clear()

        # Extract unique variables from the function text
        variables = sorted(set(re.findall(r'[A-Za-z]+', function_text)))

        # Generate all permutations of variables (variable orderings)
        orderings = list(itertools.permutations(variables))

        # Clear the combo box and insert new items
        combo_box.clear()
        for ordering in orderings:
            combo_box.addItem(", ".join(ordering))

        # Optional: Display a message box indicating success
        success_box = QMessageBox(self)
        success_box.setWindowTitle("Success")
        success_box.setText(f"Function saved successfully!\n{len(orderings)} variable orderings generated for \n{len(variables)} variables in the function.")
        success_box.setStyleSheet("QLabel{color: white;}")
        success_box.exec()


    def open_third_window(self):
        variables_in_Func1 = sorted(set(re.findall(r'[A-Za-z]+', self.ui.Func1.text())))
        variables_in_Func2 = sorted(set(re.findall(r'[A-Za-z]+', self.ui.Func2.text())))
        variables_in_Vorder1 = sorted(set(re.findall(r'[A-Za-z]+', self.ui.Vorder1.currentText())))
        variables_in_Vorder2 = sorted(set(re.findall(r'[A-Za-z]+', self.ui.Vorder2.currentText())))
        if self.ui.Func1.text() == "" or self.ui.Func2.text() == "":
            if self.ui.Func1.text() == "":
                self.ui.Error1.setText("Error: Function cannot be empty.")
                self.ui.Error1.setStyleSheet("color: red;")
                self.ui.Error1.show()

                # Clear the line edit
                self.ui.Func1.clear()

            if self.ui.Func2.text() == "":
                self.ui.Error2.setText("Error: Function cannot be empty.")
                self.ui.Error2.setStyleSheet("color: red;")
                self.ui.Error2.show()

                # Clear the line edit
                self.ui.Func2.clear()
            return
        elif self.ui.Vorder1.currentText() == "" or self.ui.Vorder2.currentText() == "":

            if self.ui.Vorder1.currentText() == "":
                self.ui.Error1.setText("Warning: Variable order cannot be empty.Please click save button to generate variable orderings.")
                self.ui.Error1.setStyleSheet("color: purple;")
                self.ui.Error1.show()

            if self.ui.Vorder2.currentText() == "":
                self.ui.Error2.setText("Warning: Variable order cannot be empty.Please click save button to generate variable orderings.")
                self.ui.Error2.setStyleSheet("color: purple;")
                self.ui.Error2.show()
            return
        if variables_in_Func1 != variables_in_Vorder1 or variables_in_Func2 != variables_in_Vorder2:
            if variables_in_Func1 != variables_in_Vorder1:
                self.ui.Error1.setText("Error: Variable orderings do not match the function.Click save to generate proper variable orderings.")
                self.ui.Error1.setStyleSheet("color: magenta;")
                self.ui.Error1.show()
            if variables_in_Func2 != variables_in_Vorder2:
                self.ui.Error2.setText("Error: Variable orderings do not match the function.Click save to generate proper variable orderings.")
                self.ui.Error2.setStyleSheet("color: magenta;")
                self.ui.Error2.show()
            return
        else:
            """Open the third window and process the Boolean functions."""
            expr1 = self.ui.Func1.text()
            expr2 = self.ui.Func2.text()
            varOrder1 = self.ui.Vorder1.currentText()
            varOrder2 = self.ui.Vorder2.currentText()
            result , BDD1 , BDD2 , ROBDD1 ,ROBDD2 = Evaluate(expr1, expr2, varOrder1, varOrder2)
            self.ui = ThirdWindow(result=result,expr1=expr1,expr2=expr2,vorder1=varOrder1,vorder2=varOrder2,BDD1=BDD1,BDD2=BDD2,ROBDD1=ROBDD1,ROBDD2=ROBDD2)
            self.close()
            self.ui.show()

"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""
"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""
"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""
"""|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"""


class MainWindow(QMainWindow):
    """Class for the main window."""
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setStyleSheet("""
            QPushButton {
                background-color: #007BFF;
                color: white;
                border-radius: 5px;
                padding: 10px;
            }
            QLabel {
                color: black;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }  
            QMainWindow {
                 background-color: #F5F5F5;
            }
        """)
        # Connect the Start button to open the second window
        self.ui.pushButton.clicked.connect(self.open_second_window)

    def open_second_window(self):
        """Open the second window."""

        self.ui = SecondWindow()
        self.close()
        self.ui.show()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
