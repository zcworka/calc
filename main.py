from ast import Delete
from ui import calc
from PyQt5 import QtWidgets, QtCore
import math_str_processor 
from queue import LifoQueue
import os
import sys

class Root(QtWidgets.QMainWindow ,calc.Ui_MainWindow):

    output = ""
    previous = ""
    previous_for_stack = "0"
    commands_stack = LifoQueue()
    commands_stack.put("0")
    cs_lastisequal = False
    

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        Root.show(self)
        # numpad
        self.one_button.clicked.connect(lambda: self.add_text(self.one_button.text()))
        self.two_button.clicked.connect(lambda: self.add_text(self.two_button.text()))
        self.three_button.clicked.connect(lambda: self.add_text(self.three_button.text()))
        self.four_button.clicked.connect(lambda: self.add_text(self.four_button.text()))
        self.five_button.clicked.connect(lambda: self.add_text(self.five_button.text()))
        self.six_button.clicked.connect(lambda: self.add_text(self.six_button.text()))
        self.seven_button.clicked.connect(lambda: self.add_text(self.seven_button.text()))
        self.eight_button.clicked.connect(lambda: self.add_text(self.eight_button.text()))
        self.nine_button.clicked.connect(lambda: self.add_text(self.nine_button.text()))
        self.zero_button.clicked.connect(lambda: self.add_text(self.zero_button.text()))
        self.plus_button.clicked.connect(lambda: self.add_text(self.plus_button.text()))
        self.minus_button.clicked.connect(lambda: self.add_text(self.minus_button.text()))
        self.multy_button.clicked.connect(lambda: self.add_text(self.multy_button.text()))
        self.division_button.clicked.connect(lambda: self.add_text(self.division_button.text()))
        self.dot_button.clicked.connect(lambda: self.add_text(self.dot_button.text()))
        self.percent_button.clicked.connect(lambda: self.add_text(self.percent_button.text()))
        self.root_button.clicked.connect(lambda: self.add_text("√"))
        self.power_button.clicked.connect(lambda: self.add_text("^"))
        self.fact_button.clicked.connect(lambda: self.add_text("!"))
        self.fbrack_button.clicked.connect(lambda: self.add_text(self.fbrack_button.text()))
        self.sbrack_button.clicked.connect(lambda: self.add_text(self.sbrack_button.text()))

        self.clear_button.clicked.connect(lambda: self.clear_output())
        self.backspace_button.clicked.connect(lambda: self.backspace())
        self.repeat_button.clicked.connect(lambda: self.repeat())
        self.equal_button.clicked.connect(lambda: self.press_equal_button())

        self.previous_list.setAutoScroll(False)
        self.previous_list.itemClicked.connect(lambda item: self.set_clicked(item))


        # stylesheet
        bundle_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
        css_file_path = os.path.abspath(os.path.join(bundle_dir, 'css/main.css'))
        if '_MEIPASS2' in os.environ:
            css_file_path = os.path.join(os.environ['_MEIPASS2'], css_file_path)
        css_file = open(css_file_path, 'rb')
        self.centralwidget.setStyleSheet(css_file.read().decode())
        css_file.close()
        

    def repeat(self):
        if self.commands_stack.qsize() >= 1:
            result = self.commands_stack.get(block=False)
            self.set_text(result)
            self.output = result
            

    def backspace(self):
        self.output = self.output[:-1]
        self.output_label.setText(self.output_label.text()[:-1])

    def clear_output(self):
        self.output = ""
        self.output_label.setText("")

    def add_text(self, text):
            self.output += str(text)
            self.output_label.setText(self.output)
    def set_text(self, text):
        self.output_label.setText(text)
    
    def set_clicked(self, item):
        clicked_text = item.text().replace("Last: ", "")
        clicked_text = clicked_text[:clicked_text.index(" = ")]
        self.output = clicked_text
        self.output_label.setText(self.output)
    
    def press_equal_button(self):
        _translate = QtCore.QCoreApplication.translate
        self.previous = self.output
        self.commands_stack.put(self.previous_for_stack)
        self.previous_for_stack = self.previous
        self.output = math_str_processor.process_str(self.output)
        if not self.previous == "":
            self.previous = self.previous + f" = {self.output}\n"
            self.set_text(self.output)
            
            item = QtWidgets.QListWidgetItem()
            item.setText(_translate("MainWindow", self.previous))
            self.previous_list.addItem(item)
            last_item = self.previous_list.item(self.previous_list.count() - 1)
            last_item.setText("Last: " + last_item.text())
            last_item.setSelected(True)
            self.previous_list.scrollToItem(last_item)
            
            if self.previous_list.count() > 1:
                previous_last_item = self.previous_list.item(self.previous_list.count() - 2)
                if last_item.text() == previous_last_item.text():
                    self.previous_list.takeItem(self.previous_list.count() - 2)
                previous_last_item.setText(previous_last_item.text().replace("Last: ", ""))




        
    
    
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Root()
    sys.exit(app.exec_())