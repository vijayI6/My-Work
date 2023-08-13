from tkinter import *

root = Tk()
root.geometry('395x520')
root.config(bg='black')
root.title('Spoof Calculator')

equation_text = ''
equation_label = StringVar()

frame1 = Frame(root)
label1 = Label(root, textvariable=equation_label, font=('Arial bold', 25))
label1.config(bg='black', width='20', height='5', borderwidth='5')
label1.pack()
frame1.pack()

frame2 = Frame(root)
button1 = Button(frame2, text='AC', height='2', width='8', font=50, bg='grey')
button1.grid(row=0, column=0)

button2 = Button(frame2, text='+/-', height='2', width='8', font=50, bg='grey')
button2.grid(row=0, column=1)

button2 = Button(frame2, text='%', height='2', width='8', font=50, bg='grey')
button2.grid(row=0, column=2)

button3 = Button(frame2, text='÷', height='2', width='8', font=50, bg='orange')
button3.grid(row=0, column=3)

button4 = Button(frame2, text='7', height='2', width='8', font=50)
button4.grid(row=1, column=0)

button5 = Button(frame2, text='8', height='2', width='8', font=50)
button5.grid(row=1, column=1)

button6 = Button(frame2, text='9', height='2', width='8', font=50)
button6.grid(row=1, column=2)

button7 = Button(frame2, text='x', height='2', width='8', font=50, bg='orange')
button7.grid(row=1, column=3)

button8 = Button(frame2, text='4', height='2', width='8', font=50)
button8.grid(row=3, column=0)

button9 = Button(frame2, text='5', height='2', width='8', font=50)
button9.grid(row=3, column=1)

button10 = Button(frame2, text='6', height='2', width='8', font=50)
button10.grid(row=3, column=2)

button11 = Button(frame2, text='-', height='2', width='8', font=50, bg='orange')
button11.grid(row=3, column=3)

button12 = Button(frame2, text='1', height='2', width='8', font=50)
button12.grid(row=4, column=0)

button13 = Button(frame2, text='2', height='2', width='8', font=50)
button13.grid(row=4, column=1)

button14 = Button(frame2, text='3', height='2', width='8', font=50)
button14.grid(row=4, column=2)

button15 = Button(frame2, text='+', height='2', width='8', font=50, bg='orange')
button15.grid(row=4, column=3)
frame2.pack()


frame3 = Frame(root)
button16 = Button(frame3, text='0', height='2', width='17', font=50)
button16.grid(row=0, column=0)

button17 = Button(frame3, text='.', height='2', width='8', font=50)
button17.grid(row=0, column=1)

button18 = Button(frame3, text='=', height='2', width='8', font=50, bg='orange')
button18.grid(row=0, column=2)

frame3.pack()
root.mainloop()
