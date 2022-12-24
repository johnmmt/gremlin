import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QBrush
import matplotlib.pyplot as plt

class GraphingCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # Create the input fields for the equation and range
        equation_label = QLabel("Equation:")
        self.equation_field = QLineEdit()
        range_label = QLabel("Range:")
        self.range_field = QLineEdit()

        # Create the "Graph" button and connect it to the graph_button_clicked method
        graph_button = QPushButton("Graph")
        graph_button.clicked.connect(self.graph_button_clicked)

        # Use a horizontal layout to arrange the input fields and button
        input_layout = QHBoxLayout()
        input_layout.addWidget(equation_label)
        input_layout.addWidget(self.equation_field)
        input_layout.addWidget(range_label)
        input_layout.addWidget(self.range_field)
        input_layout.addWidget(graph_button)

        # Create a graphics view widget to display the graph
        self.graphics_view = QGraphicsView(self)

        # Use a vertical layout to arrange the input layout and graphics view
        main_layout = QVBoxLayout()
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.graphics_view)
        self.setLayout(main_layout)

    def graph_button_clicked(self):
        # Get the equation and range from the input fields
        equation = self.equation_field.text()
        x_range = self.range_field.text()

        # Use NumPy's linspace function to generate an array of x-values over the specified range
        x_values = np.linspace(float(x_range.split(",")[0]), float(x_range.split(",")[1]), 100)

        # Use NumPy's eval function to evaluate the equation for each x-value and generate an array of y-values
        y_values = np.eval(equation, {'x': x_values})

        # Create a figure and axis using Matplotlib
        figure, axis = plt.subplots()

        # Plot the x and y values on the axis
        axis.plot(x_values, y_values)

        # Clear the graphics view's scene and set it to the Matplotlib figure
        self.graphics_view.setScene(QGraphicsScene())
        self.graphics_view.setScene(MatplotlibFigureToGraphicsScene(figure))

# Convert a Matplotlib figure to a QGraphicsScene
def MatplotlibFigureToGraphicsScene(figure):
    # Create a QGraphicsScene and add the figure to it
