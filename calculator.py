import sys
import numpy as np
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget, QGridLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        # Create the display and the buttons
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(15)

        num_buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        # Create a grid layout to hold the buttons
        grid = QGridLayout()
        grid.setSpacing(10)

        # Add the buttons to the grid
        row = 1
        col = 0
        for button in num_buttons:
            btn = QPushButton(button)
            btn.setFixedSize(40, 40)
            btn.clicked.connect(self.num_button_clicked)
            grid.addWidget(btn, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Add the display and the grid to the main layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid)
        self.setLayout(main_layout)

        # Set the window title
        self.setWindowTitle("Calculator")

    def num_button_clicked(self):
        # Get the clicked button's text
        button = self.sender()
        num = button.text()

        # If the user clicked the "=" button, evaluate the expression and display the result
        if num == "=":
            result = str(eval(self.display.text()))
            self.display.setText(result)
        # If the user clicked the "." button, only add it if it is not already in the display
        elif num == ".":
            if "." not in self.display.text():
                self.display.setText(self.display.text() + num)
        # Otherwise, just append the clicked number to the display
        else:
            self.display.setText(self.display.text() + num)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
