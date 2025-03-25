import requests
import json
url = "https://api-app2.simpletexting.com/v2/api/messages"


payload = json.dumps({
      "contactPhone": "9363713307",
      "accountPhone": "2073679805",
      "mode": "AUTO",
      "text": "You Ready For Tonight?"
    })
headers = {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer 5b51659c5e9a5e3380c6bc3c7bd92f00'
    }

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

