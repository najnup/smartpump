from random import randrange
from flask import Flask,render_template,request

def check_password(username, password):
    passwords_file = 'login_info.txt'
    with open(passwords_file, mode='r') as file:
        for line in file:
            if username == line.split()[0] and password == line.split()[1]:
                return True
            else:
                continue
    return False

def chaos_fail_monkey():
    ## Something should fail in case monkey retruns True
    dice = randrange(1,100)
    if dice > 80:
        print(dice)
        return True
    else:
        print(dice)
        return False

app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/fillorder', methods = ['POST', 'GET'])
def fillorder():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        form_data = request.form

        if check_password(form_data['User'], form_data['Password']):
            return render_template('fillorder.html',form_data = form_data)
        else:
            return render_template('error.html')

@app.route('/data', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        ## Implementing here some Random fails
        if chaos_fail_monkey():
            return render_template('order_error.html')
        
        else:       
            form_data = request.form
            return render_template('data.html',form_data = form_data)

@app.route('/about')
def about():
    return render_template('about.html')

app.run(host='0.0.0.0', port='5000', ssl_context='adhoc')

