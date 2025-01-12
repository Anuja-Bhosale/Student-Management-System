from tkinter import *
import ttkthemes
from tkinter import ttk,messagebox
from PIL import ImageTk
import pymysql

def exit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

def show_student():
    query = 'select * from Student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        datalist = list(data)
        studentTable.insert('', END, values=datalist)


def update_student():
    def update_data():
        query = 'update Student set Name=%s,Gender=%s,Address=%s,DOB=%s,FY_CPI=%s ,SY_CPI=%s ,TY_CPI=%s,B_TECH_CPI=%s where URN=%s'
        mycursor.execute(query, (nameEntry.get(), genderEntry.get(), addressEntry.get(), dEntry.get(), fEntry.get(), sEntry.get(),
            tEntry.get(),bEntry.get(), idEntry.get()))
        con.commit()
        messagebox.showinfo('SucCess', f'ID {idEntry.get()} is modified successfully', parent=update_window)
        update_window.destroy()
        show_student()

    update_window = Toplevel()
    update_window.title('Update Student')
    update_window.grab_set()
    update_window.resizable(0, 0)
    idLabel = Label(update_window, text='URN:-', font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)
    idEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(update_window, text='Name:-', font=('times new roman', 15, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    genderLabel = Label(update_window, text='Gender:-', font=('times new roman', 15, 'bold'))
    genderLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    genderEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=2, column=1, pady=15, padx=10)

    addressLabel = Label(update_window, text='Address:-', font=('times new roman', 15, 'bold'))
    addressLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    addressEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=3, column=1, pady=15, padx=10)

    dLabel = Label(update_window, text='DOB:-', font=('times new roman', 15, 'bold'))
    dLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    dEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    dEntry.grid(row=4, column=1, pady=15, padx=10)

    fLabel = Label(update_window, text='FY CPI:-', font=('times new roman', 15, 'bold'))
    fLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    fEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    fEntry.grid(row=5, column=1, pady=15, padx=10)

    sLabel = Label(update_window, text='SY CPI:-', font=('times new roman', 15, 'bold'))
    sLabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    sEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    sEntry.grid(row=6, column=1, pady=15, padx=10)

    tLabel = Label(update_window, text='TY CPI:-', font=('times new roman', 15, 'bold'))
    tLabel.grid(row=7, column=0, padx=20, pady=15, sticky=W)
    tEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    tEntry.grid(row=7, column=1, pady=15, padx=10)

    bLabel = Label(update_window, text='B_TECH:-', font=('times new roman', 15, 'bold'))
    bLabel.grid(row=8, column=0, padx=20, pady=15, sticky=W)
    bEntry = Entry(update_window, font=('roman', 15, 'bold'), width=24)
    bEntry.grid(row=8, column=1, pady=15, padx=10)

    update_student_button = ttk.Button(update_window, text='Update', command=update_data)
    update_student_button.grid(row=9, columnspan=2, pady=15)

    indexing = studentTable.focus()
    content = studentTable.item(indexing)
    listdata = content['values']
    idEntry.insert(0, listdata[0])
    nameEntry.insert(0, listdata[1])
    genderEntry.insert(0, listdata[2])
    addressEntry.insert(0, listdata[3])
    dEntry.insert(0, listdata[4])
    fEntry.insert(0, listdata[5])
    sEntry.insert(0, listdata[6])
    tEntry.insert(0, listdata[7])
    bEntry.insert(0, listdata[8])





def delete_student():
    indexing = studentTable.focus()
    print(indexing)
    content = studentTable.item(indexing)
    content_id = content['values'][0]
    query = 'delete from student where URN=%s'
    mycursor.execute(query, content_id)
    con.commit()
    messagebox.showinfo('Deleted', f'This {content_id} is deleted successfully')
    query = 'select * from Student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        datalist = list(data)
        studentTable.insert('', END, values=datalist)



