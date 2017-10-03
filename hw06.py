from flask import Flask, render_template, request
my_app = Flask (__name__)

@my_app.route('/')
def root():
    return render_template("hw06.html")

@my_app.route('/form')
def form():
    return render_template("greetings.html", user_input = request.args['userInput'])

if __name__ == '__main__':
    my_app.debug = True
    my_app.run()
    
