# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 00:01:40 2022

@author: Michel T.
@INSTRUCTOR: Kyle Johnson
@School: UMGC
@Course: SDEV 300 Building Secure Python Applications

"""
from datetime import date
import random
import math
i = 0
while(i != 6):
    print("Enter 1 for Password Generator")
    print("Enter 2 Calculate and Format Percentage")
    print("Enter 3 How many Days from Today until July 4, 2025")
    print("Enter 4 Use the law of cosine to calculate the leg of a triangle")
    print("Enter 5 Calculate the volume of right circular cylinder")
    print("Enter 6 to exit")
    Inp = int(input("Enter a choice: "))
    if Inp == 6:       ## Condition that terminates the system after user input
        print("*********************** Have a good day! **********************************")
        break
    elif Inp == 1:
        
        L = int(input("Enter the length of the password: "))
        Num = int(input("Enter 0 if no NUMBERS are needed in password else enter 1:  "))
        Up = int(input("Enter 0 if no UPPER CASE LETTERS are needed in password else enter 1:  "))
        Low = int(input("Enter 0 if no LOWER CASE LETTERS are needed in password else enter 1:  "))
        Spe = int(input("Enter 0 if no SPECIAL CHARACTERS are needed in password else enter 1:  "))
        Password = ""
        Dic = []
        if Num == 1:
            X = chr(random.randint(48, 57)) 
            Password = Password + X
            L -= 1
            if L < 0:
                print("invalid inputs")
                continue
            Dic.append([48, 57])
        if Up == 1:
            X = chr(random.randint(65, 90)) 
            Password = Password + X
            L -= 1
            if L < 0:     
                print("invalid inputs")
                continue
            Dic.append([65, 90])
        if Low == 1:
            X = chr(random.randint(97, 122)) 
            Password = Password + X
            L -= 1
            if L < 0:
                print("invalid inputs")
                continue
            Dic.append([97, 122])
        if Spe == 1:
            X = chr(random.randint(33, 46)) 
            Password = Password + X
            L -= 1
            if L < 0:
                print("invalid inputs")
                continue
            Dic.append([33, 46])
        
        for i in range(L):
            R = random.randint(0, len(Dic) - 1)
            Password = Password + chr(random.randint(Dic[R][0], Dic[R][-1]))
        Password = ''.join(random.sample(Password, len(Password)))
        print(f"Generated password is {Password}.")
        
        
    elif Inp == 2:
        Num = float(input("Enter the numerator: "))
        Denom = float(input("Enter the denomenator: "))
        Decimal = int(input("Enter the number of decimal points for formatting: "))
        Val = Num/Denom*100
        Val = round(Val, Decimal)
        print(f"Percentage value is {Val}.")
        
    elif Inp == 3:
        D0 = date.today() ##Automatically tells the program the current date 
        D1 = date(2025, 7, 25)
        Delta = D1 - D0
        print(f"Total number of days is {Delta.days}.")
    
    elif Inp == 4:
        A = int(input("Enter first side length: "))
        B = int(input("Enter second side length: "))
        Ang = int(input("Enter the angle: "))
        C = A*A + B*B - 2*A*B*math.cos(math.pi/180*Ang)
        print(f"The leg of the triangle is {C}.")
    else:
        R = int(input("Enter the radius: "))
        H = int(input("Enter the height of cylinder: "))
        Vol = math.pi*R*R*H
        print(f"Volume of the cylinder is {Vol}.")
    print()
    print()

