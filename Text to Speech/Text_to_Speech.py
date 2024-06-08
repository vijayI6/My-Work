"""
Text to speech is an API cloud service that enables to you turn return written text into real sounding audio and voices
"""
#  pakages needed for this project

import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3  # It is used for text to speech

# Creating user interface
root = tk.Tk()
root.title("Text to Speech Convector")
root.geometry("1000x580+200+80")
root.resizable(False, False)  # for changing the Dimensions
root.configure(bg="#333333")

# Speak Function
tts = pyttsx3.init()


def Speak_Now():
    text = text_box.get(1.0, END)
    gender = gender_box.get()
    speed = speed_box.get()
    voices = tts.getProperty('voices')

    def Select_Voice():
        if gender == 'Male':
            tts.setProperty('voice', voices[0].id)
            tts.say(text)
            tts.runAndWait()
        else:
            tts.setProperty('voice', voices[1].id)
            tts.say(text)
            tts.runAndWait()

    if text:
        if speed == 'Fast':
            tts.setProperty('rate', 250)
            Select_Voice()
        elif speed == 'Medium':
            tts.setProperty('rate', 150)
            Select_Voice()
        else:
            tts.setProperty('rate', 60)
            Select_Voice()


# Setting a logo for Title
logo = tk.PhotoImage(file='C:\\Users\\saivi\\Pictures\\Saved Pictures\\Speech (3).png')
root.iconphoto(False, logo)

# Creating a frame for heading Name
upper_frame = Frame(root, bg="#14A7DD", width=1000, height=100)
upper_frame.place(x=0, y=0)
heading_label = Label(upper_frame, text="Text to Speech Convector", font="TimesNewRoman 40 bold", bg="#14A7DD",
                      fg="black")
heading_label.place(x=170, y=1)

# For textbox to paste the paragraph
text_box = Text(root, font='calibre 20', bg='White', relief=GROOVE, wrap=WORD, bd=10)
text_box.place(x=30, y=110, width=940, height=200)

# For Selecting Voice Label and Combobox
Label(root, text='Select Voice', font='TimesNewRoman 15 bold', bg='#333333', fg='white').place(x=70, y=350)
gender_box = Combobox(root, values=['Male', 'Female'], font='Robote 12', state='r', width=12)
gender_box.place(x=70, y=400)
gender_box.set('Male')

# For Selecting Speed label and Combobox
Label(root, text='Select Speed', font='TimesNewRoman 15 bold', bg='#333333', fg='white').place(x=750, y=350)
speed_box = Combobox(root, values=['Fast', 'Medium', 'Slow'], font='Robote 12', state='r', width=12)
speed_box.place(x=750, y=400)
speed_box.set('Medium')

# For Play Button label
play_button = PhotoImage(file='C:\\Users\\saivi\\Pictures\\Saved Pictures\\Play.png')
play_btn = Button(root, text=' Play', compound=LEFT, image=play_button, bg='white', width=130,
                  font='arial 14 bold', command=Speak_Now
                  )
play_btn.place(x=435, y=475)

root.mainloop()
