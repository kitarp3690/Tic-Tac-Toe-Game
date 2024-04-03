'''
    This file is for all logic of games
'''

from tkinter import *
from tkinter import messagebox
import random
import sys
import signinClone as sn
import database_commands as datab

class ttt:
    global human_played
    human_played=True
    db_user=None
    db_pass=None  
    tttimg=None
    blackimg=None
    @staticmethod
    def store_record(id,pw):
        ttt.db_user,ttt.db_pass=id,pw
        ttt.show_front_page()
    @staticmethod
    def start_tic_tac_toe_game(receive_frontpage,is_comp=False):
        game_window = Tk()
        game_window.title('codemy - tictactoe')
        game_window.geometry("700x600")

        # Move the game logic here...
        #x starts so true
        global clicked, count, human_played
        clicked= True
        count = 0

        #structure of game
        #build our buttons    
        def structure():
            global b1,b2,b3,b4,b5,b6,b7,b8,b9
            b1= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: ttt.b_click(b1,game_window))
            b2= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: ttt.b_click(b2,game_window))
            b3= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: ttt.b_click(b3,game_window))
            b4= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: ttt.b_click(b4,game_window))
            b5= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: ttt.b_click(b5,game_window))
            b6= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: ttt.b_click(b6,game_window))
            b7= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: ttt.b_click(b7,game_window))
            b8= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: ttt.b_click(b8,game_window))
            b9= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: ttt.b_click(b9,game_window))

            #grid our buttons to the screen
            b1.grid(row=0,column=0)
            b2.grid(row=0,column=1)
            b3.grid(row=0,column=2)

            b4.grid(row=1,column=0)
            b5.grid(row=1,column=1)
            b6.grid(row=1,column=2)

            b7.grid(row=2,column=0)
            b8.grid(row=2,column=1)
            b9.grid(row=2,column=2)

            #Showing the score in the front_page
            if is_comp==True:
                # store_usname,store_uspass=ttt.get_score()
                actual_score=datab.Data.db_get_score(ttt.db_user,ttt.db_pass)
                score=Label(text=f"Score: {actual_score}",font=("helvetica",20,"bold"),fg="blue")
                score.place(x=400,y=60)

        # Calling structure function to create the game board
        structure()
        game_window.mainloop()
    @staticmethod
    def b_click(b,window):
            global clicked,count
            #for vs computer
            if not human_played:
                buttons_list=[]
                if b["text"] == " " and clicked == True:
                    b["text"] = "X"
                    clicked = False
                    count+=1
                    ttt.checkifwon(window,True)   
                    for button in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
                        if button["text"]==" ":
                            buttons_list.append(button)
                    generated_button=random.choice(buttons_list)
                    ttt.b_click(generated_button,window)
                elif b["text"]== " " and clicked == False:
                    b["text"]= "O"
                    clicked= True
                    count+=1
                    ttt.checkifwon(window,True)
                else:
                    messagebox.showerror("Tic-Tac-Toe","That box is already selected.\nSelect another box")
            else:#for 2v2
                if b["text"] == " " and clicked == True:
                    b["text"] = "X"
                    clicked = False
                    count+=1
                    ttt.checkifwon(window)        
                elif b["text"]== " " and clicked == False:
                    b["text"]= "O"
                    clicked= True
                    count+=1
                    ttt.checkifwon(window)
                else:
                    messagebox.showerror("Tic-Tac-Toe","That box is already selected.\nSelect another box")
    @staticmethod
    def checkifwon(game_window,is_comp=False):
        global winner 
        winner = False
        player_win = False 

        # store_usname,store_uspass=ttt.get_score()
        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            player_win = True
            ttt.disable_all_buttons()
            # datab.Data.increase_score(ttt.db_user,ttt.db_pass)
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            player_win = True
            ttt.disable_all_buttons()
            # datab.Data.increase_score(ttt.db_user,ttt.db_pass)
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            player_win = True
            ttt.disable_all_buttons()
            # datab.Data.increase_score(ttt.db_user,ttt.db_pass)
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            player_win = True
            ttt.disable_all_buttons()
            # datab.Data.increase_score(ttt.db_user,ttt.db_pass)
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            player_win = True
            ttt.disable_all_buttons()
            # datab.Data.increase_score(ttt.db_user,ttt.db_pass)
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            player_win = True
            ttt.disable_all_buttons()
            # datab.Data.increase_score(ttt.db_user,ttt.db_pass)
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            player_win = True
            ttt.disable_all_buttons()
            # datab.Data.increase_score(ttt.db_user,ttt.db_pass)
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            player_win = True
            ttt.disable_all_buttons()
            # datab.Data.increase_score(ttt.db_user,ttt.db_pass)
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()

        #check for 0
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            ttt.disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            ttt.disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            ttt.disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            ttt.disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            ttt.disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            ttt.disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            ttt.disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()
        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            ttt.disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            # game_window.destroy()
            # ttt.show_front_page()

        #check for draw
        elif  winner == False:
            if count==9:
                # winner = True
                ttt.disable_all_buttons()
                messagebox.showinfo("Tic-Tac-Toe","Draw !!")
                game_window.destroy()
                ttt.show_front_page()
        
        #for vs_comp check for user win
        if winner == True:
            if is_comp == True and player_win == True:
                datab.Data.increase_score(ttt.db_user,ttt.db_pass)
            else:
                pass
            game_window.destroy()
            ttt.show_front_page()
    @staticmethod
    def disable_all_buttons():
        for button in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
            button.config(state=DISABLED)
    @staticmethod
    def vs_comp(recieved):
        global human_played
        human_played=False
        ttt.start_tic_tac_toe_game(recieved,is_comp=True)
    @staticmethod
    def twoVtwo(recieved):
        global human_played
        human_played=True
        ttt.start_tic_tac_toe_game(recieved)
    @staticmethod
    # Function to change button color on hover
    def on_enter(event,butt):
        """This method is used to show bg(background) color when mouse cursor is hovered in that button"""
        butt.config(bg="#35E375")
    @staticmethod
    # Function to change button color back when mouse leaves
    def on_leave(event,butt):
        """This method is used to change the bg color to normal state color when mouse cursor leaves that button"""
        butt.config(bg="SystemButtonFace")
    @staticmethod
    def show_front_page():
        front_page = Tk()
        front_page.title('codemy - tictactoe')
        front_page.geometry('925x500+300+200')
        front_page.resizable(False,False)
        #loading the background image        
        global bg_image, blackimg
        tttimg = PhotoImage(file="images/ttt.png")
        ttt.show_bg_image(front_page,tttimg)

        global b1,b2,b3,b4,b5,b6,b7,b8,b9
        def play_vs_computer():
            front_page.destroy()
            ttt.vs_comp(ttt.show_front_page)

        def play_vs_player():
            front_page.destroy()
            ttt.twoVtwo(ttt.show_front_page)

        def show_leaderboard():
            front_page.destroy()
            datab.Data.show_leaderboard()

        def exit_game():
            front_page.destroy()
            sys.exit()

        vs_computer_btn = Button(front_page, text="Vs Computer", command=play_vs_computer, height=3, width=15, cursor="hand2", font=("Helvetica", 16), relief=RAISED, borderwidth=3)
        vs_computer_btn.bind("<Enter>", lambda event: ttt.on_enter(event,vs_computer_btn))
        vs_computer_btn.bind("<Leave>", lambda event: ttt.on_leave(event,vs_computer_btn))
        vs_computer_btn.place(x=680,y=70)

        vs_player_btn = Button(front_page, text="Vs Player", command=play_vs_player, height=3, width=15, cursor="hand2", font=("Helvetica", 16), relief=RAISED, borderwidth=3)
        vs_player_btn.bind("<Enter>", lambda event: ttt.on_enter(event,vs_player_btn))
        vs_player_btn.bind("<Leave>", lambda event: ttt.on_leave(event,vs_player_btn))
        vs_player_btn.place(x=680, y=160)
        
        leaderboard_btn = Button(front_page, text="Leaderboard", command=show_leaderboard, height=3, width=15, cursor="hand2", font=("Helvetica", 16), relief=RAISED, borderwidth=3)
        leaderboard_btn.bind("<Enter>", lambda event: ttt.on_enter(event,leaderboard_btn))
        leaderboard_btn.bind("<Leave>", lambda event: ttt.on_leave(event,leaderboard_btn))
        leaderboard_btn.place(x=680,y=250)

        exit_btn = Button(front_page, text="Exit", command=exit_game, height=3, width=15, cursor="hand2", font=("Helvetica", 16),relief=RAISED, borderwidth=3)
        exit_btn.bind("<Enter>", lambda event: ttt.on_enter(event,exit_btn))
        exit_btn.bind("<Leave>", lambda event: ttt.on_leave(event,exit_btn))
        exit_btn.place(x=680, y=340)

        front_page.mainloop()
    @staticmethod
    def show_bg_image(front, tttimg):
        tttimg_width = int(front.winfo_width() * 0.9)

        #creating label with tttimg bg img
        my_label = Label(front, image=tttimg, width=tttimg_width )
        my_label.place(x=0, y=0, relheight=1)
    
if __name__=="__main__":
    ttt.show_front_page()