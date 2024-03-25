from tkinter import *
from tkinter import messagebox
import random
import sys

global human_played
human_played=True
    
# def beginning():
def start_tic_tac_toe_game(receive_frontpage):
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
        b1= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b1,game_window))
        b2= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b2,game_window))
        b3= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b3,game_window))
        b4= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b4,game_window))
        b5= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b5,game_window))
        b6= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b6,game_window))
        b7= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b7,game_window))
        b8= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b8,game_window))
        b9= Button(game_window, text =" ", font=("helvetica",20),height=3,width=6,bg="systemButtonFace",command=lambda: b_click(b9,game_window))

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
    # return b1,b2,b3,b4,b5,b6,b7,b8,b9
    # return game_window
    game_window.mainloop()

def b_click(b,window):
        global clicked,count
        #for vs computer
        if not human_played:
            buttons_list=[]
            if b["text"] == " " and clicked == True:
                b["text"] = "X"
                clicked = False
                count+=1
                checkifwon(window)   
                for button in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
                    if button["text"]==" ":
                        buttons_list.append(button)
                generated_button=random.choice(buttons_list)
                b_click(generated_button,window)
            elif b["text"]== " " and clicked == False:
                b["text"]= "O"
                clicked= True
                count+=1
                checkifwon(window)
            else:
                messagebox.showerror("Tic-Tac-Toe","That box is already selected.\nSelect another box")
        else:#for 2v2
            print('its here for 2v2')
            if b["text"] == " " and clicked == True:
                b["text"] = "X"
                clicked = False
                count+=1
                checkifwon(window)        
            elif b["text"]== " " and clicked == False:
                b["text"]= "O"
                clicked= True
                count+=1
                checkifwon(window)
            else:
                messagebox.showerror("Tic-Tac-Toe","That box is already selected.\nSelect another box")

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
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        game_window.destroy()
        show_front_page()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","X Wins!!")
        game_window.destroy()
        show_front_page()

    #check for 0
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="red")
        b2.config(bg="red")
        b3.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        game_window.destroy()
        show_front_page()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="red")
        b5.config(bg="red")
        b6.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        game_window.destroy()
        show_front_page()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="red")
        b8.config(bg="red")
        b9.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="red")
        b5.config(bg="red")
        b9.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="red")
        b5.config(bg="red")
        b7.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="red")
        b4.config(bg="red")
        b7.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="red")
        b5.config(bg="red")
        b8.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        game_window.destroy()
        show_front_page()
    elif  b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="red")
        b6.config(bg="red")
        b9.config(bg="red")
        winner = True
        disable_all_buttons()
        messagebox.showinfo("Tic-Tac-Toe","O Wins!!")
        game_window.destroy()
        show_front_page()

    elif  winner==False:
        if count==9:
            winner = True
            disable_all_buttons()
            messagebox.showinfo("Tic-Tac-Toe","Draw !!")
            game_window.destroy()
            show_front_page()

def disable_all_buttons():
    for button in [b1,b2,b3,b4,b5,b6,b7,b8,b9]:
        button.config(state=DISABLED)

def vs_comp(recieved):
    global human_played
    human_played=False
    start_tic_tac_toe_game(recieved)
    print('its completed')
    # generated_button=random.choice([b1,b2,b3,b4,b5,b6,b7,b8,b9])
    # b_click(generated_butt)

def twoVtwo(recieved):
    global human_played
    human_played=True
    start_tic_tac_toe_game(recieved)

def show_front_page():
    front_page = Tk()
    front_page.title('codemy - tictactoe')
    front_page.geometry('925x500+300+200')
    front_page.resizable(False,False)

    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    def play_vs_computer():
        front_page.destroy()
        vs_comp(show_front_page)

    def play_vs_player():
        front_page.destroy()
        # start_tic_tac_toe_game(show_front_page)
        twoVtwo(show_front_page)

    def exit_game():
        front_page.destroy()
        sys.exit()

    vs_computer_btn = Button(front_page, text="Vs Computer", command=play_vs_computer)
    vs_computer_btn.pack()

    vs_player_btn = Button(front_page, text="Vs Player", command=play_vs_player)
    vs_player_btn.pack()

    exit_btn = Button(front_page, text="Exit", command=exit_game)
    exit_btn.pack()

    front_page.mainloop()

if __name__=="__main__":
    show_front_page()
