from cgitb import text
from distutils.log import error
from logging.config import valid_ident
import random
import string
from tkinter import *
from tkinter.font import Font
from typing import List
import pyperclip

# Strings that represent all the characters that can be used to construct a password
lowerCase: str = string.ascii_lowercase
upperCase: str  = string.ascii_uppercase
digits: str  = string.digits
specialChars:str  = "!?@#$%^&*()[]-_+=,."

# Tkinter class used to construct the GUI and create the widgets
class Tkinter():
    def __init__(self, root):
        self.root = root

        # Title and Size of the window
        root.title("PassGen - Password Generator")
        root.geometry("1920x1000")

        self.font = Font(
            family = 'Helvetica',
            size = 20,
            weight = 'bold',
            slant = 'roman',
        )

        self.passGen = Label(root, text = "PASSWORD GENERATOR", font = ('Helvetica',30,'bold'))
        self.passGen.place(relx = 0.4,rely = 0.005)

        self.length = Label(root,text = "Length of password", font = self.font)
        self.length.place(anchor=NW, relx= 0.35, rely = 0.09)

        self.lengthOfPass = Entry(root,bg = "#FBF9FF", font = ("Helvetica",13,"bold"))
        self.lengthOfPass.place(height = 30, width=250,relx = 0.56, rely = 0.095)

        self.customization = Label(root,text="Password includes", font = self.font)
        self.customization.place(anchor=W, relx= 0.35, rely = 0.3)

        self.c1Text = Label(root,text = "Lowercase Letters", font = ("Helvetica",13,"bold"))
        self.c1Text.place(relx = 0.535, rely = 0.24)

        self.c2Text = Label(root,text = "Uppercase Letters", font = ("Helvetica",13,"bold"))
        self.c2Text.place(relx = 0.655, rely = 0.24)

        self.c3Text = Label(root,text = "Numbers", font = ("Helvetica",13,"bold"))
        self.c3Text.place(relx = 0.535, rely = 0.34)

        self.c4Text = Label(root,text = "Special Characters", font = ("Helvetica",13,"bold"))
        self.c4Text.place(relx = 0.655, rely = 0.34)

        self.var1 = IntVar()
        self.c1 = Checkbutton(root, variable=self.var1)
        self.c1.place(relx = 0.52, rely = 0.24)

        self.var2 = IntVar()
        self.c2 = Checkbutton(root, variable=self.var2)
        self.c2.place(relx = 0.64, rely = 0.24)
        
        self.var3 = IntVar()
        self.c3 = Checkbutton(root, variable=self.var3)
        self.c3.place(relx = 0.52, rely = 0.34)

        self.var4 = IntVar()
        self.c4 = Checkbutton(root, variable=self.var4)
        self.c4.place(relx = 0.64, rely = 0.34)

        self.generateBtn = Button(root, fg='#FBF9FF',bg = 'blue',text="GENERATE",command= self.generatePassword ,font = ('Helvetica',12,'bold'), anchor = "center")
        self.generateBtn.place(height = 60, width=200, relx = 0.42, rely = 0.5)

        self.copyBtn = Button(root, fg='#FBF9FF',bg = 'red',text="COPY",command= self.copyPassword ,font = ('Helvetica',12,'bold'), anchor = "center")      
        self.copyBtn.place(height = 60, width=200, relx = 0.55, rely = 0.5)

        self.passwordFrame = LabelFrame(root)
        self.passwordFrame.place(height = 100, width=800, relx = 0.54, rely = 0.7, anchor = "center")

        self.password = Label(self.passwordFrame, font = ("Helvetica",20,"bold"), text = '')
        self.password.place(height = 80, width=700, relx = 0.50, rely = 0.5, anchor = "center")

        self.errorMsg = Label(root, text = '',fg='red',font = ('Helvetica',10,'bold'))
        self.errorMsg.place(relx = 0.45, rely = 0.6)
        self.clickedBoxes = [int(self.var1.get()),int(self.var2.get()),int(self.var3.get()),int(self.var4.get())]


    def validateLength(self):
        toReturn = False
        try:
            passLength = int(self.lengthOfPass.get())
            if( 6 <= passLength <= 32):
                self.errorMsg.config(text = "")
                toReturn = True
            else:
                self.errorMsg.config(text = "*Integer out of Bounds")
        except ValueError:
            self.errorMsg.config(text = "*Please Enter an Integer")

        return toReturn

    def validateChars(self):
        clickedBoxes = [int(self.var1.get()),int(self.var2.get()),int(self.var3.get()),int(self.var4.get())]
        toReturn = False
        if(not(clickedBoxes.count(1) >= 1)):
            self.errorMsg.config(text = "*Please Check Atleast 1 Box")
        else:
            self.errorMsg.config(text = "")
            toReturn = True

        return toReturn 

    def findPossibleChars(self, chars: str, box: List[int]):
        if(box[0] == 1):
            chars += ''.join(lowerCase)
        if(box[1]== 1):
            chars += ''.join(upperCase)    
        if(box[2] == 1):
            chars += ''.join(digits)
        if(box[3]== 1):
            chars += ''.join(specialChars)
        return chars

    def copyPassword(self):
        pyperclip.copy(self.password.cget("text"))

    def generatePassword(self):
        clickedBoxes = [int(self.var1.get()),int(self.var2.get()),int(self.var3.get()),int(self.var4.get())]

        if(self.validateLength() and self.validateChars()):
            includedChars = ""
            passwordLength = int(self.lengthOfPass.get())
            allChars = self.findPossibleChars(includedChars, clickedBoxes) 
            allCharsList = list(allChars)

            passwordList = []
            password = ""
            for i in range(passwordLength):
                passwordList.append(random.choice(allCharsList))
            
            password = password.join(passwordList)
            self.password.config(text=password)

        elif(not self.validateLength()):
            self.validateLength()
        else:
            self.validateChars()
        

if __name__ == "__main__":
    root = Tk()
    Tkinter(root)
    root.mainloop()