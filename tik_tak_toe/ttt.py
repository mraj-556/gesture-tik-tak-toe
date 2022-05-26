import cv2
from tkinter import *
import threading
import time
import pygame as pg
from tkinter import messagebox as msgbox


                        #################  Map and variables  initialization #################

map_list =[ [-1 for i in range(3)] for j in range(3) ]  # (3 X 3)  matrix
btn_list = {}

global player_turn , game_over , player_choosed , flag , i , t_g_start , t_g_res , screen
player_turn = 1
player_choosed = 0
game_over = False


                    #################  Player &  Button  Class  Declaration #################

class player:
    def __init__(self , player_name , player_type ):
        self.p_name = player_name
        self.p_type = player_type
    
    def set(self,loc_x,loc_y):
        map_list[loc_x][loc_y] = 1

    def reset(self,loc_x,loc_y):
        map_list[loc_x][loc_y] = -1


class Buttons:
    global screen
    def __init__(self,b_names,b_poss):
        self.b_name = b_names
        self.b_size = [5,9]
        self.b_pos = b_poss
        self.button = Button(screen,text=' ',bg='blue',bd='2',height=self.b_size[0],width = self.b_size[1] )
        self.button.config( command=lambda:set_colour(self.b_name , self.button) )
        # bg_clr = self.button.cget('bg')
        self.button.config(activebackground = 'cyan')
        self.button.place( x=self.b_pos[0] , y=self.b_pos[1] )

    def get_loc(self):
        print('x : ',self.b_pos[0],'y : ',self.b_pos[1])
    def get_name(self):
        print(self.b_name)

                        ##################  button  clicked  ##################

def set_colour(btn_name,btn_obj):
    global player_turn , game_over , player_choosed , screen
    if not game_over:
        p = btn_name.split('_')[1]
        x,y = int(p[0]), int(p[1])
        if player_turn == 1 and map_list[x][y] == -1:
            map_list[x][y] = 1
            clr = 'green'
            btn_obj.config(bg=clr)
            player_choosed = 1

        elif player_turn ==2 and map_list[x][y] == -1:
            map_list[x][y] = 2
            clr = 'red'
            btn_obj.config(bg=clr)
            player_choosed = 2

        elif map_list[x][y] == 1 or map_list[x][y] == 2:
            print('Invalid')


                        #################  Player  Object  initialization #################

p_1 = player('Player 1',1)
p_2 = player('Player 2',0)

                        #################  object  details  set up #################

def multiplayer():
    p1_name = input('Player 1 : ')
    p2_type = 0
    
    while True:
        p1_type = input('Type (x / o) : ').lower()
        if p1_type == 'x':
            p1_type = 'X'
            p2_type = 'O'
            break
        elif p1_type == 'o':
            p1_type = 'O'
            p2_type = 'X'
            break
        else:
            print('Invalid Choice')

    p2_name = input('Player 2 : ')

    p_1.p_name = p1_name
    p_1.p_type = p1_type

    p_2.p_name = p2_name
    p_2.p_type = p2_type

    show_details()

def bot():
    p_name = input('Name : ')
    bot_type = 0
    while True:
        p_type = input('Type (x / o) : ').lower()
        if p_type == 'x':
            p_type = 'X'
            bot_type = 'O'
            break
        elif p_type == 'o':
            p_type = 'O'
            bot_type = 'X'
            break
        else:
            print('Invalid choice')
    
    p_1.p_name = p_name
    p_1.p_type = p_type

    p_2.p_name = 'Bot'
    p_2.p_type = bot_type

    show_details()

def show_details():
    print('\n Details of players : \n')
    print('Player 1 :')
    print('     Name    : ',p_1.p_name)
    print('     choosed : ',p_1.p_type)
    print()
    print('###################################')
    print()
    print('Player 2 :')
    print('     Name    : ',p_2.p_name)
    print('     choosed : ',p_2.p_type)


                        #################  button  creating #################

def create_button():
    x,y = 200,80
    for i in range(3):
        for j in range(3):
            btn_name = 'btn_'+f'{i}{j}'
            btn_list[btn_name] = Buttons(btn_name,[x,y])
            x += 102
        y += 100
        x = 200
    # print( btn_list['btn_11'].b_name)

                        #################  mode selection and details input #################

def game_setup():
    print('Modes : ')
    print('     1. Two player2.')
    print('     2. Bot.')

    while True:
        try:
            mode = int(input('Choose a mode : '))
            if mode==1:
                print('Enabling Multiplayer mode.....')
                multiplayer()
                break
            elif mode==2:
                print('Enabling Bot mode.....')
                bot()
                break
            else:
                print('Invalid Selection...')
        except:
            print('Invalid Selection...')

                    ########################  game start  ########################

def game_start():
    global player_turn,game_over,player_choosed , screen
    print(f'{p_1.p_name} turn')
    while not game_over:
        if player_turn == 1 and player_choosed == 1:
            print(f'{p_2.p_name} turn')
            player_choosed = 1
            player_turn = 2
        elif player_turn == 2 and player_choosed == 2:
            print(f'{p_1.p_name} turn')
            player_choosed = 2
            player_turn = 1

                    ########################  game over  ########################

# map_list = [[1, 2, 2], [1, -1, -1], [1, -1, -1]]

i = 0
flag = True
def game_result():
    global flag , i , game_over , t_g_start , t_g_res , screen
    flag1 = True   
    while flag1:
        p = [ [ map_list[0][0],map_list[0][1],map_list[0][2] ] , [ map_list[1][0],map_list[1][1],map_list[1][2] ] , [ map_list[2][0],map_list[2][1],map_list[2][2] ] , [ map_list[0][0],map_list[1][0],map_list[2][0] ]  ,  [ map_list[0][1],map_list[1][1],map_list[2][1] ] , [ map_list[0][2],map_list[1][2],map_list[2][2] ] , [ map_list[0][0],map_list[1][1],map_list[2][2] ] , [ map_list[0][2],map_list[1][1],map_list[2][0] ] ]
        i=0
        # time.sleep(1)
        while (flag and i<len(p)):
            # print(map_list,"      |||||||    ",p[0])
            if p[i] == [1,1,1]:
                print(f'{p_1.p_name} own this')
                msg = f'{p_1.p_name} Own This Match\nGood Luck'
                notification = msgbox.showinfo('Result',msg)
                game_over = True
                flag1 = False
                screen.destroy()
                break
            elif p[i] == [2,2,2]:
                print(f'{p_2.p_name} own this')
                msg = f'{p_2.p_name} Own This Match\nGood Luck'
                notification = msgbox.showinfo('Result',msg)
                game_over = True
                flag1 = False
                screen.destroy()
                break
            else:
                pass
            i += 1
        for j,l in enumerate(map_list):
            if l.count(-1)==0 and j==len(map_list)-1 and not game_over:
                print('Draw')
                msg = ' !...Match Draw...!'
                notification = msgbox.showinfo('Result',msg)
                game_over = True
                flag = False
                flag1 = False
                screen.destroy()
                break
# game_result()
                    #######################  Threading  ###########################

def create_thread():
    global t_g_start,t_g_res
    t_g_start = threading.Thread(target=game_start)
    t_g_res = threading.Thread(target= game_result)

    t_g_res.daemon = True
    t_g_start.daemon = True
    
    t_g_start.start()
    t_g_res.start()

    

            ##################################  main  code #####################################
def main():
    global screen
    game_setup()

    screen = Tk()
    screen.geometry('700x500+340+100')
    screen.title('... Tik -- Tak -- Toe ...')

    create_button()
    create_thread()

    screen.mainloop()

if __name__ == '__main__':
    main()