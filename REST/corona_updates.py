############################################################################################
# Created example how to get Covid-19 updates for US by date
# Source: 
#   https://documenter.getpostman.com/view/8854915/SzS7R74n?version=latest#08adba6b-8533-42c2-a30f-bdb00eac5925
# Used: GET Country Timeline API
#   curl --location --request GET 'https://thevirustracker.com/free-api?countryTimeline=US'
############################################################################################
import requests
import json
import datetime

def main():
    # Create a request
    method = 'GET'
    URL = 'https://thevirustracker.com/free-api?countryTimeline=US'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    r = requests.request(method=method, url=URL, headers=headers)
    status = resp.status_code
    print('Response Status Code:', status)
    if status== 200:
        js_resp = json.loads(r.content)
        # Get today date in format like '05/03/20'
        date = datetime.datetime.now().strftime("%m/%d/%y")
        update = js_resp['timelineitems'][0][date]    
        # display data
        print(update)
    
if __name__ == "__main__":
    main()   
    
# Output:
# {u'total_recoveries': 0, u'total_cases': 1157687, u'total_deaths': 67674, u'new_daily_cases': 29975, u'new_daily_deaths': 1599}
