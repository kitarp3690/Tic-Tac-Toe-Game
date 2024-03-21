from tkinter import *
from tkinter import messagebox
import psycopg2
import signup as connect2
import trying

def run_signin():
    root =Tk()
    root.title('Login')
    root.geometry('925x500+300+200')
    root.configure(bg='#fff')
    root.resizable(False,False)

    def signup_window():
        root.destroy()
        connect2.run_signup()

    #this is photo of boy and girl
    img= PhotoImage(file='login.png')
    Label(root,image=img,bg='white').place(x=50,y=50)

    #this is the frame where all username,password and signin option is there
    frame=Frame(root,width=350,height=350,bg='white')
    frame.place(x=480,y=70)

    #this is the sign in header 
    heading=Label(frame,text='Sign in ', fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Ligth',23,'bold'))
    heading.place(x=100,y=5)

    #this function is used when signin button is pressed to get name and password
    def signing():
        username=user.get()
        password=code.get()
        
        try:
            connection=psycopg2.connect(
                dbname="firstTry",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            cursor=connection.cursor()
            cursor.execute("select * from details where username=%s and password=%s",(username,password))
            result=cursor.fetchone()
            if result:
                # User authenticated
                # messagebox.Message('Success', 'Logged in successfully')
                root.destroy()
                trying.show_front_page()
            else:
                # User not found or invalid credentials
                messagebox.showerror('Error', 'Invalid username or password')

            # Close cursor and connection
            cursor.close()
            connection.close()

        except (Exception, psycopg2.Error) as error:
            # Error occurred while connecting or querying the database
            messagebox.showerror('Error', f'Database error: {error}')

    ######-------------------------------------------
    def user_on_enter(e):
        user.delete(0,'end')
    def user_on_leave(e):
        name=user.get()
        if name=='':
            user.insert(0,'Username')
    #this for username 
    #this is the place where usename is entered
    user=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Ligth',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>', user_on_enter)
    user.bind('<FocusOut>', user_on_leave)

    #this is the frame for username
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

    ######----------------------------
    def code_on_enter(e):
        code.delete(0,'end')
    def code_on_leave(e):
        name=code.get()
        if name=='':
            code.insert(0,'Password')
    #this for password 
    #this is the place where password is entered
    code=Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft YaHei UI Ligth',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind('<FocusIn>', code_on_enter)
    code.bind('<FocusOut>', code_on_leave)

    #this is the frame for username
    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    ######----------------------------

    #This is the signin option button
    Button(frame,width=39,pady=7,text='Sign in',bg='#57a158',fg='white',cursor='hand2',command=signing,border=0).place(x=35,y=204)
    label=Label(frame,text="Don't have an account?",fg='black',bg='white',font=('Microsoft YaHei UI Ligth',9))
    label.place(x=75,y=270)

    signup=Button(frame,width=6,text='Sign up',border=0, bg='white', cursor='hand2',fg='#57a1f8',command=signup_window)
    signup.place(x=215,y=270)
    root.mainloop()

if __name__=='__main__':
    run_signin()