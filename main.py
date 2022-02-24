import random
import time
import datetime
from tkinter import *
from tkinter import ttk
import tkinter.messagebox


def main():
    root = Tk()
    app = windows1(root)
    root.mainloop()


class windows1:
    def __init__(self, master):
        self.master = master
        self.master.title('Pharmacy management system')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

        self.Username = StringVar()
        self.Password = StringVar()


        self.LabelTitle = Label(self.frame, text = '     Pharmacy management system    ', font = ('arial',40,'bold'),
                                bd = 10, relief = 'flat')
        self.LabelTitle.grid(row = 0, column = 0, columnspan = 2, pady = 20)

        self.LoginFrame1 = Frame(self.frame, width = 1000, height = 300, bd = 10, relief = 'groove')
        self.LoginFrame1.grid(row = 1, column = 0)

        self.LoginFrame2 = Frame(self.frame, width = 1000, height = 100, bd = 10, relief ='groove')
        self.LoginFrame2.grid(row = 2, column = 0, pady=15)

        self.LoginFrame3 = Frame(self.frame, width = 1000, height = 200, bd = 10, relief = 'flat')
        self.LoginFrame3.grid(row = 6, column = 0, pady = 5)

        self.buttonRegistration = Button(self.LoginFrame3, text ='Patient registration', font = ('arial', 15, 'bold'),
                                         command = self.RegistrationForm, state = DISABLED)
        self.buttonRegistration.grid(row = 0, column = 0, padx = 10, pady = 10)


        self.buttonHospital = Button(self.LoginFrame3, text ='Hospital section', font = ('arial', 15, 'bold'),
                                     command = self.HospitalSection, state = DISABLED)
        self.buttonHospital.grid(row = 0, column = 1, padx = 10, pady = 10)


        self.buttonDoctorSection = Button(self.LoginFrame3, text ='Doctor section', font = ('arial', 15, 'bold'),
                                          command = self.DoctorSection, state = DISABLED)
        self.buttonDoctorSection.grid(row = 1, column = 0, padx = 10, pady = 10)


        self.buttonMedicalStock = Button(self.LoginFrame3, text ='Medicine stock', font = ('arial', 15, 'bold'),
                                         command=self.MedicineStock, state = DISABLED)
        self.buttonMedicalStock.grid(row = 1, column = 1, padx = 10, pady = 10)

        self.LabelUsername = Label(self.LoginFrame1, text = 'Username', font = ('arial', 20, 'bold'), bd = 3)
        self.LabelUsername.grid(row = 0, column = 0)

        self.textUsername = Entry(self.LoginFrame1, font = ('arial', 20), bd = 3, textvariable = self.Username)
        self.textUsername.grid(row = 0, column = 1, padx = 40, pady = 15)

        self.LabelPassword = Label(self.LoginFrame1, text='Password', font=('arial', 20, 'bold'), bd=3)
        self.LabelPassword.grid(row=1, column=0)

        self.textPassword = Entry(self.LoginFrame1, font = ('arial', 20), bd = 3, textvariable = self.Password, show = '*')
        self.textPassword.grid(row = 1, column = 1, padx = 40, pady = 15)

        self.buttonLogin = Button(self.LoginFrame2, text ="Login", width = 20, font = ("arial", 18, "bold"), command = self.LoginForm)
        self.buttonLogin.grid(row = 0, column = 0, padx = 10, pady = 10)

        self.buttonReset = Button(self.LoginFrame2, text ="Reset", width = 20, font = ("arial", 18, "bold"))
        self.buttonReset.grid(row = 0, column = 3, padx = 10, pady = 10)

        self.buttonExit = Button(self.LoginFrame2, text ="Exit", width = 20, font = ("arial", 18, "bold"))
        self.buttonExit.grid(row = 0, column = 6, padx = 10, pady = 10)

    def LoginForm(self):
        user = self.Username.get()
        password = self.Password.get()

        if(user == str('administrator') and (password == str('berina123'))):
            self.buttonRegistration.config(state = NORMAL)
            self.buttonHospital.config(state = NORMAL)
            self.buttonDoctorSection.config(state = NORMAL)
            self.buttonMedicalStock.config(state = NORMAL)
        else:
            tkinter.messagebox.askyesno("Pharmacy management system", "Incorrect username or password")
            self.buttonRegistration.config(state=DISABLED)
            self.buttonHospital.config(state=DISABLED)
            self.buttonDoctorSection.config(state=DISABLED)
            self.buttonMedicalStock.config(state=DISABLED)

            self.Username.set("")
            self.Password.set("")
            self.textUsername.focus

    def RegistrationForm(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows2(self.newWindow)

    def HospitalSection(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows3(self.newWindow)

    def DoctorSection(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows4(self.newWindow)

    def MedicineStock(self):
        self.newWindow = Toplevel(self.master)
        self.app = windows5(self.newWindow)


class windows2:
    def __init__(self, master):
        self.master = master
        self.master.title('Patient management system')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

class windows3:
    def __init__(self, master):
        self.master = master
        self.master.title('Hospital management system')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

class windows4:
    def __init__(self, master):
        self.master = master
        self.master.title('Doctor management system')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

class windows5:
    def __init__(self, master):
        self.master = master
        self.master.title('Medicine system')
        self.master.geometry('1350x750+0+0')
        self.frame = Frame(self.master)
        self.frame.pack()

if __name__ == '__main__':
    main()
