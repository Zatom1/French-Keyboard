# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 01:00:25 2022

@author: Ziddane
"""


import keyboard

anum = 0
cnum = 0
enum = 0
inum = 0
onum = 0
unum = 0

while True:
    
    if keyboard.is_pressed("alt+a"):
        if anum == 0:
            keyboard.write("à")
            anum = 1
        elif anum == 1:

            keyboard.write("â")
            anum = 2
        elif anum == 2:

            keyboard.write("æ")
            anum = 0    
            
            
            
    if keyboard.is_pressed("alt+c"):
        keyboard.write("ç")
        
        
        
    if keyboard.is_pressed("alt+y"):
        keyboard.write("ÿ")   
        
        
        
    if keyboard.is_pressed("alt+e"):

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
            
            
            
    if keyboard.is_pressed("alt+i"):

        if inum == 0:
            keyboard.write("ï")
            inum = 1
        elif inum == 1:
            keyboard.write("î")
            inum = 0
            
            
            
    if keyboard.is_pressed("alt+o"):
        if onum == 0:
            keyboard.write("ô")
            onum = 1
        elif onum == 1:
            keyboard.write("œ")
            onum = 0
       
       
       
    if keyboard.is_pressed("alt+u"):

        if unum == 0:
            keyboard.write("ù")
            unum = 1
        elif unum == 1:

            keyboard.write("û")
            unum = 2
        elif unum == 2:

            keyboard.write("ü")
            unum = 0    