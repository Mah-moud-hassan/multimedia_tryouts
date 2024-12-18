# from tkinter import *

# myframe=Tk()
# myframe.title('GUI')
# myframe.geometry('1000x500')
# myframe.mainloop()

############################

# from tkinter import *
# import webbrowser

# myframe=Tk()
# myframe.title("my app")
# myframe.geometry("500x300")
# myframe.mainloop()

############################

# from tkinter import *
# import webbrowser

# myframe=Tk()
# mybutton=Button(myframe,text="Cleck Me" , fg="blue" , bg="yellow" ,
#                  font= "Helvatica 10 bold" , width=10 , height=10)
# mybutton.pack()
# myframe.mainloop()

#######################################################################

# from tkinter import *
# import webbrowser

# def myfunc():
#     webbrowser.open("https://www.google.com.eg/")

# myframe=Tk()
# mybutton=Button(myframe,text="GO TO Link" , fg="blue" , bg="yellow" ,
#                 font= "Helvatica 10 bold" , padx=10 , pady=3  
#                 , command=myfunc)

# mybutton.pack()
# myframe.mainloop()

#########################################################################

# from tkinter import *
# import webbrowser

# def myfunc():
#     webbrowser.open("https://www.google.com.eg/")

# myframe=Tk()

# mylabel=Label(myframe,text="Web Browser" , font="Tahoma 30 bold")
# mylabel.pack(pady=30)

# mybutton=Button(myframe,text="GO TO Link" , fg="blue" , bg="yellow" ,
#                 font= "Helvatica 10 bold" , padx=10 , pady=3  
#                 , command=myfunc)
# mybutton.pack()

# myframe.mainloop()

########################################################################

# from tkinter import *
# import webbrowser

# def myfunc():
#     link=mytext.get()
#     webbrowser.open(link)

# myframe=Tk()

# mylabel=Label(myframe,text="Web Browser" , font="Tahoma 30 bold")
# mylabel.pack(pady=30)

# mytext=Entry(myframe,width=50)
# mytext.pack(pady=10)

# mybutton=Button(myframe,text="GO TO Link" , fg="blue" , bg="yellow" ,
#                 font= "Helvatica 10 bold" , padx=10 , pady=3  
#                 , command=myfunc)
# mybutton.pack()

# myframe.mainloop()

###########################################################################

# from tkinter import *

# root=Tk()
# root.geometry("300x300")
# mybutton=Button(root , text="My Button")

# mybutton.pack(side=LEFT , padx=10 ,pady=20,
#               anchor="nw")

# m=Entry(root,width=30)
# m.pack(side=LEFT , padx=10 ,pady=20, anchor="nw",
#        ipady=5 , fill=X, expand=True)

# root.mainloop()

##########################################################

# from tkinter import *

# root = Tk()
# root.geometry("200x200")

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=0)

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=1)

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0)

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1)

# root.mainloop()

##########################################################

# from tkinter import *

# root = Tk()
# root.geometry("400x200")

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=2)

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=3)

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0)

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1)

# root.mainloop()

##################################################

# from tkinter import *

# root = Tk()
# root.geometry("400x200")

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=0)

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=1)

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0)

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1)

# button5 = Button(root ,text="Button5")
# button5.grid(row=2 , column=0 , columnspan=2)

# root.mainloop()

##################################################

# from tkinter import *

# root = Tk()
# root.geometry("400x200")

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=0)

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=1)

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0)

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1)

# button5 = Button(root ,text="Button5")
# button5.grid(row=0 , column=2 , rowspan=2)

# root.mainloop()

##################################################

# from tkinter import *

# root = Tk()
# root.geometry("400x200")

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=0 , padx=10 , pady=10)

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=1 , padx=10 , pady=10)

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0 , padx=10 , pady=10)

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1 , padx=10 , pady=10)

# button5 = Button(root ,text="Button5")
# button5.grid(row=2 , column=0 , columnspan=2
# , padx=10 , pady=10)

# root.mainloop()

##########################################################

# from tkinter import *

# root = Tk()
# root.geometry("400x200")

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=0 , padx=10 , pady=10)

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=1 , padx=10 , pady=10)

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0 , padx=10 , pady=10)

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1 , padx=10 , pady=10)

# button5 = Button(root ,text="Button5")
# button5.grid(row=2 , column=0 , columnspan=2
# , padx=10 , pady=10 , ipadx=10)