def search_student():
    def search_data():
        query = 'select *from Student where URN=%s or Name=%s or Gender=%s or Address=%s or DOB=%s or FY_CPI=%s or SY_CPI=%s or TY_CPI=%s or B_TECH_CPI=%s'
        mycursor.execute(query, (
            idEntry.get(), nameEntry.get(), genderEntry.get(), addressEntry.get(), dEntry.get(), fEntry.get(),
            sEntry.get(),
            tEntry.get(), bEntry.get()))
        studentTable.delete(*studentTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            datalist = list(data)
            studentTable.insert('', END, values=datalist)

    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set()
    search_window.resizable(0, 0)
    idLabel = Label(search_window, text='URN:-', font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)
    idEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(search_window, text='Name:-', font=('times new roman', 15, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    genderLabel = Label(search_window, text='Gender:-', font=('times new roman', 15, 'bold'))
    genderLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    genderEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=2, column=1, pady=15, padx=10)

    addressLabel = Label(search_window, text='Address:-', font=('times new roman', 15, 'bold'))
    addressLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    addressEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=3, column=1, pady=15, padx=10)

    dLabel = Label(search_window, text='DOB:-', font=('times new roman', 15, 'bold'))
    dLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    dEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    dEntry.grid(row=4, column=1, pady=15, padx=10)

    fLabel = Label(search_window, text='FY CPI:-', font=('times new roman', 15, 'bold'))
    fLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    fEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    fEntry.grid(row=5, column=1, pady=15, padx=10)

    sLabel = Label(search_window, text='SY CPI:-', font=('times new roman', 15, 'bold'))
    sLabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    sEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    sEntry.grid(row=6, column=1, pady=15, padx=10)

    tLabel = Label(search_window, text='TY CPI:-', font=('times new roman', 15, 'bold'))
    tLabel.grid(row=7, column=0, padx=20, pady=15, sticky=W)
    tEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    tEntry.grid(row=7, column=1, pady=15, padx=10)

    bLabel = Label(search_window, text='B_TECH:-', font=('times new roman', 15, 'bold'))
    bLabel.grid(row=8, column=0, padx=20, pady=15, sticky=W)
    bEntry = Entry(search_window, font=('roman', 15, 'bold'), width=24)
    bEntry.grid(row=8, column=1, pady=15, padx=10)

    search_student_button = ttk.Button(search_window, text='Search', command=search_data)
    search_student_button.grid(row=9, columnspan=2, pady=15)


def add_student():
    def add_data():

        if idEntry.get() == '' or nameEntry.get() == '' or genderEntry.get() == '' or addressEntry.get() == '' or dEntry.get() == '' or fEntry.get() == '' or sEntry.get() == '' or tEntry.get() == '' or bEntry.get() == '':
            messagebox.showerror('Error', 'All Feilds are required', parent=add_window)

        else:
            try:

                query = 'insert into Student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query, (
                    idEntry.get(), nameEntry.get(), genderEntry.get(), addressEntry.get(), dEntry.get(), fEntry.get(),
                    sEntry.get(), tEntry.get(), bEntry.get()))
                con.commit()
                result = messagebox.askyesno('Confirm', 'Data added successfully.Do you want to clean the form?',
                                             parent=add_window)
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    dEntry.delete(0, END)
                    fEntry.delete(0, END)
                    sEntry.delete(0, END)
                    tEntry.delete(0, END)
                    bEntry.delete(0, END)
                else:
                    pass
            except:
                messagebox.showerror('Error', 'Id cannot be repeated', parent=add_window)
                return

            query = 'select *from Student'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                datalist = list(data)
                studentTable.insert('', END, values=datalist)

    add_window = Toplevel()
    add_window.title('Search Student')
    add_window.grab_set()
    add_window.resizable(0, 0)
    idLabel = Label(add_window, text='URN:-', font=('times new roman', 15, 'bold'))
    idLabel.grid(row=0, column=0, padx=20, pady=15, sticky=W)
    idEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(add_window, text='Name:-', font=('times new roman', 15, 'bold'))
    nameLabel.grid(row=1, column=0, padx=20, pady=15, sticky=W)
    nameEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    genderLabel = Label(add_window, text='Gender:-', font=('times new roman', 15, 'bold'))
    genderLabel.grid(row=2, column=0, padx=20, pady=15, sticky=W)
    genderEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=2, column=1, pady=15, padx=10)

    addressLabel = Label(add_window, text='Address:-', font=('times new roman', 15, 'bold'))
    addressLabel.grid(row=3, column=0, padx=20, pady=15, sticky=W)
    addressEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=3, column=1, pady=15, padx=10)

    dLabel = Label(add_window, text='DOB:-', font=('times new roman', 15, 'bold'))
    dLabel.grid(row=4, column=0, padx=20, pady=15, sticky=W)
    dEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    dEntry.grid(row=4, column=1, pady=15, padx=10)

    fLabel = Label(add_window, text='FY CPI:-', font=('times new roman', 15, 'bold'))
    fLabel.grid(row=5, column=0, padx=20, pady=15, sticky=W)
    fEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    fEntry.grid(row=5, column=1, pady=15, padx=10)

    sLabel = Label(add_window, text='SY CPI:-', font=('times new roman', 15, 'bold'))
    sLabel.grid(row=6, column=0, padx=20, pady=15, sticky=W)
    sEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    sEntry.grid(row=6, column=1, pady=15, padx=10)

    tLabel = Label(add_window, text='TY CPI:-', font=('times new roman', 15, 'bold'))
    tLabel.grid(row=7, column=0, padx=20, pady=15, sticky=W)
    tEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    tEntry.grid(row=7, column=1, pady=15, padx=10)

    bLabel = Label(add_window, text='B_TECH:-', font=('times new roman', 15, 'bold'))
    bLabel.grid(row=8, column=0, padx=20, pady=15, sticky=W)
    bEntry = Entry(add_window, font=('roman', 15, 'bold'), width=24)
    bEntry.grid(row=8, column=1, pady=15, padx=10)

    add_student_button = ttk.Button(add_window, text='Add student', command=add_data)
    add_student_button.grid(row=9, columnspan=2, pady=15)




