import requests

response = {
    "items": [
        {
            "name": "Jyoti",
            "address": {
                "home": "test home address",
                "office": "test office address"
            }
        },
        {
            "name": "Priyanka",
            "address": {
                "home": "test home address",
                "office": "test office address"
            }
        }
    ]
}

items = response.get("items")

for i in items:
    if isinstance(i, dict) and i["name"] == "Priyanka":
        print(i["address"]["home"])
        break

baseUri = "www.example.com"
endPoint = "/a"
jwtToken = ""
url = baseUri + endPoint
headers = {"Authorization": "Bearer %s" % jwtToken,
           "Content-Type": "application/json"}
payload = {"key": "value"}
postResponse = requests.post(url, headers=headers, data=payload)
