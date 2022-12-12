# NPRL-GUI - In Progress
For Emory University's Neural Plasticity Research Laboratory with a GUI that displays a progress bar with the force exerted on the loadcell. 

Use Python 3.10, latest Python version
Do not do pip install serial, do ```pip install pyserial```

Do not do pip install PIL, do ```pip install pillow```

Useful Documentation for using customtkinter and the Adafruit Neopixel LED strip:

https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-use

https://github.com/TomSchimansky/CustomTkinter

File Descriptions:
 - NPRL_GUI_KG.py 
    - File starts up the GUI and outputs the force from the load cell on the rig in kilograms so when someone presses against the load cell, it will update the progress bar and show values in kg
Run the file by clicking on it and pressing the run button on the top right corner of Visual Studio Code
 - Other folders and files included in the project
    - data_files folder
      - Contains all CSV files titled current_data.csv that have the results of running the GUI with columns listing the current time, forces exerted, max forces, average max force, and number of trials
    - NPRL_Side_Quest_Default folder
        - Has NPRL_Side_Quest_Default.ino file that is the current Arduino code loaded on the Arduino Nano that gets the force data from the load cell and changes the LED strip colors
    - NPRL_Side_Quest file
        - File calibrates the load cell and how it calculates the force data
    - theme.json
        - Color theme of the GUI

