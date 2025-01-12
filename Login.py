from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='Student' and passwordEntry.get()=='2022':

        messagebox.showinfo('Success','Welcome')
        window.destroy()
        import First

    else:

        messagebox.showerror('Error','Please enter correct credentials')

window=Tk()

window.geometry('1530x800+0+0')
window.title('Login System of Student Management System')
window.resizable(False,False)




loginFrame=Frame(window,bg='yellow')
loginFrame.place(x=500,y=200)
logoImage=ImageTk.PhotoImage(file='Logo.jpg')

logoLabel=Label(loginFrame,image=logoImage)

logoLabel.grid(row=0,column=0,columnspan=2, pady=10)
usernameImage=ImageTk.PhotoImage(file='user.jpg')
usernameLabel=Label(loginFrame,image=usernameImage, text='Username', compound=LEFT,font=('times new roman', 20, 'bold'))
usernameLabel.grid(row=1,column=0,pady=10,padx=20)
usernameEntry=Entry(loginFrame,font=('times new roman', 20,'bold'),bd=5,fg='royalblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

passwordImage=ImageTk.PhotoImage(file='Password.jpg')
passwordLabel=Label(loginFrame,image=passwordImage, text='Password', compound=LEFT,font=('times new roman', 20, 'bold'))
passwordLabel.grid(row=2,column=0,pady=10,padx=20)
passwordEntry=Entry(loginFrame,font=('times new roman', 20,'bold'),bd=5,fg='royalblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton=Button(loginFrame,text='Login',font=('times new roman', 16,'bold'),width=15,fg='white',bg='cornflowerblue'
                   ,activebackground='cornflowerblue',activeforeground='white',cursor='hand2',command=login)
loginButton.grid(row=3,column=1,pady=15)
window.mainloop()