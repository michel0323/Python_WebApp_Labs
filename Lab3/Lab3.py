# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 01:14:22 2022

@author: Michel T.
@INSTRUCTOR: Kyle Johnson
@School: UMGC
@Course: SDEV 300 Building Secure Python Applications
"""

import sys
import matplotlib.pyplot as plt
# import numpy as np

from PIL import Image
import requests
from io import BytesIO

# define an empty list which will carry all the data
state = []

# state.append inserts the contents to the list n2amed state
state.append ( ['Alabama', 'Montgomery', 4903185, 'Camellia','https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/camellia-flower.jpg?itok=K1xKDUI5'] )
state.append ( ['Alaska', 'Juneau', 731545, 'Forget-Me-Not', 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Oak_leaf_hydrangea380.jpg?itok=oKb8UNHC' ] )
state.append ( ['Arizona', 'Phoenix', 7278717, 'Saguaro Catus Blossom'] )
state.append ( ['Arkansas', 'Little Rock', 3017825, 'Apple Blossom'] )
state.append ( ['California', 'Sacramento ', 39512223, 'Golden Poppy'] )
state.append ( ['Colorado', 'Denver', 5758736, 'Mountain Columbine'] )
state.append ( ['Connecticut', 'Hartford', 3565287, 'Mountain Laurel'] )
state.append ( ['Delaware', 'Dover', 973764, 'Peach Blossom'] )
state.append ( ['Florida', 'Tallahassee', 21477737, 'Orange Blossom'] )
state.append ( ['Georgia', 'Atlanta', 10617423, 'Cherokee Rose'] )
state.append ( ['Hawaii', 'Honolulu', 415872, 'Red Hibiscus'] )
state.append ( ['Idaho', 'Boise', 1787065, 'Syringa'] )
state.append ( ['Illinois', 'Springfield', 12671821, 'Violet'] )
state.append ( ['Indiana', 'Indianaplis', 6732219, 'Peony'] )
state.append ( ['Iowa', 'Des Moines', 3155070, 'Wild Rose'] )
state.append ( ['Kansas', 'Topeka', 2913314, 'Sunflower'] )
state.append ( ['Kentucky', 'Frankfort', 4467673, 'Goldenrod'] )
state.append ( ['Louisiana', 'Baton Rouge', 4648794, 'Magnolia'] )
state.append ( ['Maine', 'Augusta', 1344212, 'Pine Cone & Tassel'] )
state.append ( ['Tennessee', 'Nashville', 6833174, 'Iris'] )
state.append ( ['Maryland', 'Annapolis', 6045680, 'Black-eyed Susan'] )
state.append ( ['Deleware', 'Dover', 973764, 'Peach Blossom'] )
state.append ( ['Massachusettes', 'Boston', 6949503, 'Mayflower'] )
state.append ( ['Rhode Island', 'Providence', 1059361, 'Violet'] )
state.append ( ['Minniesota', 'St.Paul', 5639632, 'Lady-Slipper'] )
state.append ( ['Mississippi', 'Jackson', 2976149, 'Magnolia'] )
state.append ( ['Missouri', 'Jefferson City', 6137428, 'Hawthorne'] )
state.append ( ['Michigan', 'Lansing', 9986857, 'Apple Blossom'] )
state.append ( ['Montana', 'Helena', 1068778, 'Bitterroot'] )
state.append ( ['Nebraska', 'Lincoln', 1934408, 'Goldenrod'] )
state.append ( ['Nevada', 'Carson City', 3080156, 'Sagebrush'] )
state.append ( ['New Hampshire', 'Concord', 1359711, 'Purple Lilac'] )
state.append ( ['Vermont', 'Montpelier', 623989, 'Red Clover'] )
state.append ( ['New Jersey', 'Trenton', 8882190, 'Violet'] )
state.append ( ['New Mexico', 'Santa Fe', 2096829, 'Yucca'] )
state.append ( ['New York', 'Albany', 19453561, 'Rose'] )
state.append ( ['North Carolina', 'Raleigh', 10488084, 'Flowering Dogwood'] )
state.append ( ['Wyoming', 'Cheyenne', 78759, 'Indian Paintbrush'] )
state.append ( ['North Dakota', 'Bismark', 762062, 'Prairie Rose'] )
state.append ( ['Ohio', 'Columbus', 11689100, 'Scalet Carnation'] )
state.append ( ['Oklahoma', 'Oklahoma City', 3956971, 'Mistletoe'] )
state.append ( ['Oregon', 'Salem', 4217737, 'Oregon Grape'] )
state.append ( ['Pennsylvania', 'Harrisburg', 12801989, 'Mountain Laurel'] )
state.append ( ['South Carolina', 'Columbia', 5148714, 'Yellow Jessamine'] )
state.append ( ['South Dakota', 'Pierre', 88465, 'Pasque flower'] )
state.append ( ['Texas', 'Austin', 28995881, 'Bluebonnet'] )
state.append ( ['Utah', 'Salt Lake City', 3202985, 'Sego Lily'] )
state.append ( ['Virginia', 'Richmond', 8535519, 'Dogwood'] )
state.append ( ['Washington', 'Olympia', 7614893, 'Coast Rhododendron'] )
state.append ( ['West Virginia', 'Charleston', 1792147, 'Rhododendron'] )
state.append ( ['Wisconsin', 'Madison', 5822434, 'Wood Violet'] )
state.sort()



def state_list():
    # Return list of states
    pass

# def display_sorted_states():
# toString
# Display all U.S. States in Alphabetical order along with the Capital, State Population, and Flower

def display_sorted_states():
    print ( "State\t\t", " Capital\t\t", " Population\t\t", " Flower\t\t" ),
    # Display all U.S. States in Alphabetical order along with the Capital, State Population, and Flower
    for i in range ( 0, 51 ):
        print ( state[i][0], "\t\t", state[i][1], "\t\t", state[i][2], "\t\t", state[i][3] )
    # https://statesymbolsusa.org/symbol/alabama/state-flower/camellia

pass


def search_state_display():
    state_name = input ( 'Input your State:  ' )
    print ( "State\t", " Capital\t", " Population\t", " Flower\t" )
    for i in range (0, 51):
        if state_name == (state[i][0]):
            response = requests.get((state[i][4]))
            img = Image.open(BytesIO(response.content))
            print ( state[i][0],"\t", state[i][1],"\t", state[i][2],"\t", state[i][3] ,img.show())

        if i == 51: print("Invalid State Name")
    pass


def display_bar_graph_top5():
    plt.plot ( [1, 2, 3, 4] )
    plt.ylabel ( 'some numbers' )
    plt.show ()
    #  Bar graph of the top 5 populated States showing their overall population
    pass


def update_population_for_State(state):
    # Update the overall state population for a specific state.
    pass


def state_population(state):
    population = state.stateString ( 2 ),
    pass


user_input = 1
while True:
    print (
        '\n1. Display all U.S. States in Alphabetical order along with the Capital, State Population, and Flower ' ),
    print (
        '2. Search for a specific state and display the appropriate Capital name, State Population, and an image of',
        'the associated State Flower. ' ),
    print ( '3. Provide a Bar graph of the top 5 populated States showing their overall population ' ),
    print ( '4. Update the overall state population for a specific state. ' ),
    print ( '5. Exit the program ' ),
    user_input = int ( input ( '\nEnter choices : ' ) )
    # add check for int between 1 and 5 else message and return to menu
    # if user_input ( 0> or 5< ), then

    if user_input == 1:
        # Display all U.S. States in Alphabetical order along with the Capital, State Population, and Flower
        display_sorted_states ()

    elif user_input == 2:
        # Search for a specific state and display the appropriate Capital name, State Population, and an image of the
        # associated State Flower.
        # using this would be cool us.states.STATES to check for valid state name
        search_state_display ()

    elif user_input == 3:
        # Bar graph of the top 5 populated States showing their overall population
        # elif (user_input == 4 ):
        # Update the overall state population for a specific state.
        state_name = input ( '\nEnter State Name:  ' )
        bird_name = input ( '\nEnter State population:  ' )
        update_population_for_State ( state_name )

    elif user_input == 5:
        # Exit the program
        print("**************************** Good Bye!! *****************************************")
        sys.exit ()

    elif user_input >= 6:
        print('Please only enter a value between 1 and 5')
