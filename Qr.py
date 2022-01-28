from tkinter import *

import pyqrcode
from pil import ImageTk


class QR_CODE:

    def __init__(self, root):
        self.root = root
        self.root.title("QR-CODE-GENERATOR  | BY Sarita Bisht")
        self.root.geometry("1000x550+200+50")  ### 200 and 50 are x and y axizs from windo
        self.root.resizable(False, False)  ###SIZE CANT BERESIZE first false is width and second is height
        self.root.config(bg="white")

        title = Label(self.root, text="       QR CODE GENERATOR", font=("Goudy Old Style", 40, "bold"), anchor='w',
                      bg="darkblue",
                      fg="white").place(x=0, y=0, relwidth=1)

        #### EMPLOYEE DETAILS  #############

        emp_Frame = Frame(self.root, bd=3, bg='white', relief=RIDGE)
        emp_Frame.place(x=50, y=100, width=500, height=380)
        emp_Title = Label(emp_Frame, text="DETAILS", font=("Goudy Old Style", 20), bg="darkblue", fg="white").place(x=0,
                                                                                                                    y=0,
                                                                                                                    relwidth=1)

        #################################### VARIABLES ############################
        self.var_NAME = StringVar()
        self.var_EMAIL = StringVar()
        self.var_PHONE = StringVar()

        ######################################   DETAILS #########################################
        NAME_ = Label(emp_Frame, text="Name", font=("times of roman", 20, 'bold'), bg="white", fg="black").place(x=30,
                                                                                                                 y=60)
        E_ID_ = Label(emp_Frame, text="Email ID ", font=("times of roman", 20, 'bold'), bg="white", fg="black").place(
            x=30, y=120)
        PASS_ = Label(emp_Frame, text="Phone No. ", font=("times of roman", 20, 'bold'), bg="white", fg="black").place(
            x=30, y=180)

        ###################################### ENTRY ################################################
        NAME_entry = Entry(emp_Frame, textvariable=self.var_NAME, font=("times of roman", 20, 'bold'), bg="lightyellow",
                           fg="black").place(x=180,
                                             y=60)
        E_ID_entry = Entry(emp_Frame, textvariable=self.var_EMAIL, font=("times of roman", 20, 'bold'),
                           bg="lightyellow", fg="black").place(x=180,
                                                               y=120)
        PASS_entry = Entry(emp_Frame, textvariable=self.var_PHONE, font=("times of roman", 20, 'bold'),
                           bg="lightyellow", fg="black").place(x=180,
                                                               y=180)

        GEN_BUTTON = Button(emp_Frame, text="GENERATE", command=self.generate, font=("times of roman", 20, 'bold'),
                            bg="white",
                            fg="darkblue").place(x=70, y=250, width=180, height=30)
        CLEAR_BUTTON = Button(emp_Frame, text="CLEAR", command=self.clear, font=("times of roman", 20, 'bold'),
                              bg="white",
                              fg="darkblue").place(x=250, y=250, width=180, height=30)

        self.msg = ""

        self.lb_msg = Label(emp_Frame, text=self.msg, font=("times of roman", 20, 'bold'), bg="white", fg="green")
        self.lb_msg.place(
            x=0, y=320, relwidth='1')

        ######################################### QR WINDOW #############################################
        QR_Frame = Frame(self.root, bd=3, bg='white', relief=RIDGE)
        QR_Frame.place(x=600, y=100, width='280', height='380')
        QR_Title = Label(QR_Frame, text="QR-CODE", font=("Goudy Old Style", 20), bg="darkblue", fg="white").place(x=0,
                                                                                                                  y=0,
                                                                                                                  relwidth=1)
        self.txt = Label(QR_Frame, text="No QR\n Available", font=("times of roman", 15, 'bold'), bg="grey",
                         fg="white")
        self.txt.place(
            x=40, y=80, width=180, height=180)

    def clear(self):
        self.var_NAME.set('')
        self.var_EMAIL.set('')
        self.var_PHONE.set('')
        self.msg = ''
        self.lb_msg.config(text=self.msg)

    def generate(self):
        if self.var_NAME.get() == '' or self.var_EMAIL.get() == '' or self.var_PHONE.get() == '':
            self.msg = "All Feilds Are Required !!!!"
            self.lb_msg.config(text=self.msg, fg='red')
        else:
            qr_data = f"NAME:{self.var_NAME.get()}\nEmail:{self.var_EMAIL.get()}\nPHONE_NO.:{self.var_PHONE.get()}"
            qr_code = pyqrcode.create(qr_data)


            qr_code.png('My_QR.png',scale=3.8)    #import png pypi



            self.im = ImageTk.PhotoImage(file='My_QR.png')
            self.txt.config(image=self.im)

            ##################### UPDATING ################################

            self.msg = 'QR Generated Successfully !!!'
            self.lb_msg.config(text=self.msg, fg='green')


root = Tk()
obj = QR_CODE(root)
root.mainloop()
