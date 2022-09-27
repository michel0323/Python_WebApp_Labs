#Importing Necessary Libraries
"""
re is used for regular expression and numpy is used for speedy calculation and computational tasks.
"""
import re
import numpy as np


print("***************** Welcome to the Python Matrix Application***********")


while True:
    #Choosing the option Yes or No
    option_choice=input("Do you want to play the Matrix Game?\nEnter Y for Yes or N for No:")
    if option_choice=="Y":
        while True:
            phone_number=input("Enter your phone number (XXX-XXX-XXXX:")
            #Using Regular expression to check ohone number Format
            if re.match(r"\d{3}-\d{3}-\d{4}",phone_number):
                break
            print("Your phone number is not in correct format. Please renter:")

        while True:
            zip_code=input("Enter your zip code+4 (XXXXX-XXXX):")
            #Using Regular expression to check zipcode Format
            if re.match(r"\d{5}-\d{4}",zip_code):
                break
            print("Your zip code is not in correct format. Please renter:")

        #Creating The first Matrix
        print("Enter your first 3x3 matrix:")
        mat1=[]

        #Loop to insert element of matrix
        for i in range(0,3):
            row=input().split(' ')
            row=list(map(str ,row))
            mat1.append(row)

        print("Your first 3x3 matrix is:")

        for r in range(0,3):
            for c in range(0,3):
                print(mat1[r][c],end=" ")
            print()

        #Creating The second Matrix
        print("Enter your second 3x3 matrix:")
        mat2=[]
        #Loop to insert element of matrix
        for i in range(0,3):
            row=input().split(' ')
            row=list(map(str,row))
            mat2.append(row)

        print("Your second 3x3 matrix is:")

        for r in range(0,3):
            for c in range(0,3):
                print(mat2[r][c],end=" ")
            print()


        #Creating the menu
        print("Select a Matrix Operation from the list below:\n\na.Addition\nb.Subtraction\
              \nc.Matrix Multiplication\nd.Element by element multiplication")
        menu_choice=input()
        #converting array into float before performing operations
        mat1=np.array(mat1, dtype = float)
        mat2=np.array(mat2,  dtype = float)
        if menu_choice=="a":
            print("You selected Addition. The results are:")

            #converting it into numpy arrays
            mat1=np.array(mat1)
            mat2=np.array(mat2)

            #Adding The matrix
            Addition=mat1+mat2

            #Printing the addition matrix
            for r in range(0,3):
                for c in range(0,3):
                    print(Addition[r][c],end=" ")
                print()

            print("The Transpose is:")
            #Creating The Transpose Matrix
            Transpose=np.transpose(Addition)
            #Printing The Transpose Matrix
            for r in range(0,3):
                for c in range(0,3):
                    print(Transpose[r][c],end=" ")
                print()


            print("The row and column mean values of the results are:")

            #Finding row mean
            print("Row:",np.mean(Addition,axis=1))

            #Finding Column mean
            print("Column:",np.mean(Addition,axis=0))


        elif menu_choice=="b":
            print("You selected Subtraction. The results are:")

            #converting it into numpy arrays
            mat1=np.array(mat1)
            mat2=np.array(mat2)

            #Subtracting The matrix
            Subtraction=mat1-mat2
            #Printing the subtraction matrix
            for r in range(0,3):
                for c in range(0,3):
                    print(Subtraction[r][c],end=" ")
                print()

            print("The Transpose is:")
            #Creating The Transpose Matrix
            Transpose=np.transpose(Subtraction)
            #Printing The Transpose Matrix
            for r in range(0,3):
                for c in range(0,3):
                    print(Transpose[r][c],end=" ")
                print()


            print("The row and column mean values of the results are:")

            #Finding row mean
            print("Row:",np.mean(Subtraction,axis=1))

            #Finding Column mean
            print("Column:",np.mean(Subtraction,axis=0))

        elif menu_choice=="c":
            print("You selected Matrix Multiplication. The results are:")

            #converting it into numpy arrays
            mat1=np.array(mat1)
            mat2=np.array(mat2)

            #Multiplying The matrix using matmul function
            Multiplication=np.matmul(mat1,mat2)
            #Printing the subtraction matrix
            for r in range(0,3):
                for c in range(0,3):
                    print(Multiplication[r][c],end=" ")
                print()

            print("The Transpose is:")
            #Creating The Transpose Matrix
            Transpose=np.transpose(Multiplication)
            #Printing The Transpose Matrix
            for r in range(0,3):
                for c in range(0,3):
                    print(Transpose[r][c],end=" ")
                print()


            print("The row and column mean values of the results are:")

            #Finding row mean
            print("Row:",np.mean(Multiplication,axis=1))

            #Finding Column mean
            print("Column:",np.mean(Multiplication,axis=0))

        elif menu_choice=="d":
            print("You selected Element by Element Multiplication. The results are:")
            #converting it into numpy arrays
            mat1=np.array(mat1)
            mat2=np.array(mat2)
            #Multiplying The matrix elementwise
            Element=mat1 * mat2
            #Printing the subtraction matrix
            for r in range(0,3):
                for c in range(0,3):
                    print(Element[r][c],end=" ")
                print()

            print("The Transpose is:")
            #Creating The Transpose Matrix
            Transpose=np.transpose(Element)
            #Printing The Transpose Matrix
            for r in range(0,3):
                for c in range(0,3):
                    print(Transpose[r][c],end=" ")
                print()
            print("The row and column mean values of the results are:")

            #Finding row mean
            print("Row:",np.mean(Element,axis=1))

            #Finding Column mean
            print("Column:",np.mean(Element,axis=0))
    else:
        print("*********** Thanks for playing Python Numpy ***************")
        break
        