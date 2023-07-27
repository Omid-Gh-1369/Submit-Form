from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class login:
    def __init__(self):
        self.login=Tk()
        
        self.login.title("Login")
        self.login.geometry('400x320')
        self.login.resizable(width=False,height=False)
        self.user=Label(self.login,text="Username",width=15).grid(row=1,column=0)
        self.passw=Label(self.login,text="Password",width=15).grid(row=2,column=0)
        self.userb=Entry(self.login).grid(row=1,column=1)
        self.password=Entry(self.login).grid(row=2,column=1)
        self.checke_log=Checkbutton(self.login,text="I'm Not Robot",onvalue=True,command=self.Verify,width=15).grid(row=3,column=1)
    def Verify(self):
        Button(self.login,text="Login",command=self.click).grid(row=6,column=1)
    def click(self):
        messagebox.showinfo("Notic","Login Successfuly")

class submit:
    def __init__(self):
        self.counter_f=1000
        self.counter_c=0
        self.submit=Tk()
        self.submit.geometry('600x480')
        self.submit.resizable(width=False,height=False)
        self.submit.title("Submit")
        
        Label(self.submit, text="Form No.", width=15).grid(row=1, column=0)
        Label(self.submit, text="Contact No.", width=15).grid(row=2, column=0)
        Label(self.submit, text="Name",width=15).grid(row=3, column=0)
        Label(self.submit, text="Course", width=15).grid(row=4, column=0)
        Label(self.submit, text="Gender", width=15).grid(row=5, column=0)
        Label(self.submit, text="Email id", width=15).grid(row=6, column=0)
        Label(self.submit, text="Address", width=15).grid(row=7, column=0)
 
        self.counter_form=self.c_form()
        self.counter_contact=self.c_contact()
        
        Label(self.submit,text=self.counter_form).grid(row=1, column=1, ipadx="150")
        Label(self.submit,text=self.counter_contact).grid(row=2, column=1, ipadx="150") 
        Entry(self.submit).grid(row=3, column=1, ipadx="150")
        Entry(self.submit).grid(row=4, column=1, ipadx="150")
        ttk.Combobox(self.submit,values=["Male","Female","Other"]).grid(row=5, column=1, ipadx="140")
        Entry(self.submit).grid(row=6, column=1, ipadx="150")
        Entry(self.submit).grid(row=7, column=1, ipadx="150")

        Label(self.submit, text="Verify", width=15).grid(row=8, column=0)
        Checkbutton(self.submit, text="I'm Not Robot", width=15,onvalue=True,command=self.Active).grid(row=8, column=1)
        Label(self.submit,text="Submit").grid(row=10,column=1)
        Button(self.submit,text="Login",command=login).grid(row=11,column=1)

    def c_form(self):
        global counter_f
        self.counter_f +=1
        return self.counter_f
    def c_contact(self):
        global counter_c
        self.counter_c +=1
        return self.counter_c
    def click(self):
        messagebox.showinfo("Notic","SuccessFull Submit...")
    def Active(self):
        Button(self.submit,text="Submit",command=self.click).grid(row=10,column=1)
        
if __name__=="__main__":
    window=Tk()
    Label(window, text="....انتخاب نمایید ",font=("Arabic Typesetting",18),fg="white",bg="gray20",anchor="center").grid()
    Button(window,text="ثبت نام",command=submit,width=15,justify="center",font=("Arabic Typesetting",18),fg="white",bg="gray20").grid()
    Button(window,text="وارد شدن",command=login,width=15,font=("Arabic Typesetting",18),fg="white",bg="gray20").grid()
    window.geometry('400x280')
    window.resizable(width=False,height=False)
    can=Canvas(window,background="gray20",borderwidth=-15)
    can.grid()
    can.create_text((200,100),fill="orange",font=('Chiller',33),text="Create by OMID-GH")
    can.create_line(55, 127,349,127 ,fill='red',width=3,dash=(5,3))
    window.config(bg="gray20")
    window.mainloop()
    
