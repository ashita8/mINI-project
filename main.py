from tkinter import *

class Application(Frame):

    def __init__(self,master):

        super (Application,self).__init__(master)
        self.task = ""  #future class subclass which have tasks in future
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets() #.grid() is used to register widgets the grid geometry manager
                            # geometry manager manages the placement and layout of the elements of GUI

    def create_widgets(self):
        self.user_Input = Entry(self, bg="#5BC8AC", bd=29,
                                insertwidth=4, width=24,
                                font=("Verdana", 20, "bold"), textvariable = self.UserIn, justify= RIGHT)
        self.user_Input.grid(columnspan=4)

        self.user_Input.insert(0, "0")
        self.button1 = Button(self, bg="#98DBC6", bd=12,
                              text="1", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(1))
        self.button1.grid(row=2, column=0, sticky=W)

        self.button2 = Button(self, bg="#98DBC6", bd=12,
                              text="2", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(2))
        self.button2.grid(row=2, column=1, sticky=W)

        self.button3 = Button(self, bg="#98DBC6", bd=12,
                              text="3", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(3))
        self.button3.grid(row=2, column=2, sticky=W)

        self.button4 = Button(self, bg="#98DBC6", bd=12,
                              text="4", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(4))
        self.button4.grid(row=3, column=0, sticky=W)

        self.button5 = Button(self, bg="#98DBC6", bd=12,
                              text="5", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(5))
        self.button5.grid(row=3, column=1, sticky=W)

        self.button6 = Button(self, bg="#98DBC6", bd=12,
                              text="6", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(6))
        self.button6.grid(row=3, column=2, sticky=W)

        self.button7 = Button(self, bg="#98DBC6", bd=12,
                              text="7", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(7))
        self.button7.grid(row=4, column=0, sticky=W)

        self.button8 = Button(self, bg="#98DBC6", bd=12,
                              text="8", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(8))
        self.button8.grid(row=4, column=1, sticky=W)

        self.button9 = Button(self, bg="#98DBC6", bd=12,
                              text="9", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(9))
        self.button9.grid(row=4, column=2, sticky=W)

        self.button0 = Button(self, bg="#98DBC6", bd=12,
                              text="0", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                              command=lambda: self.buttonClick(0))
        self.button0.grid(row=5, column=0, sticky=W)

        self.addition = Button(self, bg="#98DBC6", bd=12,
                               text="+", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                               command=lambda: self.buttonClick("+"))
        self.addition.grid(row=2, column=3, sticky=W)

        self.Subbutton = Button(self, bg="#98DBC6", bd=12,
                                text="-", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                command=lambda: self.buttonClick("-"))
        self.Subbutton.grid(row=3, column=3, sticky=W)

        self.Multbutton = Button(self, bg="#98DBC6", bd=12,
                                 text="*", padx=33, pady=25, font=("Helvetica", 20, "bold"),
                                 command=lambda: self.buttonClick("*"))
        self.Multbutton.grid(row=4, column=3, sticky=W)

        self.Divbutton = Button(self, bg="#98DBC6", bd=12,
                                text="/", padx=33, pady=25,
                                command= lambda: self.buttonClick("/"), font=("Helvetica", 20, "bold"))
        self.Divbutton.grid(row=5, column=3, sticky=W)


        self.equalbutton = Button(self, bg="#E6D72A", bd=12,
                                  text="=", padx=100, pady=25,
                                  command = self.CalculateTask, font=("Helvetica", 20, "bold"))

        self.equalbutton.grid(row=5, column=1, sticky=W,columnspan = 2)

        self.clearbutton = Button(self, bg="#E6D72A", bd=12,
                                  text="AC",font=("Helvetica", 20, "bold"),width = 28,padx = 7,command = self.ClearDisplay )

        self.clearbutton.grid(row=1, columnspan=4, sticky=W)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def CalculateTask(self):
        self.data = self.user_Input.get()

        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer

        except SyntaxError as e:
            self.displayText("Invald syn")
            self.task = ""

    def displayText(self, value):
        self.user_Input.delete(0, END)
        self.user_Input.insert(0, value)

    def ClearDisplay(self):
        self.task = ""
        self.user_Input.delete(0, END)
        self.user_Input.insert(0, "0")


calculator = Tk()
calculator.title("Calculator")
app= Application(calculator)
calculator.resizable(width= False,height= False)

calculator.mainloop()





