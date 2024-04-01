'''
    This file is for implementing database functions and commands
'''

import psycopg2
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Data:
    @staticmethod
    def db_get_score(un,pw):
        try:
            connection=psycopg2.connect(
                dbname="firstTry",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            cursor=connection.cursor()
            cursor.execute("select * from details where username=%s and password=%s",(un,pw))
            result=cursor.fetchone()
            if result:
                cursor.execute("select score from details where username=%s and password=%s",(un,pw))
                result_score=cursor.fetchone()[0]
                return result_score
            else:
                # User not found or invalid credentials
                messagebox.showerror('Error', 'Invalid username or password')

            # Close cursor and connection
            cursor.close()
            connection.close()

        except (Exception, psycopg2.Error) as error:
                # Error occurred while connecting or querying the database
                messagebox.showerror('Error', f'Database error: {error}')

    @staticmethod
    def increase_score(un,pw):
        try:
            connection=psycopg2.connect(
                dbname="firstTry",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            cursor=connection.cursor()
            cursor.execute("select * from details where username=%s and password=%s",(un,pw))
            result=cursor.fetchone()
            if result:
                cursor.execute("update details set score= score+1 where username=%s and password=%s",(un,pw))
                connection.commit()
            else:
                # User not found or invalid credentials
                messagebox.showerror('Error', 'Invalid username or password')

            # Close cursor and connection
            cursor.close()
            connection.close()

        except (Exception, psycopg2.Error) as error:
                # Error occurred while connecting or querying the database
                messagebox.showerror('Error', f'Database error: {error}')
   
    @staticmethod
    def show_leaderboard():
        try:
            # Establish connection to the database
            connection = psycopg2.connect(
                dbname="firstTry",
                user="postgres",
                password="admin",
                host="localhost",
                port="5432"
            )
            
            # Create a cursor to execute SQL queries
            cursor = connection.cursor()
            
            # Fetch scores from the database
            cursor.execute("SELECT username, score FROM details ORDER BY score DESC")
            leaderboard_data = cursor.fetchall()

            # Close cursor and connection
            cursor.close()
            connection.close()

            # Display leaderboard in a new window
            leaderboard_window = Tk()
            leaderboard_window.title("Leaderboard")
            leaderboard_window.geometry("700x600")
            
            # Create Treeview widget
            tree = ttk.Treeview(leaderboard_window, columns=("Rank", "Username", "Score"), show="headings")
            tree.heading("Rank", text="Rank")
            tree.heading("Username", text="Username")
            tree.heading("Score", text="Score")

            # Insert data into the Treeview
            for i, (username, score) in enumerate(leaderboard_data, start=1):
                tree.insert("", "end", values=(i, username, score))

            tree.tag_configure('right_align', anchor='e')  # Align values to the right

            tree.pack(expand=YES, fill=BOTH)

            # Close the leaderboard window
            def close_leaderboard():
                leaderboard_window.destroy()

            close_btn = Button(leaderboard_window, text="Close", command=close_leaderboard)
            close_btn.pack()

            leaderboard_window.mainloop()
        except (Exception, psycopg2.Error) as error:
            # Error occurred while connecting or querying the database
            messagebox.showerror('Error', f'Database error: {error}')

if __name__=="__main__":
    Data.show_leaderboard()
