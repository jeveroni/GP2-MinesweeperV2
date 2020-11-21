import tkinter
import tkinter.messagebox
import numpy as np
from tkinter import *
import random
from PIL import Image, ImageTk


window = tkinter.Tk()
window.geometry("755x455")
window.title("Jev's 2nd Minesweeper Game")
window.resizable(0, 0)


def press_click(event):
    x = event.widget.winfo_x()
    y = event.widget.winfo_y()
    if(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 2):
        ()
    elif(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 1):
        ()
    elif(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 3):
        ()        
    else:
        event.widget.configure(bg='green')

def release_click(event):      
    x = event.widget.winfo_x()
    y = event.widget.winfo_y()
    if(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 2):
        ()
    elif(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 1):
        ()
    elif(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 3):
        ()
    else:
        event.widget.configure(bg="blue")
        global click_count
        if(click_count == 0):
            rando(spot_check_rev(x,y))
            board_nums()
        click_count = click_count + 1
        reveal(spot_check(x,y), spot_check_rev(x,y))
        if(check_win()):
            mine_number.configure(bg='green2',text='0')
            win_lose_label.configure(text = "You win", bg='green2')
            for i in range(9):
                for j in range(9):
                    if(board[i][j] == 100):
                        grid[j][i].configure(image=flag, bg='green2')
                    flag_board[i][j] = 3

                        
def right_click(event):
    if(click_count > 0):
        x = event.widget.winfo_x()
        y = event.widget.winfo_y()
        if(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 2):
            ()
        elif(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 1):
            event.widget.configure(image='', bg='blue')
            flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] = 0
            mine_temp_count = 0
            for i in range(9):
                for j in range(9):
                    if(flag_board[i][j]==1):
                        mine_temp_count += 1
            mine_number.configure(text = f"{10 - mine_temp_count}")
            
        elif(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 0):
            event.widget.configure(image=flag,bg = 'gold')
            flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] = 1
            mine_temp_count = 0
            for i in range(9):
                for j in range(9):
                    if(flag_board[i][j]==1):
                        mine_temp_count += 1
            mine_number.configure(text = f"{10 - mine_temp_count}")
        elif(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 3):
            ()
            
def double_click(event):
    x = event.widget.winfo_x()
    y = event.widget.winfo_y()
    if(flag_board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]] == 2):
        flag_count = 0 
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                temporary = ([spot_check_rev(x,y)[0]+i,spot_check_rev(x,y)[1]+j])
                if(temporary[0] < 0 or temporary[1] < 0 or temporary[0] > 8 or temporary[1] > 8):
                    ()
                else:
                    if(flag_board[temporary[0]][temporary[1]]==1):
                        flag_count += 1
        if(board[spot_check_rev(x,y)[0]][spot_check_rev(x,y)[1]]==flag_count and flag_count>0):
            for i in range(-1,2,1):
                for j in range(-1,2,1):
                    temporary = ([spot_check_rev(x,y)[0]+i,spot_check_rev(x,y)[1]+j])
                    if(temporary[0] < 0 or temporary[1] < 0 or temporary[0] > 8 or temporary[1] > 8):
                        ()
                    else:
                        if(board[temporary[0]][temporary[1]] != 0 and board[temporary[0]][temporary[1]] != 100):
                            grid[temporary[1]][temporary[0]].configure(font = "Helvetica 45 bold",text = f'{board[temporary[0]][temporary[1]]}', fg = colours[int(f'{board[temporary[0]][temporary[1]]}')],bg = 'lavender',justify = 'center')
                            win_board[temporary[0]][temporary[1]]=10
                            flag_board[temporary[0]][temporary[1]]=2
                        elif(board[temporary[0]][temporary[1]] == 0):
                            reveal((temporary[1],temporary[0]),(temporary[0],temporary[1]))
    if(check_win()):
        mine_number.configure(bg='green2',text='0')
        win_lose_label.configure(text = "You win", bg='green2')
        for i in range(9):
            for j in range(9):
                if(board[i][j] == 100):
                    grid[j][i].configure(image=flag, bg='green2')
                flag_board[i][j] = 3
                            



def spot_check(x,y):
    new_x = (x-5)/50
    new_y = (y-5)/50
    return([int(new_x), int(new_y)])

def spot_check_rev(y,x):
    new_x = (x-5)/50
    new_y = (y-5)/50
    return([int(new_x), int(new_y)])

    


def rando(initial_click):
    if(len(coords) == 10):
        return True
    temp_x_coord = random.randint(0,8)
    temp_y_coord = random.randint(0,8)
    temp_coord = ([temp_x_coord,temp_y_coord])
    if not(initial_click == temp_coord):
        counter1=0
        for m in range(-1,2,1):
            for n in range(-1,2,1):
                temp_spot = ([temp_coord[0]+m,temp_coord[1]+n])
                if(temp_spot[0] < 0 or temp_spot[1] <0 or temp_spot[0] > 8 or temp_spot[1] > 8):
                    ()
                elif(temp_spot == initial_click):
                        counter1 =counter1+1
        if(counter1 == 0):
            counter2=0
            for i in range(len(coords)):
                if(len(coords) == 0):
                    break
                if(temp_coord==coords[i]):
                    counter2 = counter2 + 1
            if(counter2 == 0):
                coords.append(temp_coord)
                board[temp_coord[0]][temp_coord[1]]=100
                rando(initial_click)
            else:
                rando(initial_click)
        else:
            rando(initial_click)
    else:
        rando(initial_click)
        
