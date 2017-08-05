import requests
import json
from requests.auth import HTTPBasicAuth
import base64
import inspect

#r = requests.get('https://github.com', verify=True)
user = "annaVVV"
password = 'password'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
#r = requests.get('https://api.github.com/users/annaVVV', auth=('annaVVV', '12345678a'))
uri1 = 'https://api.github.com/users/' + user
server = "https://api.github.com"
url = server + "/gists"
r = requests.get(uri1,auth=(user,password)) # auth=HTTPBasicAuth(user,password))

print r  #<Response [200]>
print 'Status:', r.status_code
print 'headers:', r.headers['content-type']
print 'encoding:', r.encoding
print 'text', r.text

try:
    json_resp = json.loads(r.content)
except ValueError:
    json_resp = 'NoJSON'
print 'json',json_resp

# method = 'GET'
# server = "https://api.github.com"
# url = server + "/user"
# headers = dict()

#
#
# print "checking ", url, "using user:", user
