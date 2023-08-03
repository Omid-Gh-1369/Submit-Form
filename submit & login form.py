from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class login:
    def __init__(self):
        self.login=Tk()
        self.login.config(bg="gray20")
        self.login.title("ورود")
        self.login.geometry('400x300+450+200')
        self.login.resizable(width=False,height=False)
        Label(self.login,text="                             ",bg="gray20").grid(row=0)
        Label(self.login,text="                             ",bg="gray20").grid(row=1)        
        Label(self.login,text="                               ",width=35,bg="gray20").grid(row=2,column=0)
        Label(self.login,text="نام کاربری",width=15,font=("Arabic Typesetting",18),fg="white",bg="gray20").grid(row=2,column=1)
        Entry(self.login,fg="gray10",bg="white",width=15,font=("Arabic Typesetting",18)).grid(row=2,column=0)
        Label(self.login,text="رمز عبور",height=1,width=15,font=("Arabic Typesetting",18),fg="white",bg="gray20").grid(row=3,column=1)
        Entry(self.login,fg="gray10",bg="white",width=15,font=("Arabic Typesetting",18),show="*").grid(row=3,column=0)
        Label(self.login,text="ورود",width=8,font=("Arabic Typesetting",14),bg="gray20",fg="white").grid(row=5,column=0)
        self.checke_log=Checkbutton(self.login,onvalue=1,activebackground="gray20",fg="red",bg="gray20",text="من ربات نیستم",font=("Arabic Typesetting",14),command=self.Verify,width=20,height=4,anchor="s").grid(row=4,column=0)
    def Verify(self):
        Button(self.login,text="ورود",width=8,command=self.click,font=("Arabic Typesetting",14),bg="gray20",fg="white").grid(row=5,column=0)       
    def click(self):
        messagebox.showinfo("پیغام","با موفقیت وارد شدید")
        self.login.destroy()

class submit:
    def __init__(self):
        self.counter_f=1000
        self.counter_c=0
        self.submit=Tk()
        self.submit.geometry('400x300+450+200')
        self.submit.resizable(width=False,height=False)
        self.submit.title("ثبت نام")
        self.submit.config(bg="gray20")
        Label(self.submit, text="", width=3,bg="gray20",fg="white").grid(row=1, column=0)
        Label(self.submit, text="فرم شماره ی ", width=15,font=("Arabic Typesetting",14),bg="gray20",fg="white").grid(row=1, column=2)
        Label(self.submit, text="کاربر شماره ی ", width=15,font=("Arabic Typesetting",14),bg="gray20",fg="white").grid(row=2, column=2)
        Label(self.submit, text="نام",width=15,font=("Arabic Typesetting",14),bg="gray20",fg="white").grid(row=3, column=2)
        Label(self.submit, text="عنوان درس", width=15,font=("Arabic Typesetting",14),bg="gray20",fg="white").grid(row=4, column=2)
        Label(self.submit, text="جنسیت", width=15,font=("Arabic Typesetting",14),bg="gray20",fg="white").grid(row=5, column=2)
        Label(self.submit, text="رایانامه", width=15,font=("Arabic Typesetting",14),bg="gray20",fg="white").grid(row=6, column=2)
        Label(self.submit, text="آدرس", width=15,font=("Arabic Typesetting",14),bg="gray20",fg="white").grid(row=7, column=2)
 
        self.counter_form=self.c_form()
        self.counter_contact=self.c_contact()
        
        Label(self.submit,text=self.counter_form,bg="gray20",fg="white").grid(row=1, column=1, ipadx="70")
        Label(self.submit,text=self.counter_contact,bg="gray20",fg="white").grid(row=2, column=1, ipadx="70") 
        Entry(self.submit,justify="right",fg="gray10",bg="white").grid(row=3, column=1, ipadx="70")
        Entry(self.submit,justify="right",fg="gray10",bg="white").grid(row=4, column=1, ipadx="70")
        Combo=ttk.Combobox(self.submit,justify="right",values=["مرد","زن","غیره"])
        Combo.grid(row=5, column=1, ipadx="61")
        Combo.current(0)
        Combo.configure()
        Entry(self.submit,justify="right",fg="gray10",bg="white").grid(row=6, column=1, ipadx="70")
        Entry(self.submit,justify="right",fg="gray10",bg="white").grid(row=7, column=1, ipadx="70")

        Label(self.submit,bg="gray20",fg="white",font=("Arabic Typesetting",14), text="اعتبار سنجی", width=15).grid(row=8, column=2)
        Checkbutton(self.submit,bg="gray20",fg="red", text="من ربات نیستم",activebackground="gray20",font=("Arabic Typesetting",14), width=15,onvalue=True,command=self.Active).grid(row=8, column=1)
        Label(self.submit,font=("Arabic Typesetting",14),bg="gray20",fg="white",text="ثبت نام").grid(row=10,column=1)
        Button(self.submit,font=("Arabic Typesetting",14),width=8,bg="gray20",fg="white",text="ورود",command=login).grid(row=11,column=1)

    def c_form(self):
        global counter_f
        self.counter_f +=1
        return self.counter_f
    def c_contact(self):
        global counter_c
        self.counter_c +=1
        return self.counter_c
    def click(self):
        messagebox.showinfo("پیغام","با موفقیت ثبت نام انجام شد")
        self.submit.destroy()
    def Active(self):
        Button(self.submit,text="ثبت نام",width=8,font=("Arabic Typesetting",14),command=self.click,bg="gray20",fg="white").grid(row=10,column=1)
        
if __name__=="__main__":
    window=Tk()
    window.title("صفحه نخست")
    Label(window, text="....انتخاب نمایید ",height=2, width=45,font=("Arabic Typesetting",18),fg="white",bg="gray20").grid()
    frame_home=Frame(window)
    frame_home.grid()
    Button(frame_home,text="ثبت نام",command=submit,height=1,width=15,font=("Arabic Typesetting",18),fg="white",bg="gray20").grid()
    Button(frame_home,text="وارد شدن",command=login,height=1,width=15,font=("Arabic Typesetting",18),fg="white",bg="gray20").grid()
    window.geometry('400x300+450+200')
    window.resizable(width=False,height=False)
    can=Canvas(window,background="gray20",borderwidth=-15)
    can.grid()
    can.create_text((180,50),fill="orange",font=('Chiller',33),text="Create by OMID-GH")
    can.create_line(43, 78,322,78 ,fill='red',width=3,dash=(5,3))
    window.config(bg="gray20")
    window.mainloop()
    
