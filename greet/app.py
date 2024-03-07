from flask import Flask

# Creating an instance of the Flask application
app = Flask(__name__)

@app.route('/welcome')
def say_welcome():
    return 'welcome'

@app.route('/welcome/home')
def say_welcomehome():
    return 'welcome home'

@app.route('/welcome/back')
def say_welcome_back():
    return 'welcome back'

if __name__ == '__main__':
    app.run()