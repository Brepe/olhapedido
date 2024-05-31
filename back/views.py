from flask import Blueprint, render_template


main = Blueprint('main', __name__)

# Define a route within the Blueprint
@main.route('/')
def home():
    data = {
        'title': 'Home Page',
        'welcome_message': 'Welcome to the Home Page!'
    }    
    return render_template('home.html', **data)
