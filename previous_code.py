from tkinter import *
from tkinter import messagebox

def start_tic_tac_toe_game(receive_frontpage):
    game_window = Tk()
    game_window.title('codemy - tictactoe')
    game_window.geometry("700x600")

    # Move the game logic here...
    #x starts so true
    global clicked, count
    clicked= True
    count = 0

    #disable all buttons 
    '''def disable_all_buttons():
        for button in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
            button.config(state=DISABLED)'''
        # b1.config(state=DISABLED)
        # b2.config(state=DISABLED)
        # b3.config(state=DISABLED)
        # b4.config(state=DISABLED)
        # b5.config(state=DISABLED)
        # b6.config(state=DISABLED)
        # b7.config(state=DISABLED)
        # b8.config(state=DISABLED)
        # b9.config(state=DISABLED)

    #check to see if someone won
    '''
    def checkifwon():
        global winner 
        winner = False

        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            game_window.destroy()
            show_front_page()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()

        #check for 0
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
        elif  b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
            disable_all_buttons()
            game_window.destroy()
            show_front_page()
'''
    #button clicked function
    def b_click(b):
        global clicked,count
        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            count=+1
            checkifwon(game_window)        
        elif b["text"]== " " and clicked == False:
            b["text"]= "O"
            clicked= True
            count=+1
            checkifwon(game_window)
        else:
            messagebox.showerror("Tic-Tac-Toe","That box is already selected.\nSelect another box")

    #structure of game
    #build our buttons
    
    def structure():
        global b1,b2,b3,b4,b5,b6,b7,b8,b9
        b1= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b1))
        b2= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b2))
        b3= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b3))
        b4= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b4))
        b5= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b5))
        b6= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b6))

        b7= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b7))
        b8= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b8))
        b9= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b9))

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

    # Call structure function to create the game board
    structure()
    game_window.mainloop()
    # return game_window

def checkifwon(game_window):
    global winner 
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        game_window.destroy()
        show_front_page()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()

    #check for 0
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()
    elif  b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        disable_all_buttons()
        game_window.destroy()
        show_front_page()

def disable_all_buttons():
    for button in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
        button.config(state=DISABLED)

def vs_comp():
    pass

def twoVtwo():
    def b_click(b):
        global clicked,count
        if b["text"] == " " and clicked == True:
            b["text"] = "X"
            clicked = False
            count=+1
            checkifwon(start_tic_tac_toe_game)        
        elif b["text"]== " " and clicked == False:
            b["text"]= "O"
            clicked= True
            count=+1
            checkifwon(start_tic_tac_toe_game)
        else:
            messagebox.showerror("Tic-Tac-Toe","That box is already selected.\nSelect another box")

def show_front_page():
    front_page = Tk()
    front_page.title('codemy - tictactoe')
    front_page.geometry("700x600")

    def play_vs_computer():
        front_page.destroy()

    def play_vs_player():
        front_page.destroy()
        start_tic_tac_toe_game(show_front_page)
        twoVtwo()

    def exit_game():
        front_page.destroy()

    vs_computer_btn = Button(front_page, text="Vs Computer", command=play_vs_computer)
    vs_computer_btn.pack()

    vs_player_btn = Button(front_page, text="Vs Player", command=play_vs_player)
    vs_player_btn.pack()

    exit_btn = Button(front_page, text="Exit", command=exit_game)
    exit_btn.pack()

    front_page.mainloop()

def main():
    show_front_page()

if __name__=="__main__":
    main()
