import tkinter
import customtkinter
import serial
import threading
import time

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
ser = serial.Serial('COM3', 9600)
time.sleep(1)

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x440")

def button_function():
    print("magenta")
    ser.write(b'o')
def turn_green():
    print("green")
    ser.write(b'x')
def turn_blue():
    print("blue")
    ser.write(b'z')
def turn_red():
    print("red")
    ser.write(b'v')
def turn_rainbow():
    print("rainbow")
    ser.write(b'c')
# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="Turn magenta", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
button2 = customtkinter.CTkButton(master=app, text="Turn green", command=turn_green)
button2.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
button3 = customtkinter.CTkButton(master=app, text="Turn rainbow", command=turn_rainbow)
button3.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
button4 = customtkinter.CTkButton(master=app, text="Turn red", command=turn_red)
button4.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
button5 = customtkinter.CTkButton(master=app, text="Turn blue", command=turn_blue)
button5.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
# switch_1 = customtkinter.CTkSwitch(master=app, text="CTkSwitch", onvalue="on", offvalue="off")
# switch_1.pack(padx=20, pady=10)
app.mainloop()