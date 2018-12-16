# Credit protocol information from https://github.com/MattTW/BlinkMonitorProtocol

import requests
import shutil
import os
import sys

if len(sys.argv) != 3:
    print('usage: ' + sys.argv[0] + ' email password')
    exit()

headers = {
    'Host': 'prod.immedia-semi.com',
    'Content-Type': 'application/json',
}
data = '{ "password" : "' + sys.argv[2] + '", "client_specifier" : "iPhone 9.2 | 2.2 | 222", "email" : "' + sys.argv[1] + '" }'
res = requests.post('https://rest.prod.immedia-semi.com/login', headers=headers, data=data)
authToken = res.json()["authtoken"]["authtoken"]
region = res.json()["region"]
region = list(region.keys())[0]
#print(region)

print(authToken)

headers = {
    'Host': 'prod.immedia-semi.com',
    'TOKEN_AUTH': authToken,
}

pageNum = 0
while True:
    pageNumUrl = 'https://rest-'+region+'.immedia-semi.com/api/v2/videos/page/' + str(pageNum)
    print(pageNumUrl)
    res = requests.get(pageNumUrl, headers=headers)
    videoListJson = res.json()
    if not videoListJson:
        break
    for videoJson in videoListJson:
        mp4Url = 'https://rest-'+region+'.immedia-semi.com' + videoJson["address"]
        print(mp4Url)
        res = requests.get(mp4Url, headers=headers, stream=True)
        with open(os.path.basename(mp4Url)[14:], 'wb') as out_file:
            shutil.copyfileobj(res.raw, out_file)
    pageNum += 1
