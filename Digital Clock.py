# Python PyQt5 Digital Clock

# Pseudocode for PyQt5 Digital Clock
# Import Necessary Modules

# Import sys for system-specific parameters and functions.
# Import QApplication, QWidget, QLabel, QVBoxLayout from PyQt5.QtWidgets for creating the GUI.
# Import QTimer, QTime, Qt from PyQt5.QtCore for handling time and timers.
# Import QFont, QFontDatabase from PyQt5.QtGui for font customization.
# Define DigitalClock Class

# Class: DigitalClock inherits from QWidget.

# Constructor: __init__()

# Call the parent class constructor.
# Create a QLabel widget to display the time.
# Create a QTimer to update the time every second.
# Initialize the user interface by calling initUI().
# Method: initUI()

# Set Window Properties:
# Set the window title to "Digital Clock".
# Set the window size and position using setGeometry(x, y, width, height).
# Layout Setup:
# Create a vertical box layout (QVBoxLayout).
# Add the time_label to the layout.
# Set the layout for the main widget.
# Label Alignment:
# Align the time_label to the center using Qt.AlignCenter.
# Style the Time Label:
# Apply CSS styles to time_label:
# Set font-size to 150px.
# Set color using HSL values.
# Set the background color of the window to black.
# Load Custom Font:
# Add a custom font (DS-DIGIT.TTF) to the application using QFontDatabase.
# Retrieve the font family name.
# Create a QFont object with the custom font family and size 150.
# Apply the custom font to time_label.
# Setup Timer:
# Connect the timer's timeout signal to the update_time method.
# Start the timer with a 1000ms (1 second) interval.
# Initial Time Update:
# Call update_time() to display the current time immediately.
# Method: update_time()

# Get the current system time in the format hh:mm:ss AP (e.g., 08:30:45 PM).
# Update the time_label with the current time string.
# Main Functionality

# Check if the script is run directly:
# Create a QApplication instance.
# Create an instance of DigitalClock.
# Show the digital clock window.
# Execute the application's event loop using app.exec_().
# Summary of Steps
# Setup and Imports:

# Import necessary PyQt5 modules and other Python libraries.
# Create DigitalClock Class:

# Initialize the main widget.
# Set up the user interface, including layout and styling.
# Load and apply a custom font.
# Initialize and start a timer to update the clock every second.
# Update Time Display:

# Define a method to fetch the current time and display it on the label.
# Run the Application:

# Instantiate the application and the DigitalClock widget.
# Display the clock and start the event loop.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 150px;"
                                    #   "font-family: Arial;"
                                      "color: hsl(349, 71%, 36%);")
        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 150)
        self.time_label.setFont(my_font)

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())