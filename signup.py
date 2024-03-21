from tkinter import *
from tkinter import messagebox
import psycopg2
from psycopg2 import Error
import signin as connect1

def run_signup():
    window=Tk()
    window.title('Sign Up')
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)

    def signin_window():
        window.destroy()
        connect1.run_signin()

    def signup():
        username=user.get()
        password=code.get()
        confirm_password=confirm_code.get()
        
        if password==confirm_password:
            try:
                connection=psycopg2.connect(
                    dbname="firstTry",
                    user="postgres",
                    password="admin",
                    host="localhost",
                    port="5432"
                )
                cursor=connection.cursor()
                cursor.execute("insert into details(username,password) values(%s,%s)",(username,password))
                connection.commit()
                messagebox.showinfo('Success', 'Account created successfully')
            
                # Close cursor and connection
                cursor.close()
                connection.close()

            except Error as error:
                # Check if the error is due to a duplicate username (UniqueViolation)
                if isinstance(error, psycopg2.errors.UniqueViolation):
                    messagebox.showerror('Error', 'Username already exists')
                else:
                    # Other database errors
                    messagebox.showerror('Error', f'Failed to create account: {error}')
        else:
            messagebox.showerror("Invalid","Password didn't matched")


    img=PhotoImage(file="signup.png")
    Label(window,image=img,border=0,bg='white').place(x=50,y=90)

    frame=Frame(window,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)

    heading=Label(frame,text='Sign Up',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Ligth',23,'bold'))
    heading.place(x=100,y=5)

    ##############
    def user_on_enter(e):
        user.delete(0,'end')
    def user_on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Ligth',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",user_on_enter)
    user.bind("<FocusOut>",user_on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    ##############
    def code_on_enter(e):
        code.delete(0,'end')
    def code_on_leave(e):
        if code.get()=='':
            code.insert(0,'Password')
    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Ligth',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>',code_on_enter)
    code.bind('<FocusOut>',code_on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    ##############
    def confirm_on_enter(e):
        confirm_code.delete(0,'end')
    def confirm_on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0,'Confirm Password')
    confirm_code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Ligth',11))
    confirm_code.place(x=30,y=220)
    confirm_code.insert(0,'Confirm Password')
    confirm_code.bind('<FocusIn>',confirm_on_enter)
    confirm_code.bind('<FocusOut>',confirm_on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    ################
    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',cursor='hand2',border=0,command=signup).place(x=35,y=280)
    label=Label(frame,text="I have an account",fg="black",bg='white',font=('Microsoft Yahei UI Ligth',9))
    label.place(x=90,y=340)

    signin=Button(frame,width=6,text="Sign in",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signin_window)
    signin.place(x=200,y=340)

    window.mainloop()

if __name__=='__main__':
    run_signup()