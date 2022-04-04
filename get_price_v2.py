import json
import requests
from datetime import datetime




### Variables
url = "https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,EUR,EUR"




### Write function, that creates Table of times and coresponding prices, for proviced day and stores in dictionary
def pool_prices(day_date = datetime.now()):
    ### day_date - has to be a datetime object
    ### will fetch prices and return Dictionary of the values
    ### Table
    ### StartTime # EndTime # Price
    ### Example -= 10-02-2022    %Y-%m-%dT%H:%M:%S
    request_url = url + "&endDate=" + day_date.strftime('%d-%m-%Y')

    r = requests.get(request_url)
    if r.status_code == 200:
        data = r.json()
        print('Data Obtained successfully!')
    
        for row in data['data']['Rows']:
            #print(row)
            if row['StartTime'] == '2022-04-03T00:00:00' and row['IsExtraRow']==False:
            #if (datetime.strptime(row['StartTime'], '%Y-%m-%dT%H:%M:%S') < self.time_now) and (self.time_now <= datetime.strptime(row['EndTime'], '%Y-%m-%dT%H:%M:%S')) and row['IsExtraRow']==False: ### We have proper Row here
                print(row)
                print('match')
                for column in row['Columns']:
                    #print(row['Columns'])
                    if column['CombinedName'] == '03-04-2022':
                        print(column['Value'])
                        price = column['Value']
                        return column['Value']

        print('No Price Found!')





    else:
        print('Something went sideways!')


def get_price(time = datetime.now()):
    ### Provide the time when needed
    ### is using sort of global dictionary.
    pass

print("so far here!")

if __name__ == "__main__":
    print("This is the part that will run!")
    pool_prices()