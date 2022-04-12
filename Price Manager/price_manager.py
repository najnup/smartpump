#!/usr/bin/env python

"""

"""


from flask import Flask,render_template,request

app = Flask(__name__)

### Will copy something from the previous process
### Have to review these stuff, have forgotten. How that worked.

### Will have one page where current price is shown and it is red if the price is above average and green in case price falls below average price
### will have previous price and current price and next hours price available on same view.
### That is all for this site.



@app.route('/')
def home():
    return render_template('index.html')