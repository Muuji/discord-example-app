import requests

API_ENDPOINT = 'https://discord.com/api/v8'
CLIENT_ID = '995465896363577465'
CLIENT_SECRET = 'OODYEaqAkQwG-i95bv-Ze1V3_L_jxgSg'
REDIRECT_URI = 'https://google.com/'

def exchange_code(code):
  data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': REDIRECT_URI
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post('%s/oauth2/token' % API_ENDPOINT, data=data, headers=headers)
  r.raise_for_status()
  return r.json()

def add_to_guild(access_token, userID):
        url = f"{API_ENDPOINT}/guilds/988147732751478784/members/{userID}"

        botToken = "OTk1NDY1ODk2MzYzNTc3NDY1.GoKgFt.fuufwBYANMpEPu9Q1GW1_A3vxi-kI614xdaPO0"
        data = {
        "access_token" : access_token,
    }
        headers = {
        "Authorization" : f"Bot {botToken}",
        'Content-Type': 'application/json'

    }
        response = requests.put(url=url, headers=headers, json=data)
        print(response.text)

code = exchange_code('yMbumAHGD6UpyEGwauK8ljH3tpBllg')['access_token']
print(code)
add_to_guild(code, '988147732751478784')