# root.mainloop()

##########################################################

# from tkinter import *

# root = Tk()
# root.geometry("400x200")

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=0 , padx=10 , pady=10)

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=1 , padx=10 , pady=10)

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0 , padx=10 , pady=10)

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1 , padx=10 , pady=10)

# button5 = Button(root ,text="Button5")
# button5.grid(row=2 , column=0 , columnspan=2
# , padx=10 , pady=10 , ipadx=10 , sticky="w")

# root.mainloop()

##########################################################

# from tkinter import *

# root = Tk()
# root.geometry("400x200")

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=0 , padx=10 , pady=10)

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=1 , padx=10 , pady=10)

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0 , padx=10 , pady=10)

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1 , padx=10 , pady=10)

# button5 = Button(root ,text="Button5")
# button5.grid(row=2 , column=0 , columnspan=2
# , padx=10 , pady=10 , ipadx=10 , sticky="we")

# root.mainloop()

##########################################################

# from tkinter import *

# root = Tk()
# root.geometry("400x200")
# root.rowconfigure(0 , weight=1)
# root.rowconfigure(1 , weight=2)

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=0 , padx=10 , pady=10)

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=1 , padx=10 , pady=10)

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0 , padx=10 , pady=10)

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1 , padx=10 , pady=10)

# button5 = Button(root ,text="Button5")
# button5.grid(row=2 , column=0 , columnspan=2
# , padx=10 , pady=10 , ipadx=10 , sticky="we")

# root.mainloop()

######################################################

# from tkinter import *

# root = Tk()
# root.geometry("400x200")
# root.rowconfigure(0 , weight=1)
# root.rowconfigure(1 , weight=2)
# root.rowconfigure(1 , weight=1)

# button1 = Button(root ,text="Button1")
# button1.grid(row=0 , column=0 , padx=10 , pady=10 , sticky="ns")

# button2 = Button(root ,text="Button2")
# button2.grid(row=0 , column=1 , padx=10 , pady=10 , sticky="nw")

# button3 = Button(root ,text="Button3")
# button3.grid(row=1 , column=0 , padx=10 , pady=10 , sticky="ns")

# button4 = Button(root ,text="Button4")
# button4.grid(row=1 , column=1 , padx=10 , pady=10 , sticky="we")

# button5 = Button(root ,text="Button5")
# button5.grid(row=2 , column=0 , columnspan=2
# , padx=10 , pady=10 , ipadx=10 , sticky="we")

# root.mainloop()

####################################################################

# from tkinter import *
# root=Tk()

# button1 =Button(root , text=" button 1") .pack()

# root.mainloop()

#####################################################################

# from tkinter import *
# from tkinter import ttk

# root=Tk()

# button1 =Button(root , text=" button 1") .pack(pady=10)

# button2 =ttk.Button(root , text=" button 2") .pack(pady=10)

# button3 =Radiobutton(root , text=" option 1") .pack(pady=10)

# button4 =ttk.Radiobutton(root , text=" option 2") .pack(pady=10)

# root.mainloop()

############################################################################

# from tkinter import *
# from tkinter import ttk

# root=Tk()

# button1 =Button(root , text=" button 1" ,bg="red") .pack(pady=10)

# button2 =ttk.Button(root , text=" button 2") .pack(pady=10)

# root.mainloop()

############################################################################

# from tkinter import *
# from tkinter import ttk

# root=Tk()

# button1 =Button(root , text=" button 1" ,bg="red") .pack()

# button2 =ttk.Button(root , text=" button 2") .pack()

# button3 =Radiobutton(root , text=" option 1") .pack(pady=10)

# button4 =ttk.Radiobutton(root , text=" option 2") .pack(pady=10)

# mylist = ttk.Combobox(root , values=['python' , 'AI' , 'ML']).pack()

# root.mainloop()

#######################################################################

# from tkinter import *
# from tkinter import ttk
# from tkinter import filedialog
# from tkinter import messagebox

# def hello():
#     messagebox.showerror(titel="hello" ,
#                           message="hello" + myentry.get())
    
# def myfile():
#     myfl=filedialog.askopenfilename(titel="open your file")
#     myentry.insert(0,myfl)

# root=Tk()

# button =ttk.Button(root , text=" button " ,command=hello) .pack()

# myentry=ttk.Entry(root)
# myentry.pack()
# root.mainloop()

#########################################################################