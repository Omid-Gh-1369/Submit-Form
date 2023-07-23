#!/usr/bin/env python
# coding: utf-8

# In[33]:


import tkinter as tk
from tkinter import ttk

class login:
    def __init__(self):
        self.login=tk.Tk()
        self.login.title("Login")
        self.login.minsize(250,100)
        self.user=ttk.Label(self.login,text="Username")
        self.passw=ttk.Label(self.login,text="Password")
        self.userb=ttk.Entry(self.login)
        self.password=ttk.Entry(self.login)
        self.user.grid(row=3,column=1)
        self.passw.grid(row=4,column=1)
        self.userb.grid(row=3,column=2)
        self.password.grid(row=4,column=2)
        self.checke_log=ttk.Checkbutton(self.login,text="I'm Not Robot",command=self.Verify)
        self.checke_log.grid(row=5,column=2)
    def Verify(self):
        self.act=ttk.Button(self.login,text="Login",command=self.click)
        self.act.grid(row=6,column=2)
    def click(self):
        self.msg=tk.Tk()
        self.msg.title("Login Success Full")
        self.label=ttk.Label(self.msg,text="Login Success Full")
        self.label.grid()
        self.bou=ttk.Button(self.msg,text="OK",command=self.msg.destroy)
        self.msg.configure(width=100)
        self.bou.grid()
class submit:
    def __init__(self):
        self.submit=tk.Tk()
        self.submit.minsize(600,400)
        self.submit.title("Submit")
        self.form_no =ttk.Label(self.submit, text="Form No.", width=15)
        self.contact_no =ttk.Label(self.submit, text="Contact No.", width=15)
        self.name =ttk.Label(self.submit, text="Name",width=15)
        self.course =ttk.Label(self.submit, text="Course", width=15)
        self.gender =ttk.Label(self.submit, text="Gender", width=15)
        self.email_id =ttk.Label(self.submit, text="Email id", width=15)
        self.address =ttk.Label(self.submit, text="Address", width=15)
        self.form_no.grid(row=1, column=0)
        self.contact_no.grid(row=2, column=0)
        self.name.grid(row=3, column=0)
        self.course.grid(row=4, column=0)
        self.gender.grid(row=5, column=0)
        self.email_id.grid(row=6, column=0)
        self.address.grid(row=7, column=0)
        self.form_no_field =ttk.Entry(self.submit)
        self.contact_no_field =ttk.Entry(self.submit)
        self.name_field =ttk.Entry(self.submit)
        self.course_field =ttk.Entry(self.submit)
        self.gender_field = ttk.Combobox(self.submit,values=["Male","Female","Other"])
        self.email_id_field =ttk.Entry(self.submit)
        self.address_field =ttk.Entry(self.submit)
        self.form_no_field.grid(row=1, column=1, ipadx="150")
        self.contact_no_field.grid(row=2, column=1, ipadx="150")
        self.name_field.grid(row=3, column=1, ipadx="150")
        self.course_field.grid(row=4, column=1, ipadx="150")
        self.gender_field.grid(row=5, column=1, ipadx="140")
        self.email_id_field.grid(row=6, column=1, ipadx="150")
        self.address_field.grid(row=7, column=1, ipadx="150")
        self.check=ttk.Label(self.submit, text="Verify", width=15)
        self.check.grid(row=8, column=0)
        self.checke=ttk.Checkbutton(self.submit, text="I'm Not Robot", width=15,onvalue=0,offvalue=1,command=self.Active)
        self.checke.grid(row=8, column=1)
        self.button_sub=ttk.Label(self.submit,text="Submit")
        self.button_sub.grid(row=10,column=1)
        self.button_log=ttk.Button(self.submit,text="Login",command=login)
        self.button_log.grid(row=11,column=1)
    def click(self):
        self.msg=tk.Message(self.submit,text="SuccessFull Submit...")
        self.msg.configure(width=150)
        self.msg.grid()
    def Active(self):
        self.act=ttk.Button(self.submit,text="Submit",command=self.click)
        self.act.grid(row=10,column=1)
        
if __name__=="__main__":
    window=tk.Tk()
    window.minsize(400,200)
    enter_info1 =tk.Label(window, text="")
    enter_info1.grid(row=0, column=0)
    enter_info2=tk.Label(window, text="")
    enter_info2.grid(row=1, column=1)
    enter_info3=tk.Label(window, text="")
    enter_info3.grid(row=3, column=2)
    enter_info4=tk.Label(window, text="Please Select : ")
    enter_info4.grid(row=2, column=3)
    bot_sub=tk.Button(window,text="Submit",command=submit,width=15,justify="center")
    bot_log=tk.Button(window,text="Login",command=login,width=15)
    bot_sub.grid(row=4,column=3)
    bot_log.grid(row=5,column=3)
    window.mainloop()
    


# In[ ]:




