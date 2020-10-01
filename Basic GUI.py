from tkinter import *
import tkinter.messagebox as MessageBox
root = Tk()
def validate():
	username1=u_entry.get()
	password1=p_entry.get()
	if(username1=="aditya" and password1=="aadi12345"):
		MessageBox.showinfo(username1,"logged successfully")
	else:
		MessageBox.showinfo(password1,"entered wrong detils")
root.configure(bg="green")
#Now we Want to give the title 
title=Label(root,text="Aditya Login Form",fg="blue",bg="yellow",font=("bold",15))
#Now we want to place the that title on screen
title.place(x=200,y=30)
#Now we want to username and password labels to enter details
username=Label(root,text="username",fg="blue",bg="yellow",font=("bold",12))
#Now we want to place username on screen
username.place(x=100,y=500)
#Now we want to create password on screen
password = Label(root,text="password",fg="blue",bg="yellow",font=("bold",12))
#Now we want to place that password on screen
password.place(x=100,y=700)
#Now we want to create entry button that user want to to enter their username and password
u_entry=Entry()
#Now we want to place that entry button on screen
u_entry.place(x=490,y=500)
#Now we aant to do same for password
p_entry=Entry()
p_entry.place(x=490,y=700)
#Now we want to create submit button
submit=Button(root,text="submit",fg="blue",bg="red",font=("bold",12),comman=validate)
#placing that submit button on the screen
submit.place(x=520,y=800)


root.mainloop()