def board_nums():
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 100):
                ()
            else:
                num = 0
                for m in range(-1,2,1):
                    for n in range(-1,2,1):
                        if(i+m < 0 or j+n < 0 or i+m > 8 or j+n > 8):
                            ()
                        else:
                            if(board[i+m][j+n]==100):
                                num += 1
                board[i][j] = num
    for i in range(9):
        for j in range(9):
            if(board[i][j]==100):
                global win_count
                win_count = win_count + 1    
                
def check_win():
    win_board_count = 0
    for i in range(9):
        for j in range(9):
            if(win_board[i][j] == 0):
                win_board_count = win_board_count + 1
    if(win_count == win_board_count):
        return True
    else:
        return False                
                
def reveal(spot,rev_spot):
#    this is if the button clicked is a 0
    if(board[rev_spot[0]][rev_spot[1]]==0):
        win_board[rev_spot[0]][rev_spot[1]] = 10
        zeros.append(rev_spot)
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                temporary = ([rev_spot[0]+i,rev_spot[1]+j])
                if(temporary[0] < 0 or temporary[1] < 0 or temporary[0] > 8 or temporary[1] > 8):
                    ()
                elif(board[temporary[0]][temporary[1]]==0):
                    same = 0
                    for k in range(len(zeros)):
                        if(temporary == zeros[k]):
                            same = same + 1
                    if(same>0):
                        win_board[temporary[0]][temporary[1]]=10
                        grid[temporary[1]][temporary[0]].configure(bg='lavender')
                        flag_board[temporary[0]][temporary[1]] = 2
                    else:
                        reveal((temporary[1],temporary[0]),temporary)
                            
                elif not(board[temporary[0]][temporary[1]]==0):
                    win_board[temporary[0]][temporary[1]] = 10
                    grid[temporary[1]][temporary[0]].configure(font = "Helvetica 45 bold",text = f'{board[rev_spot[0]+i][rev_spot[1]+j]}', fg = colours[int(f'{board[rev_spot[0]+i][rev_spot[1]+j]}')],bg = 'lavender',justify = 'center')
                    flag_board[temporary[0]][temporary[1]] = 2

#   this is if the button clicked is a mine 
    elif(board[rev_spot[0]][rev_spot[1]]==100):
        grid[spot[0]][spot[1]].configure(bg='red')
        lose()
        global win_lose_label
        win_lose_label.configure(text = "You lose", bg='red')
#   this is if the button clicked is a number
    else:            
        win_board[rev_spot[0]][rev_spot[1]]=10                                                    
        grid[spot[0]][spot[1]].configure(font = "Helvetica 45 bold",text = f'{board[rev_spot[0]][rev_spot[1]]}', fg = colours[int(f'{board[rev_spot[0]][rev_spot[1]]}')],bg = 'lavender',justify = 'center')
        flag_board[spot[1]][spot[0]] = 2
                   
def lose():
    mine_number.configure(bg='red',text='0')
    for i in range(9):
        for j in range(9):
            if(board[i][j] == 100):
                if(flag_board[i][j]==1):
                    grid[j][i].configure(bg='green2')
                else:
                    grid[j][i].configure(image=mine)
            flag_board[i][j]=3
                            



def set_up_game():   
    global click_count
    global win_count
    global zeros
    global coords
    global board
    global win_board
    global first_time
    global flag_board
    win_lose_label.configure(bg='white',text='')
    mine_number.configure(bg='white',text='10')
    click_count = 0
    win_count=0
    zeros=[]
    coords=[]        

    board = np.array([
        [0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]])  

    win_board = np.array([
        [0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]])
    
    flag_board = np.array([
        [0,0,0,0,0,0,0,0,0], 
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]])
    
    if(first_time == 0):
        ()
    else:
        for i in range(9):
            for j in range(9):
                grid[i][j].configure(text = '', background='blue',image='')
    first_time = 1
    


grid=[]            
first_time = 0
win_lose_label = tkinter.Label(window, bg='white', text='')
win_lose_label.place(x=455,y=0, height=100,width=300)
mine_count = tkinter.Label(window, text = "Mines left:", font = "Helvetica 40 bold")
mine_count.place(x=455, y=250, height=50)
mine_number = tkinter.Label(window, bg='white', text = '10', font = "Helvetica 40 bold")
mine_number.place(x=675, y=250,height = 50, width = 50)
set_up_game()
colours=['','blue','green','red','purple','black']
labels = []

for i in range(0,9):
    button_row=[]
    for j in range(0,9):
        button = tkinter.Label(window, background='blue')
        button.place(x=(50*i)+5,y=(50*j)+5, width = 45, height = 45)
        button_row.append(button)
    grid.append(button_row)
    
for i in range(0,9):
    for j in range(0,9):
        grid[i][j].bind("<ButtonPress-1>", press_click)
        grid[i][j].bind("<ButtonRelease-1>", release_click)
        grid[i][j].bind("<ButtonRelease-2>", right_click)
        grid[i][j].bind("<ButtonRelease-3>", right_click)
        grid[i][j].bind("<Double-Button-1>", double_click)
        

flag = ImageTk.PhotoImage(Image.open("flag.png"))
mine = ImageTk.PhotoImage(Image.open("mine.png"))

restart_button = tkinter.Button(window, command = set_up_game, text='Restart')
restart_button.place(x=455,y=350,height=100,width=295)
window.mainloop()