def connect_database():
    def connect():
        global mycursor,con
        try:
            con = pymysql.connect(host=hostEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
            mycursor = con.cursor()

        except:
            messagebox.showerror('Error','Invalid Details',parent=connectWindow)
            return
        try:
            query = 'create database studentanagementsystem'
            mycursor.execute(query)
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
            query='create table Student(URN int not null primary key,Name Varchar(60),Gender Varchar(30),Address Varchar(30),D.O.B Varchar(20),FY_CPI double,SY_CPI double,TY_CPI double,B-Tech_CPI double)'
            mycursor.execute(query)
        except:
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Success','Database Connection is Successful',parent=connectWindow)
        connectWindow.destroy()
        addStudentButton.config(state=NORMAL)
        searchStudentButton.config(state=NORMAL)
        deleteStudentButton.config(state=NORMAL)
        updateStudentButton.config(state=NORMAL)
        showStudentButton.config(state=NORMAL)





    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0,0)

    hostnameLabel=Label(connectWindow,text='Host Name',font=('arial',15,'bold'))
    hostnameLabel.grid(row=0,column=0,padx=20)

    hostEntry=Entry(connectWindow,font=('roman',15,'bold'),bd=2)
    hostEntry.grid(row=0,column=1,padx=40,pady=20)

    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 15, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 15, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    connectButton=ttk.Button(connectWindow,text='CONNECT',command=connect)
    connectButton.grid(row=3,columnspan=2)

count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text=text+s[count] #S
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(1000,slider)

#GUI Part
root=ttkthemes.ThemedTk()
root.get_themes()

root.set_theme('radiance')
root.geometry('1455x860+50+20')
root.resizable(0,0)
root.title('Student Management System')


s='Student Management System'
sliderLabel=Label(root,font=('arial',28,'italic bold'),width=30)
sliderLabel.place(x=400,y=0)
slider()

connectButton=ttk.Button(root,text='Connect database',command=connect_database)
connectButton.place(x=1200,y=0)

leftFrame=Frame(root)
leftFrame.place(x=50,y=80,width=300,height=600)

logo_image=ImageTk.PhotoImage(file='Student.jpg')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0)
logo_Label=Label(leftFrame)

addStudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=add_student)
addStudentButton.grid(row=1,column=0,pady=20)

searchStudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=search_student)
searchStudentButton.grid(row=2,column=0,pady=20)

deleteStudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deleteStudentButton.grid(row=3,column=0,pady=20)

updateStudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=update_student)
updateStudentButton.grid(row=4,column=0,pady=20)

showStudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showStudentButton.grid(row=5,column=0,pady=20)

exitStudentButton=ttk.Button(leftFrame,text='Exit Student',width=25,command=exit)
exitStudentButton.grid(row=6,column=0,pady=20)

rightFrame=Frame(root)
rightFrame.place(x=350,y=80,width=1020,height=650)
scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
studentTable=ttk.Treeview(rightFrame,columns=('URN','Name','Gender','Address','D.O.B','FY CPI','SY CPI','TY CPI','B-TECH CPI')
                          ,xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('URN',text='URN')
studentTable.heading('Name',text='Name')
studentTable.heading('Gender',text='Gender')
studentTable.heading('Address',text='Address')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('FY CPI',text='FY CPI')
studentTable.heading('SY CPI',text='SY CPI')
studentTable.heading('TY CPI',text='TY CPI')
studentTable.heading('B-TECH CPI',text='B-TECH CPI')

studentTable.column('URN',width=200,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('D.O.B',width=200,anchor=CENTER)
studentTable.column('FY CPI',width=100,anchor=CENTER)
studentTable.column('SY CPI',width=100,anchor=CENTER)
studentTable.column('TY CPI',width=100,anchor=CENTER)
studentTable.column('B-TECH CPI',width=100,anchor=CENTER)

style=ttk.Style()
style.configure('Treeview',rowheight=40,font=('arial',12,'bold'))

studentTable.config(show='headings')


root.mainloop()