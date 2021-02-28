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

window = Tk()
window.title('')

def leap_year(obj):
    '''
    If there is no remainder return This is a leap year else This is not a leap year.
    '''
    if obj % 4 == 0 and obj % 100 != 0:
        return True
    elif obj % 4 == 0 and obj % 100 == 0 and obj % 400 == 0:
        return True
    else:
        return False

def sanitize(obj1,obj2):
    '''
    This function removes the letters in obj2 from obj1 then returns the new obj1
    '''
    sanitized_str = ''
    
    for i in obj1:
        if i in obj2:
            sanitized_str = sanitized_str + i
    return sanitized_str

def size_check(obj, intobj):
    '''
    This function sees if the number of items in obj matches intobj
    '''
    if len(obj) == intobj:
        return True
    else:
        return False

def range_check(obj1, obj2):
    '''
    This function checks that obj1 is in range of obj2[0] and obj[1]
    '''
    if obj1 in range(obj2[0],obj2[1]):
        return True
    else:
        return False
    
def usage():    
    '''
    If there is something wrong with the input print this
    '''

    print('Usage: YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD')

def main():

    if __name__ == "__main__":
       # step 1
    
       
       userDate_get = userDate_entry.get()
       # step 2

       month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                     'Jul','Aug','Sep','Oct','Nov','Dec']
       days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                        7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
       user_raw_data = userDate_get
       
       # step 3
       allow_chars = '0123456789'
       dob = sanitize(user_raw_data, allow_chars)
       sanitizied_label = Label(window,text = 'Sanitized user data:'+ str(dob))
       
       # setp 4
       result = size_check(dob,8)
       if result == False:
           txt = "Error 09: wrong data entered"
       
       # step 5
       year = int(dob[0:4])
       month = int(dob[4:6])
       day = int(dob[6:])
       
       # step 6
       result = range_check(year,(1900,9999))
       if result == False:
           txt = "Error 10: year out of range, must be 1900 or later"
    
       result = range_check(month,(1,12))
       if result == False:
           txt = "Error 02: Wrong month entered"
    
       result = leap_year(year)
       if result == True:
           days_in_month[2] = 29
       result = range_check(day, (1, days_in_month[month]))
       if result == False:
           txt = "Error 03: wrong day entered"
    
       # step 7
       new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
       
       sanitized_label.grid(row = 2, column = 0, padx = 10, pady = 10)
       res_label.grid(row = 3, column = 0, padx = 10, paddy = 10)

userDate_label = Label(window,text = 'Plese enter your date of birth ===>')
userDate_entry = Entry(window)
submit_btn = Button(window,text = 'Submit',width = 20,height = 3, command = main)

userDate_label.grid(row = 0, column = 0, padx = 10, pady = 10)
userDate_entry.grid(row = 0, column = 1, padx = 10, pady = 10)
submit_btn.grid(row = 1, column = 0, padx = 10, pady = 10)