import tkinter
from tkinter import *
import customtkinter
import serial 
import threading
from PIL import Image, ImageTk
import csv
import time

time.sleep(2)
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("theme.json")
ArduinoSerial = serial.Serial('COM3', 9600)
data_saved = []
max_force_saved = []
average_saved = []
app = customtkinter.CTk()
app.geometry("1000x700")
app.title("NPRL Force Sensor GUI")
current_progress = 0
displayVar = StringVar()
maxValueStr = StringVar()
targetStr = StringVar()
countStr = StringVar()
maxValueStr.set("Max Value")
targetStr.set("Target: ")
displayVar.set("Current Progress: ")
countStr.set("Current Count: ")
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
frame_left = customtkinter.CTkFrame(master=app,
                                 width=180,
                                 corner_radius=0)
frame_left.grid(row=0, column=0, sticky="nswe")

frame_right = customtkinter.CTkFrame(master=app)
frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)
label_left = customtkinter.CTkLabel(master=frame_left,
                                    text="NPRL Force Sensor GUI",
                                    text_font=("Roboto Medium", -16))
target = 1
target_range = 0.01
def button_event():
    global target, target_range
    target = float(entry_target.get())
    target_range = float(entry_range.get())
    targetStr.set("Target: " + str(target))
label_left.grid(row=1, column=0, pady=10, padx=10)
entry_target = customtkinter.CTkEntry(master=frame_left, placeholder_text="Target")
entry_target.grid(row=4, column=0, pady=10, padx=10)
entry_range = customtkinter.CTkEntry(master=frame_left, placeholder_text="Range from target")
entry_range.grid(row=5, column=0, pady=10, padx=10)
button = customtkinter.CTkButton(master=frame_left, text="Submit", command=button_event)
button.grid(row=6, column=0, pady=10, padx=10)

img = ImageTk.PhotoImage(Image.open("NPRL.png"))
img_label = Label(frame_left, image = img, borderwidth=0)
img_label.grid(row=12, column=0, padx=30, pady=30)

frame_right.rowconfigure((0, 1, 2, 3), weight=1)
frame_right.rowconfigure(7, weight=20)
frame_right.columnconfigure((0, 1), weight=1)
frame_right.columnconfigure(2, weight=0)
frame_info = customtkinter.CTkFrame(master=frame_right)
frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=10, padx=10, sticky="nsew")

frame_info.rowconfigure(0, weight=1)
frame_info.columnconfigure(0, weight=1)
progressbar = customtkinter.CTkProgressBar(master=frame_info)
progressbar.grid(row=2, column=0, sticky="ew", padx=15, pady=15)

label_info_1 = customtkinter.CTkLabel(master=frame_info,
                                      text="NPRL Force Sensor Output",
                                      height=100,
                                      corner_radius=3,
                                      justify=tkinter.LEFT,
                                      text_font=("Roboto Medium", -16))
label_info_1.grid(column=0, row=0, sticky="we", padx=5, pady=5)
displayLab = Label(frame_info, textvariable=displayVar, background='#333333', fg="white")
displayLab.grid(column=0, row=1, sticky="we", padx=5, pady=5)
maxValueLab = Label(frame_info, textvariable=maxValueStr, background='#333333', fg="white")
maxValueLab.grid(column=0, row=3, sticky="we", padx=5, pady=5)
targetLab = Label(frame_left, textvariable=targetStr, background='#2c2c24', fg="white")
targetLab.grid(column=0, row=8, sticky="we", padx=5, pady=5)
countLab = Label(frame_left, textvariable=countStr, background='#2c2c24', fg="white")
countLab.grid(column=0, row=9, sticky="we", padx=5, pady=5)


progressbar.set(0)
progressbar.configure(height=35)
switch = customtkinter.CTkSwitch(frame_left, text="Calibration")
switch.grid(row=7, column=0, padx=20, pady=10)
switch.deselect()
max_force = 0
max_force_arr = []
i = 0
csvlist = []
max_force_not_average = 0
def turn_green():
    print("green")
    ArduinoSerial.write(b'x')
def turn_blue():
    print("blue")
    ArduinoSerial.write(b'z')
def turn_red():
    print("red")
    ArduinoSerial.write(b'v')
def add_element(list, curr, max, average):
    mydict = {}
    mydict['Force Exerted'] = curr
    mydict['Max Forces'] = max
    mydict['Average Max Force'] = average
    list.append(mydict)
def arduino_handler():
    global current_progress
    global data_saved
    global max_force_saved
    global average_saved
    global max_force
    global max_force_arr
    global max_force_not_average
    global i
    global maxValueStr
    global csvlist
    global target, target_range
    while True:
        data = ArduinoSerial.readline().decode('utf-8').strip()
        print(data)
        current_progress = float(data)
        displayVar.set("Current Progress: " + str(abs(current_progress)))
        countStr.set("Current Count: " + str(i))
        if switch.get():
            print("Time: " + str(time.time()))
            curr_time = time.time()
            target_time = curr_time + 5
            max_force_arr.append(0.0)
            while curr_time < target_time:
                curr_time = time.time()
                data = ArduinoSerial.readline().decode('utf-8').strip()
                print("Current Progress Data: ", data)
                current_progress = float(data)
                print("Updating Current Progress", current_progress)
                if current_progress > max_force_arr[i]:
                    # print("Updating Max Force: ", max_force)
                    # print("Max Force Array", max_force_arr)
                    max_force_arr[i] = current_progress
                    # maxValueStr.set("Max Force: " + str(max_force))
                    target = max_force_arr[i] * 0.15
                    print("Target: " + str(target))
                    targetStr.set("Target: " + str(target))
                    if not max_force == 0:
                        progressbar.set(current_progress/max_force)
                        progressbar.configure(progress_color='#0362fc', height=35)
                        turn_blue()
            switch.deselect()
            for x in max_force_arr:
                    max_force += x
            max_force_not_average = max_force_arr[i]
            # max_force_saved.append(max_force_arr[i])
            i+=1
            max_force /= i
            print("Updating Max Force: ", max_force)
            print("Max Force Array", max_force_arr)
            maxValueStr.set("Average Max Force: " + str(max_force))
        if 0 <= current_progress < 1:
            print("Max Force", max_force)
            if not max_force == 0:
                progressbar.set(current_progress/max_force)
        target_subtact = target - target_range
        target_add = target + target_range
        if not switch.get():
            data = ArduinoSerial.readline().decode('utf-8').strip()
            current_progress = float(data)
            displayVar.set("Current Progress: " + str(abs(current_progress)))
            if target_subtact < current_progress < target_add:
                progressbar.configure(progress_color='#2bf09e', height=35)
                turn_green()
            else:
                progressbar.configure(progress_color='#e3141f', height=35)
                turn_red()
        else:
            progressbar.configure(progress_color='#0362fc')
        # data_saved.append(current_progress)
        # average_saved.append(max_force)
        add_element(csvlist, current_progress, max_force_not_average, max_force)
        header = ['Force Exerted', 'Max Forces', 'Average Max Force']
        with open('data_files/current_data.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames = header)
            writer.writeheader()
            writer.writerows(csvlist)


threading.Thread(target=arduino_handler, daemon=True).start()
app.mainloop()