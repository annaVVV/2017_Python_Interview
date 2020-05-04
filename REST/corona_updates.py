import requests
import json
############################################################################################
# Created example how to get Covid-19 updates for US by date
# Source: 
#   https://documenter.getpostman.com/view/8854915/SzS7R74n?version=latest#08adba6b-8533-42c2-a30f-bdb00eac5925
# Used: 
#   curl --location --request GET 'https://thevirustracker.com/free-api?countryTimeline=US'
############################################################################################

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
