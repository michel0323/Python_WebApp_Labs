'''Python language syntax for rendering HTML templates
 using the Python Flask module '''
from datetime import datetime
from flask import Flask, render_template

app = Flask('sdev300flaskapp',
            template_folder='templates')

# @Name: Michel T.## @Name: Michel T.
# @Instructor: Kyle Johnson.
# @Date: 09/25/22.
# @Class: Michel T.
# @Project: Lab6.py


@app.route('/')
def index(user='User'):
    """Routes to the main page"""
    nav = [
        {'name': 'Amazon', 'url': 'https://www.amazon.com/'},
        {'name': 'Google', 'url': 'https://www.google.com'},
        {'name': 'Twitter', 'url': 'https://www.twitter.com'}
    ]

    description = '''Amazon.com, Inc. is an American multinational technology company that
     focuses on e-commerce, cloud computing, digital streaming, and artificial intelligence.
    It has been referred to as "one of the most 
    influential economic and cultural forces in the world", 
    and is one of the world's most valuable brands. It is one of the Big 
    Five American information technology companies, alongside Alphabet, Apple, Meta, and Microsoft. 
    Amazon was founded by Jeff Bezos from his garage in Bellevue, Washington, on July 5, 1994. 
    Initially an online marketplace for books, it has expanded into a multitude of product categories: 
    a strategy that has earned it the moniker The Everything Store.
    It has multiple subsidiaries including Amazon Web Services (cloud computing), 
    Zoox (autonomous vehicles), 
    Kuiper Systems (satellite Internet), and Amazon Lab126 (computer hardware R&D). 
    Its other subsidiaries include Ring, Twitch, IMDb, and Whole Foods Market. 
    Its acquisition of Whole Foods in August 2017 for US$13.4 
    billion substantially increased its footprint as a physical retailer'''

    items = [
        'Amazon Fresh',
        'Amazon Prime',
        'Alexa',
        'Appstore',
        'Amazon Drive',
        'Amazon Digital Software & Video Games',
        'Kindle Store'
    ]

    time = datetime.now().isoformat(' ')

    return render_template(
        'home.html',
        user=user,
        nav=nav,
        title='Lab6',
        description=description,
        subtitle='WHAT WE DO',
        subsub='Amazon.com has a number of products and services available, including:',
        items=items,
        time=time
    )
