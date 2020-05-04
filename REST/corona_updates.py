import requests
import json

def main():

    # Create a request
    method = 'GET'
    URL = 'https://thevirustracker.com/free-api?countryTimeline=US'
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
    r = requests.request(method='GET', url=URL, headers=headers)
    js_resp = json.loads(r.content)
    date = '5/03/20'
    update = js_resp['timelineitems'][0][date]
    
    # display data
    print(update)
    
if __name__ == "__main__":
    main()   
    
# Output:
# {u'total_recoveries': 0, u'total_cases': 1157687, u'total_deaths': 67674, u'new_daily_cases': 29975, u'new_daily_deaths': 1599}
