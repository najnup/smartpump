import json
import requests
from datetime import datetime




### Variables
url = "https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,EUR,EUR"




### Write function, that creates Table of times and coresponding prices, for proviced day and stores in dictionary
def pool_prices(day_date = datetime.now()):
    ### day_date - has to be a datetime object
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
        print(prices_dict)
        return prices_dict

    else:
        print('Something went South!')


def get_price(time = datetime.now()):
    ### Provide the time when needed
    ### is using sort of global dictionary.
    pass

print("so far here!")

if __name__ == "__main__":
    print("This is the part that will run!")
    pool_prices()