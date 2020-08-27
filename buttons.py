from tkinter import*
root = Tk()

def getVals():
    print(f"the value of username {uservalue.get()}")
    print(f"the value of password {passvalue.get()}")

root.geometry("655x333")

user = Label(root, text = "Username")
password = Label(root , text = "Password")
user.grid()
password.grid(row = 1)

#variable classes:
#--> BooleanVar
#--> DoubleVar
#--> IntVar
#--> StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable = uservalue)
passentry = Entry(root, textvariable = passvalue)

userentry.grid(row = 0 , column = 1)
passentry.grid(row = 1 , column = 1)

Button(text = "submit" , command = getVals).grid()

root.mainloop()