'''
Set up 2FA with rh, used for first time log in

-- user input username, password, mfa code
-- output otp for user to input into rh
-- save mfa to json file 
'''

from tkinter import *
import robin_stocks.robinhood as rh
import pyotp
import json

root = Tk() #blank root
root.geometry('700x700')
root.configure(bg="black")

userIn = StringVar()
passIn = StringVar()
mfaIn = StringVar()

def auth():

    try:
        totp  = pyotp.TOTP(mfaIn.get()).now()
        print(totp)
        Label(root ,text = 'INPUT CODE TO ROBINHOOD:   '+ totp).grid(row = 5,column = 0)
        #save totp to json
        with open('user.txt', 'w') as out:
            out.write(mfaIn.get())
    except Exception as e:
        print(e)
        Label(root ,text = "Error generating code").grid(row = 5,column = 0)


userLabel = Label(root ,text = "Username").grid(row = 1,column = 0)
passLabel = Label(root ,text = "Password").grid(row = 2,column = 0)
mfaLabel = Label(root ,text = "MFA code").grid(row = 3,column = 0)
userForm = Entry(root, textvariable=userIn).grid(row = 1,column = 1)
passForm = Entry(root, textvariable=passIn, show="*").grid(row = 2,column = 1)
mfaForm = Entry(root, textvariable=mfaIn).grid(row = 3,column = 1)

loginBtn = Button(root, text="generate auth code", command=auth).grid(row=4, column=0)


root.mainloop() #holds view in desktop