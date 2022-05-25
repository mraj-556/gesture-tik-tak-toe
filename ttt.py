import cv2
from tkinter import *
import threading
import time


                        #################  Map and variables  initialization #################

map =[ [-1 for i in range(3)] for j in range(3) ]  # (3 X 3)  matrix
btn_list = {}

global player_turn,game_over
player_turn = 1
game_over = False



                    #################  Player &  Button  Class  Declaration #################

class player:
    def __init__(self , player_name , player_type ):
        self.p_name = player_name
        self.p_type = player_type
    
    def set(self,loc_x,loc_y):
        map[loc_x][loc_y] = 1

    def reset(self,loc_x,loc_y):
        map[loc_x][loc_y] = -1


class Buttons:
    def __init__(self,b_name,b_pos):
        self.b_name = b_name
        self.b_size = [5,9]
        self.b_pos = b_pos
        self.button = Button(screen,text=' ',bg='blue',height=self.b_size[0],width = self.b_size[1] )
        self.button.config( command=lambda:set_colour(self.button) )
        self.button.place( x=b_pos[0] , y=b_pos[1] )

    def get_loc(self):
        print('x : ',self.b_pos[0],'y : ',self.b_pos[1])


                        ##################  button  clicked  ##################

def set_colour(button):
        # if player_turn == 1:
        #     clr = 'green'
        # elif player_turn ==2:
        #     clr = 'red'
        clr = 'green'
        button.config(bg=clr)


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
            btn_list[btn_name] = (Buttons(btn_name,[x,y]))
            x += 102
        y += 100
        x = 200

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
    global player_turn,game_over
    while not game_over:
        if player_turn == 1:
            print('player_1')
            player_turn = 2
        elif player_turn == 2:
            print('player_2')
            player_turn = 1
        time.sleep(1)

def create_thread():
    t = threading.Thread(target=game_start)
    t.daemon = True
    t.start()

            ##################################  main  code #####################################

game_setup()

screen = Tk()
screen.geometry('700x500+340+100')
screen.title('... Tik -- Tak -- Toe ...')

create_button()
create_thread()

screen.mainloop()
