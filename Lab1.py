
"""
Created on Thu Aug 18 23:02:35 2022

@author: Michel T.
@INSTRUCTOR: Kyle Johnson
@School: UMGC
@Course: SDEV 300 Building Secure Python Applications
"""
print("Welcome to the Python Voter Registration Application")

Flag: str = str(input("\nDo you want to continue with Voter Registration? (Y/N): "))

if Flag == 'Y' or Flag == 'y':

    First: str = str(input("What is your first name: "))

    Flag = str(input("\nDo you want to continue with Voter Registration? (Y/N): "))

    if 'Y' != Flag and Flag != 'y':
        pass
    else:
        Last = str(input("What is your last name: "))

        Flag = str(input("\nDo you want to continue with Voter Registration? (Y/N): "))

        if 'Y' == Flag or Flag == 'y':

            Age = int(input("What is your Age: "))

            if Age < 18:

                Flag = 'n'

            else:

                Flag = str(input("\nDo you want to continue with Voter Registration? (Y/N): "))

                if "Y" == Flag or Flag == 'y':

                    US = str(input("Are you US citizen? (Y/N)"))

                    Flag = str(input("\nDo you want to continue with Voter Registration? (Y/N): "))

                    if 'Y' == Flag or Flag == 'y':

                        State: str = str(input("What state do you live? "))

                        Flag = str(input("\nDo you want to continue with Voter Registration? (Y/N): "))

                        if Flag == 'Y' or Flag == 'y':

                            Zip: str = str(input("Enter your zip code: "))

                            print("\nThanks for registering to vote. Here are the information we received.")

                            print("\nName (first, last): %s %s" % (First, Last))

                            print("Age: %d" % Age)

                            if US != 'Y' and US != 'y':
                                print("U.S. Citizen: NO")

                            else:
                                print("U.S. Citizen: YES")

                            print("State: %s" % State)

                            print("Zip Code: %s" % Zip)

                            print("\nThanks for trying the Voter Registration Application.")

                            print("Your Voter Registration Card should be shipped within 3 weeks.")
