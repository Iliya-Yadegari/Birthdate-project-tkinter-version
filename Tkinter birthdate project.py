#!/usr/bin/env python3
'''
Author: "Iliya Yadegari"
The python code in this file (a1_IliyaYadegari.py) is original work written by
"Iliya Yadegari". No code in this file is copied from any other source 
except those provided by the teacher, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading. 
'''
from tkinter import *
import brithdateModule as bm

window = Tk()
window.title('Birth date app')



userDate_label = Label(window,text = 'Plese enter your date of birth ===>')
userDate_entry = Entry(window)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3, command = lambda: bm.main(userDate_entry.get(),window))

userDate_label.grid(row = 0, column = 0, padx = 10, pady = 10)
userDate_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
submit_btn.grid(row = 1, column = 0, padx = 10, pady = 10)

window.mainloop()