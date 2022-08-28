from asyncore import write
from csv import writer
from distutils.cmd import Command
from email.mime import image
from fileinput import close
from importlib.resources import path
from tkinter import*
from tkinter import ttk
from tkinter.ttk import Treeview
import pandas as pd

from tkinter import messagebox

####saving records##########

def submit():
    path = 'myData.xlsx'
    df1 = pd.read_excel(path)
    SeriesA =df1['App_name']
    SeriesB = df1['Pswd']

    x = pd.Series(entry1.get())
    y = pd.Series(entry2.get())
    SeriesA = SeriesA.append(x)
    SeriesB = SeriesB.append(y)
    df2 = pd.DataFrame({'App_name':SeriesA, 'Pswd':SeriesB})
    df2.to_excel(path, index=False)
    entry1.delete(0, END)
    entry2.delete(0, END)

def saver():

    new_screen1 = Tk()
    new_screen1.title("Pswd Saver")
    new_screen1.geometry('300x200')
    new_screen1.resizable(False,False)


    def cls():
         new_screen1.destroy()
    #the grid
    new_screen1.config(background='teal')

    lb1 = Label(new_screen1, text='Name of Application', bg='teal', font='Arial 12 bold' )
    lb1.grid(row=1, column=0, padx=5, pady=20)

    lb2 = Label(new_screen1, text='Password', bg='teal', font='Arial 12 bold' )
    lb2.grid(row=2, column=0 , padx=5, pady=5)

    lb3 = Button(new_screen1, text="save", font='Arial 12', command=submit )
    lb3.place(x=100, y=150)

    lb4 = Button(new_screen1, text="exit", command=cls, font='Arial 12' )
    lb4.place(x=160, y=150)
    
    global entry1

    entry1= Entry(new_screen1)
    entry1.grid(row=1, column=1)


    global entry2
    entry2= Entry(new_screen1)
    entry2.grid(row=2, column=1)

    


    new_screen1.mainloop()


   

   

#########code for view records#############
def view():
    new_screen2 = Tk()
    new_screen2.title("Pswd Saver App")

    #the grid
    new_screen2.config(background='teal')
    new_screen2.geometry('500x350')

    my_frame = Frame(new_screen2)
    my_frame.place(x=50, y= 50)

    my_tree = ttk.Treeview(my_frame)

    file_path = 'myData.xlsx'
    df = pd.read_excel(file_path)

  
    
    my_tree["column"] = list(df.columns)
    my_tree["show"] = "headings"

    #looping
    for column in my_tree["column"]:
        my_tree.heading(column, text=column)

    df_row = df.to_numpy().tolist()
    for row in df_row:
        my_tree.insert("","end", values=row)
        print(row)

    my_tree.pack()

    def del_data():
        dx= my_tree.selection()[0]
        print(df(dx))
        df.insert(dx,"")
        print(df)
        # df.drop(idx=dx)
        # write = pd.ExcelWriter(file_path)

        # df.to_excel(writer,'Sheet1')
        # writer.save()
        my_tree.delete(dx)
        print(tuple)
        # df.to_excel(file_path, index=False)
        # dx.replace(r'\W',"deleted")
        
    def clear_tree():
        my_tree.delete(*my_tree.get_children())


    lb_v1 = Label(new_screen2, text="Saved Passwords", font='Arial 12 bold', bg='teal', fg='white')
    lb_v1.place(x=190, y=20)

    bt1_v = Button(new_screen2, text='Delete', command=del_data )
    bt1_v.place(x=160, y=300)
    bt2_v = Button(new_screen2, text='Clear', command= clear_tree )
    bt2_v.place(x=210, y=300)
    bt3_v = Button(new_screen2, text='Close', command= exit )
    bt3_v.place(x=250, y=300)

    new_screen2.mainloop()







def action():
    new_scrn = Tk()
    new_scrn.geometry('300x300')
    new_scrn.resizable(False,False)
    # root.config(background='Gr')
    new_scrn.title('Pswd Saver App')

    frame3 = Frame(new_scrn, width=290, height=290, background="cadet blue", bd=20)
    frame3.place(x=5, y=5)
    frame2 = Frame(new_scrn, width=100, height=100, bg='cadet blue', bd=20)
    frame2.place(x=70, y=90)

   

    lbl = Label(frame3, text="Enter your credential", font='Arial 14 bold')
    lbl.place(x= 30, y= 20)

    btn1 = Button(frame2, text='save new password', command=saver)
    btn1.grid(row=1, column=1, pady=5)
    btn2 = Button(frame2, text='View passwords', command=view)
    btn2.grid(row=2, column=1, pady=5)
    btn3 = Button(frame2, text='Exit', command=exit)
    btn3.grid(row=3, column=1, pady=5)


   
    

    new_scrn.mainloop()


def Login():
    user = str(uzer.get())
    pswd = str(ps.get())
    if (user==str('admin') and pswd == str('password') ):
        
        uzer.delete(0, END)
        ps.delete(0, END)
        action()
    else:
        messagebox.askyesno("Attention", "wrong password")   

    


if __name__=='__main__':
    
    root = Tk()
    root.geometry('925x500+300+200')
    root.resizable(False,False)
    # root.config(background='Gr')
    root.title('Pswd Saver App')

    img= PhotoImage(file='logo.png')
    Label(root, image=img, border=0, ).place(x=20, y=30)

    frame1 = Frame(root, width=350, height=390, background="red", bd=20)
    frame1.place(x=510, y=50)


    uzer = Entry(frame1,width=50, bg='white')
    uzer.place(x=20, y=100)
    uzer.insert(0, 'Insert Username') 
    ps = Entry(frame1, width=50, text='Password', bg='white')
    ps.place(x=20, y= 150)
    ps.insert(0, 'Insert Password')

    lbl1 = Button(frame1, text='Submit', font='Arial 14 bold', command=Login)
    lbl1.place(x=80, y=200)

    lbl2 = Button(frame1, text='exit', font='Arial 14 bold', command=exit)
    lbl2.place(x=190, y=200)
   
   

    root.mainloop()
