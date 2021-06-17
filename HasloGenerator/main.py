from tkinter import *
from tkinter import messagebox
import random
import os
import clipboard

root = Tk()
root.title("Password Generator")
root.iconphoto(TRUE, PhotoImage(file = "HG.png"))
znaki = []

def GeneratePassword():
    znaki = []
    global IS, IN, LA, UA, AD, e, yourPassword, Save, password
    global gloabls
    if IS.get() == 1:
        pomocnicze = "!@#$%^&*"
        for znak in pomocnicze:
            znaki.append(znak)
    if IN.get() == 1:
        pomocnicze = "123456789"
        for znak in pomocnicze:
            znaki.append(znak)
    if LA.get() == 1:
        pomocnicze = "qwertyuiopasdfghjklzxcvbnm"
        for znak in pomocnicze:
            znaki.append(znak)
    if UA.get() == 1:
        pomocnicze = "QWERTYUIOPASDFGHJKLZXCVBNM"
        for znak in pomocnicze:
            znaki.append(znak)
    if AD.get() == 1:
        pomocnicze = ";:'\",.<>?//{}[]-_=+*()"
        for znak in pomocnicze:
            znaki.append(znak)
    if Save.get() == 1:
        with open('save.txt', 'w') as f:
            for checkBox in gloabls:
                f.write(str(checkBox.get()) + ',')
    checkIfChecked = False
    for checkBox in gloabls:
        if(checkBox.get() == 1):
            checkIfChecked = True
    if(checkIfChecked):
        try:
            dlugosc = int(e.get())
            password = ""
            for i in range(dlugosc):
                password += znaki[random.randint(0, len(znaki) - 1)]
            yourPassword.delete(1.0,END)
            yourPassword.insert(END ,str(password))
            print(len(password))
            if(len(password) < 16):
                yourPassword.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 28, 'bold'))
                yourPassword.config(font=('Tempus Sans ITC', 18, 'bold'), height = 0.7, width = 14)
            else:
                if(len(password) < 64):
                    yourPassword.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 20, 'bold'))
                    yourPassword.config(font=('Tempus Sans ITC', 12, 'bold'), height = 1.5, width = 20)
                else:
                    if(len(password) < 256):
                        yourPassword.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 15, 'bold'))
                        yourPassword.config(font=('Tempus Sans ITC', 10, 'bold'), height = 2, width = 23)
                    else:
                        yourPassword.tag_configure('color',foreground='#476042',font=('Tempus Sans ITC', 10, 'bold'))
                        yourPassword.config(font=('Tempus Sans ITC', 8, 'bold'), height = 2.3, width = 30)
        except:
            messagebox.showerror("Zle dane podane", "Dlugosc musi być liczbą")
    else:
        messagebox.showerror("Musisz wybrać chociaż 1 z opcji", "Opcje wybrać musze bo sie udusze")

def copy():
    try:
        clipboard.copy(password)
    except:
        messagebox.showwarning("Puste okno kopiowania", "Wpierw wygeneruj haslo")

Padding = 15
IS = IntVar()
IncludeSymbols_Text = Label(root, text = "Znaki specjalne :", anchor = W)
IncludeSymbols = Checkbutton(root, text = "(!@#$%^&*)", variable = IS, anchor = W)
IN = IntVar()
IncludeNumbers_Text = Label(root, text = "Liczby :", anchor = W)
IncludeNumbers = Checkbutton(root, text = "(123456789)", variable = IN, anchor = W)
LA = IntVar()
IncludeLA_Text = Label(root, text = "Małe litery alfabetu :", anchor = W)
LowercaseAlphabet = Checkbutton(root, text = "(abcdef...)", variable = LA, anchor = W)
UA = IntVar()
IncludeUA_Text = Label(root, text = "Duże litery alfabetu :", anchor = W)
UppercaseAlphabet = Checkbutton(root, text = "(ABCDEF...)", variable = UA, anchor = W)
AD = IntVar()
IncludeAD_Text = Label(root, text = "Znaki inne :", anchor = W)
AdditionalCharacters = Checkbutton(root, text = "(;:'\",.<>?//{}[]-_=+*())", variable = AD, anchor = W)
Save  = IntVar()
Save_Text = Label(root, text = "Zapisz ustawienia", anchor = W)
SaveThis = Checkbutton(root, text = "Zapisz swoje ustawienia na przyszłość", variable = Save, anchor = W)

e_Text = Label(root, text = "Wpisz długość hasła", font = ("Arial", 15, "bold", "italic"))
e = Entry(root, bd = 2)

generateButoon = Button(root, text = "Generate Password", command = GeneratePassword, height=3, width=25)
yourPassword_Text = Label(root, text = "Your Password :", anchor = W, font = ("Arial", 10, "bold"))
yourPassword = Text(root, height = 2, width = 30)


IncludeSymbols_Text.grid(row = 0, column = 0, sticky=W+E)
IncludeNumbers_Text.grid(row = 1, column = 0, sticky=W+E)
IncludeLA_Text.grid(row = 2, column = 0, sticky=W+E)
IncludeUA_Text.grid(row = 3, column = 0, sticky=W+E)
IncludeAD_Text.grid(row = 4, column = 0, sticky=W+E)
Save_Text.grid(row = 5, column = 0, sticky= W+E)

IncludeSymbols.grid(row = 0, column = 1, sticky=W+E, padx = Padding)
IncludeNumbers.grid(row = 1, column = 1, sticky=W+E, padx = Padding)
LowercaseAlphabet.grid(row = 2, column = 1, sticky=W+E, padx = Padding)
UppercaseAlphabet.grid(row = 3, column = 1, sticky=W+E, padx = Padding)
AdditionalCharacters.grid(row = 4, column = 1, sticky=W+E, padx = Padding)
SaveThis.grid(row = 5, column = 1, sticky=W+E, padx = Padding)

e_Text.grid(row = 6, column = 0, columnspan = 2)
e.grid(row = 7, column = 0, columnspan = 2 ,sticky = W+E, pady = 5 , padx = 10)

generateButoon.grid(row = 8, column =0, columnspan = 2)
yourPassword_Text.grid(row = 9, column =0, sticky = E + W)
yourPassword.grid(row = 9, column = 1, pady = 5 , padx = (10,0))

image = PhotoImage(file = "copy.png")
Copy_Button = Button(root, image = image, command = copy, width = 25, height = 25)
Copy_Button.grid(row = 9, column = 2, padx = (4,4), pady = (2,0))
gloabls = [IS, IN, LA, UA, AD]

if os.path.isfile('save.txt'):
    with open('save.txt', "r") as f:
        preferencs = f.read()
        preferencs = preferencs.split(",")
        preferences = [x for x in preferencs if x.strip()]
        i = 0
        print(preferences)
        for preference in preferences:
            gloabls[i].set(preference)
            i += 1

root.mainloop()
