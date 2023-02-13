# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 01:00:25 2022

@author: Ziddane
"""


import keyboard
import sys

anum = 0
cnum = 0
enum = 0
inum = 0
onum = 0
unum = 0
stopped = False

def a():
    global anum
    if keyboard.is_pressed("`+a"):
        keyboard.write('\b')
        keyboard.write('\b')
    
        if anum == 0:
            keyboard.write("à")
            anum = 1
        elif anum == 1:
    
            keyboard.write("â")
            anum = 2
        elif anum == 2:
    
            keyboard.write("æ")
            anum = 0    
        #keyboard.write('\b')
            
def c():

    if keyboard.is_pressed("`+c"):
        keyboard.write('\b')
        keyboard.write('\b')
        keyboard.write("ç")
        
        
def y():  
    
    if keyboard.is_pressed("`+y"):
        keyboard.write('\b')
        keyboard.write('\b')
        keyboard.write("ÿ")   
        
        
def e():
    global enum
    if keyboard.is_pressed("`+e"):
        keyboard.write('\b')
        keyboard.write('\b')
        if enum == 0:
            keyboard.write("é")
            enum = 1
        elif enum == 1:
            keyboard.write("è")
            enum = 2
        elif enum == 2:
            keyboard.write("ê")
            enum = 3       
        elif enum == 3:
            keyboard.write("ë")
            enum = 0
            
def i():
   
    global inum
    if keyboard.is_pressed("`+i"):
        keyboard.write('\b')
        keyboard.write('\b')
        if inum == 0:
            keyboard.write("ï")
            inum = 1
        elif inum == 1:
            keyboard.write("î")
            inum = 0
            
def o():
  
    global onum
    if keyboard.is_pressed("`+o"):
        keyboard.write('\b')
        keyboard.write('\b')
        if onum == 0:
            keyboard.write("ô")
            onum = 1
        elif onum == 1:
            keyboard.write("œ")
            onum = 0
       
       
def u():
    global unum
    if keyboard.is_pressed("`+u"):
        keyboard.write('\b')
        keyboard.write('\b')
        if unum == 0:
            keyboard.write("ù")
            unum = 1
        elif unum == 1:
    
            keyboard.write("û")
            unum = 2
        elif unum == 2:
    
            keyboard.write("ü")
            unum = 0    
            
def quitKeyboard():
    global stopped
    keyboard.write('\b')
    keyboard.write('\b')
    stopped = True
            #####
keyboard.add_hotkey('`+a', a)
keyboard.add_hotkey('`+e', e)
keyboard.add_hotkey('`+i', i)
keyboard.add_hotkey('`+o', o)
keyboard.add_hotkey('`+u', u)
keyboard.add_hotkey('`+c', c)
keyboard.add_hotkey('`+y', y)

keyboard.add_hotkey('`+q', quitKeyboard)

keyboard.wait()

while True:
    if stopped == True:
        sys.exit("French Keyboard disabled")