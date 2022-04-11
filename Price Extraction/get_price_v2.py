#!/usr/bin/env python

"""
Description: This part for dayly electricity price extraction is used to decrease and maintain household electricity consumption. This part of code delivers current price avialable and makes current price more easily observable. Goal is to decrease electricity bill.
Author: NajNup
Start Date: 03.03.2022
Disclaimer: In this example NordPool price extraction is used for learning purposes not used for commercial purpose in any way. NordPool has data portal available, more details on - https://www.nordpoolgroup.com/en/services/power-market-data-services/dataportalregistration/
            All information here is used merely for educational and informational purposes. It is not intended as a substitute for professional advice. Should you decide to act upon any information here, you do so at your own risk.
"""

import json
import requests
from datetime import datetime

### Function, that creates Table of times and coresponding prices, for proviced day and stores in dictionary
### Currency EUR
### Units for results - EUR/MWh
### Timezone for resutls - UTC +1 or CET/CEST
### Latvia Time zone  GMT +3 or UTC +3
### CEST Time zone UTC +2
### Due to time zone LV results will be missinf first hour of the day
### Notes: In results there is 1 h offset. Results does not show locally 00-01 that is missing

### Variables
url = "https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,EUR,EUR"

### What is the time zone for the results???
def pool_prices(day_date = datetime.now()):
    ### day_date - has to be a datetime object
    ### Time will be presented in text. Example: 2022-04-03T01:00:00
    prices_dict = []
    request_url = url + "&endDate=" + day_date.strftime('%d-%m-%Y')

    r = requests.get(request_url)
    if r.status_code == 200:
        data = r.json()
        print('Data Obtained successfully!')
    
        for row in data['data']['Rows']:
            ### row['IsExtraRow']==False taking only main info
            if row['IsExtraRow']==False:
                for column in row['Columns']:
                    #print(row['Columns'])
                    if column['Name'] == day_date.strftime('%d-%m-%Y'):
                        print(row['StartTime'], row['EndTime'], column['Name'], column['Value'])
                        prices_dict.append({'StartTime':row['StartTime'], 'EndTime':row['EndTime'], 'Price':column['Value']})
        print('Prices Dictionary prepared')
        return prices_dict

    else:
        print('Something went South!')

def get_price(price_data, time = datetime.now()):
    ### Provide the time when needed
    ### is using sort of global dictionary.
    ### time example datetime.strptime('2022-04-03T01:00:00', '%Y-%m-%dT%H:%M:%S')
    for row in price_data:
        if (datetime.strptime(row['StartTime'],'%Y-%m-%dT%H:%M:%S') < time) and (datetime.strptime(row['EndTime'],'%Y-%m-%dT%H:%M:%S') > time):
            print(row['Price'])
            return row['Price']

def get_average(prices_data):
    ### Function is returning average prace for that day
    ### prices_data is expected to be a list
    sum_prices = 0

    ### Acumulate all days prices
    for row in prices_data:
        sum_prices += float(row['Price'].replace(',', '.'))
    print('Test!')
    print(sum_prices//len(prices_data))
    return (sum_prices//len(prices_data))

print('All functions defined!')

if __name__ == "__main__":
    print("This is the part that will run!")
    prices_data = pool_prices()
    ### Will have to do time zone adjustment
    get_price(prices_data)
    print('Average is!')
    get_average(prices_data)