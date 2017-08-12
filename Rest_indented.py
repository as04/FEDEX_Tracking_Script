import requests
import json
trackNum=input("Input ")       #"777255010172"

data = {
    'data': json.dumps({
        'TrackPackagesRequest': {
            
            'trackingInfoList': [{
                'trackNumberInfo': {
                    'trackingNumber': trackNum,
                }
            }]
        }
    }),
    'action': 'trackpackages',
}

#print data

r = requests.post('https://www.fedex.com/trackingCal/track',  data=data)
response = r.json()
print(r)
#print(response)
shipDate = response['TrackPackagesResponse']['packageList'][0]['displayShipDt']
event = response['TrackPackagesResponse']['packageList'][0]['scanEventList'][0]
status  = event['status']
deliveryDate = event['date']
time = event['time']

output = {"tracking no":trackNum, "ship date":shipDate, "status":status, "scheduled delivery":deliveryDate+" "+time}
print json.dumps(output)
