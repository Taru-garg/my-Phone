import requests
import json
api_key = 'acc_4789f20196cd49d'
api_secret = '8a15436aeb272e9e498d68db95af7fd9'
image_path = '/home/vip/Pictures/parrot.jpg'

response = requests.post(
    'https://api.imagga.com/v2/tags?limit=3',
    auth=(api_key, api_secret),
    files={'image': open(image_path, 'rb')})
jsonresponse=response.json()
print(jsonresponse['result']["tags"][0]['tag']["en"])
print(jsonresponse['result']["tags"][1]['tag']["en"])
print(jsonresponse['result']["tags"][2]['tag']["en"])

