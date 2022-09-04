import tkinter
from tkinter import *
import customtkinter
import serial 
import threading
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("theme.json")
ArduinoSerial = serial.Serial('COM3', 9600)

app = customtkinter.CTk()
app.geometry("1000x700")
app.title("NPRL Force Sensor GUI")
current_progress = 0
target = 0
displayVar = StringVar()
displayVar.set("Current Progress: ")
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
target = 0.1
target_range = 0.1
def button_event():
    global target, target_range
    print("click")
    target = float(entry_target.get())
    target_range = float(entry_range.get())
label_left.grid(row=1, column=0, pady=10, padx=10)
entry_target = customtkinter.CTkEntry(master=frame_left, placeholder_text="Target")
entry_target.grid(row=4, column=0, pady=10, padx=10)
entry_range = customtkinter.CTkEntry(master=frame_left, placeholder_text="Range from target")
entry_range.grid(row=5, column=0, pady=10, padx=10)
button = customtkinter.CTkButton(master=frame_left, text="Submit", command=button_event)
button.grid(row=6, column=0, pady=10, padx=10)

img = ImageTk.PhotoImage(Image.open("NPRL.png"))
img_label = Label(frame_left, image = img, borderwidth=0)
img_label.grid(row=8, column=0, padx=20, pady=20)


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
progressbar.configure(progress_color='#e3141f')

label_info_1 = customtkinter.CTkLabel(master=frame_info,
                                      text="NPRL Force Sensor Output",
                                      height=100,
                                      corner_radius=3,
                                      justify=tkinter.LEFT,
                                      text_font=("Roboto Medium", -16))
label_info_1.grid(column=0, row=0, sticky="we", padx=5, pady=5)
displayLab = Label(frame_info, textvariable=displayVar, background='#333333', fg="white")
displayLab.grid(column=0, row=1, sticky="we", padx=5, pady=5)
progressbar.set(0)

def arduino_handler():
    global current_progress
    while True:
        data = ArduinoSerial.readline().decode('utf-8').strip()
        print(data)
        current_progress = float(data)
        if 0 <= current_progress < 1:
            progressbar.set(current_progress)
        target_subtact = target - target_range
        target_add = target + target_range
        #print(target_subtact)
        #print(target_add)
        if target_subtact < current_progress < target_add:
            progressbar.configure(progress_color='#2bf09e')
        else:
            progressbar.configure(progress_color='#e3141f')
        displayVar.set(str(abs(current_progress)))

threading.Thread(target=arduino_handler, daemon=True).start()
app.mainloop()