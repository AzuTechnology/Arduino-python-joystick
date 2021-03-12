from tkinter import *
import serial


win = Tk()
win.geometry("300x400+50+200")
win.bind('<Escape>', lambda e: win.quit())
win.configure(relief=RAISED)
label = Label(win,font=('Arial',20))
label.place(x=100, y=100)
import pygame

ser = serial.Serial("COM3", '9600', timeout=5)

pygame.init()
joysticks = []
for i in range(pygame.joystick.get_count()):
    joysticks.append(pygame.joystick.Joystick(i))
for joystick in joysticks:
    joystick.init()

button_keys={
  "1": 0,
  "2": 1,
  "3": 2,
  "4": 3,
  "L2": 4,
  "R2": 5,
  "L1": 6,
  "R1": 7,
  "select": 8,
  "start": 9,
  "up_arrow": 10,
  "down_arrow": 11,
  "left_arrow": 12,
  "right_arrow": 13
}
def get_joystick():
    """To read the joystick buttons this fun return button"""
    for event in pygame.event.get():
        button = ''
        # right buttons and joystick
        key = '1','2','3','4'
        stop_key = '1x','2x','3x','4x'
        if event.type == pygame.JOYBUTTONDOWN:
            for i,val in enumerate(key):
                if event.button == button_keys[key[i]]:
                    button = key[i]
                    return button

        if event.type == pygame.JOYBUTTONUP:
            for i, val in enumerate(key):
                if event.button == button_keys[key[i]]:
                    button = stop_key[i]

        return button
    
val =''
def send():
    global val
    button = get_joystick()
    #turn on
    if button == '1':
        val = 'a'
    if button == '2':
        val = 'b'
    if button == '3':
        val = 'c'
    if button == '4':
        val = 'd'
    # turn off
    if button == '1x':
        val = 'x'
    if button == '2x':
        val = 'x'
    if button == '3x':
        val = 'x'
    if button == '4x':
        val = 'x'
    label['text'] = val



    ser.write(val.encode('utf-8'))
    win.after(30,send)

send()

win.mainloop()