import cv2
from cvzone.HandTrackingModule import HandDetector as hd
from pynput.mouse import Button, Controller
from  ttt import main
import threading

def create_thread():
    hand = threading.Thread(target=main)
    hand.daemon = True
    hand.start()


mouse = Controller()
cap = cv2.VideoCapture(0)
hand_detector = hd(1)

def hand_detect():
    while True:
        success , frame = cap.read()
        hand , frame = hand_detector.findHands(frame)
        if hand:
            id_fin = hand[0]['lmList'][8]
            mid_fin = hand[0]['lmList'][12]

            dist_x = abs(id_fin[0] - mid_fin[0])
            dist_y = abs(id_fin[1] - mid_fin[1])
            x , y = ( id_fin[0] + mid_fin[0] )//2 , ( id_fin[1] + mid_fin[1] )//2
            cv2.circle(frame,(id_fin[0],id_fin[1]) , 7 , (0,0,255) , -1)
            cv2.circle(frame,(mid_fin[0],mid_fin[1]) , 7 , (0,0,255) , -1)
            if dist_x <= 25 :
                clr = (0,255,0)
                mouse.press(Button.left)
                mouse.release(Button.left)
            else:
                clr = (0,0,255)
            cv2.circle(frame,(x,y) , 5 , clr , -1)

            cv2.line(frame , (id_fin[0],id_fin[1]) , (x,y) , (0,255,0) , 2 )
            cv2.line(frame , (x,y) ,  (mid_fin[0],mid_fin[1]) , (0,255,0) , 2 )


        cv2.imshow('img',frame)
        if cv2.waitKey(1) == ord('q'):
            break

create_thread()
hand_detect()