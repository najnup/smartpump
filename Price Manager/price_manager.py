#!/usr/bin/env python

from datetime import datetime
from datetime import timedelta

from get_price_v2 import *

"""
Description:
Author:
Date: 
"""

from flask import Flask,render_template,request
app = Flask(__name__)

### Will copy something from the previous process
### Have to review these stuff, have forgotten. How that worked.

### Will have one page where current price is shown and it is red if the price is above average and green in case price falls below average price
### will have previous price and current price and next hours price available on same view.
### That is all for this site.

### do an adjustment for LV time


print(LOCAL_TIME)
prices_data = pool_prices(LOCAL_TIME)

@app.route('/')
def home():
    
    before_price = get_price(prices_data,LOCAL_TIME - timedelta(hours=1))
    now_price = get_price(prices_data,LOCAL_TIME)
    future_price = get_price(prices_data,LOCAL_TIME + timedelta(hours=1))
    average_price = get_average(prices_data)

    title_date = LOCAL_TIME.strftime('%d-%m-%Y')
    return render_template('index.html', date = title_date, before_price = before_price, now_price = now_price, future_price = future_price, average_price = average_price)

app.run(host='0.0.0.0', port='8080')
