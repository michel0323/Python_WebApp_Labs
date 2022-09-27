import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data from housing.csv and Popchange.csv and store it in numpy arrays as well as pandas dataframe for analysis
housing = pd.read_csv('Housing.csv')
houd = np.array(housing)
population = pd.read_csv('PopChange.csv')
popd = np.array(population)


# Define calc_pop to calculate statistics for population change columns
def calc_pop(num):
    print(" The Statistics For This Column Are: ")
    num = int(num)
    count = 0
    mean = 0
    min = 0
    max = 0
    sdev = 0
    # use pandas iloc and functions to get statistics column indexed at value num
    mean = round(population.iloc[:, num].mean(), 1)
    sdev = round(population.iloc[:, num].std(), 1)
    max = round(population.iloc[:, num].max(), 1)
    min = round(population.iloc[:, num].min(), 1)
    count = len(population.iloc[:, num])

    print(" Count = " + str(count))
    print(" Mean = " + str(mean))
    print("Standard deviation = ", sdev)
    print(" Min = " + str(min))
    print(" Max = " + str(max))
    n, bins, patches = plt.hist(popd[:, num], 50, density=True, facecolor="b"
                                , alpha=0.75)
    plt.grid(True)
    plt.show()


# Define get_pop that prompts for column name in population change csv and display the histogram
def get_pop():
    while True:
        print("\n")
        print(" You Have Entered Population Data. ")
        print("a. Pop Apr 1")
        print("b. Pop Jul 1")
        print("c. Change Pop")
        print("d. Exit Column")
        pick = input(" Please Enter Your Selection a - d: ").capitalize()

        if pick == "A":
            calc_pop(4)

        elif pick == "B":
            calc_pop(5)

        elif pick == "C":
            calc_pop(6)

        elif pick == "D":

            print("You selected to exit the column menu ")

            break


# Define calc_hou function that analyzes housing data and gets column statistics
def calc_hou(num):
    print(" The Statistics For This Column Are: ")
    num = int(num)
    count = 0
    mean = 0
    min = float(houd[count][num])
    max = float(houd[count][num])
    sdev = 0
    # use pandas iloc and functions to get statistics column indexed at value num
    mean = round(housing.iloc[:, num].mean(), 2)
    count = round(len(housing.iloc[:, num]), 2)
    min = round(housing.iloc[:, num].min(), 2)
    max = round(housing.iloc[:, num].max(), 2)
    sdev = round(housing.iloc[:, num].std(), 2)

    print(" Count = " + str(count))
    print(" Mean = " + str(mean))
    print("Standard Deviation = " + str(sdev))
    print(" Min = " + str(min))
    print(" Max = " + str(max))

    n, bins, patches = plt.hist(houd[:, num], 10, density=True, facecolor="b", alpha=0.75)
    plt.grid(True)
    plt.show()


# prompts user to input the column to be analyzed and display the histogram
def get_hou():
    while True:
        print("\n")
        print(" You Have Entered Housing Data. ")
        print(" Select The Column You Want to Analyze")
        print("a. Age")
        print("b. Bedroom")
        print("c. Built Year")
        print("d. Rooms")
        print("e. Utility")
        print("f. Exit Columns")
        pick = input(" Please Enter Your Selection a - f: ").capitalize()

        if pick == "A":
            calc_hou(0)

        elif pick == "B":
            calc_hou(1)

        elif pick == "C":
            calc_hou(2)

        elif pick == "D":
            calc_hou(4)

        elif pick == "E":
            calc_hou(6)

        elif pick == "F":

            print("You selected to exit the column menu ")
            break


print("***************** Welcome to the Python Data Analysis App**********")
# Main Program
while True:
    # Display Menu

    print("Select the file you want to analyze:")
    print("1. Population Data ")
    print("2. Housing Data ")
    print("3. Exit The Program ")

    # This is the Menu part of my program
    try:
        pic = int(input("Enter A Selection 1 - 3: "))
    except:
        print("Try Again. Please Pick 1 - 3: ")

    if pic == 1:
        # Call get_pop function to analyze population changd data
        get_pop()

    elif pic == 2:
        # Call get_hou function to analyze population changd data
        get_hou()

    elif pic == 3:
        print("*************** Thanks for using the Data Analysis App**********.")
        break

    else:
        print("Try Again. Please Pick 1 - 3: ")