import json
import requests
from datetime import datetime

## url = "https://www.nordpoolgroup.com/Market-data1/Dayahead/Area-Prices/LV/Hourly/?view=table"
### For price confirmation GET https://www.nordpoolgroup.com/api/pricesconfirmed/
### Returns Date when prices got confirmed
##url = 'https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,EUR,EUR&endDate=10-02-2022'

url = "https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,EUR,EUR"

### Format 2022-02-10T01:00:00
### %Y-%m-%dT%H:%M:%S

dt_object1 = datetime.strptime('2022-04-03T01:00:00', '%Y-%m-%dT%H:%M:%S')

if dt_object1 > datetime.now():
    print('dt is bigger than now')
else:
    print('now is bigger')

## Compile dictionary
## {0:"0-1", 1:"1-2", 2:"2-3", 3:"3-4", ...}


def pool_prices(date = datetime.now()):
    ## This functions retrieves electricity prices for certain date
    ## Starting from 00 until 24, returns dictionary
    pass


file_path = r'C:\Users\janis\OneDrive\2022 0002 - Smart Pump\Price Extraction\response.json'

##    for column in row['Columns']:
##       print(row['Columns']['Value'])

## 2022-02-10T00:00:00


## To get date in order to fetch prices

class NordPoolData():
    
    def __init__(self):
        self.url = "https://www.nordpoolgroup.com/api/marketdata/page/59?currency=,,EUR,EUR"
        ## url adition &endDate=16-02-2022
        
        ## URL to use
        url = self.url + '&endDate=' + 

 
        
        print('Init initiated!')
        


"""def pool_price(price_time = datetime.now()):
    ## Expecting datetime object. If no time passed then using current time

    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        print('Data Obtained successfully!')
    else:
        print('Something went sideways!')"""



def pool_price(self, current_time = datetime.now()):
    ## Prepare proper URL

    ## Columns are located - decoded['data']['Rows'][0]['Columns']
    ## Seperate row - decoded['data']['Rows'][0]['Columns'][0]

    ## Here extracting Price for certain time and date
    ## datetime.strptime('2022-02-10T01:00:00', '%Y-%m-%dT%H:%M:%S')
    for row in self.data['data']['Rows']:
        #print(row)
        if row['StartTime'] == '2022-02-17T00:00:00' and row['IsExtraRow']==False:
        #if (datetime.strptime(row['StartTime'], '%Y-%m-%dT%H:%M:%S') < self.time_now) and (self.time_now <= datetime.strptime(row['EndTime'], '%Y-%m-%dT%H:%M:%S')) and row['IsExtraRow']==False: ### We have proper Row here
            print(row)
            print('match')
            for column in row['Columns']:
                #print(row['Columns'])
                if column['CombinedName'] == '15-02-2022':
                    print(column['Value'])
                    self.price = column['Value']
                    return column['Value']

    print('No Price Found!')



if __name__ == "__main__":
    #To do
    price_lookup()

print("Loaded!")
