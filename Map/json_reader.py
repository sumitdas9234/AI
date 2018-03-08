import json

with open('map.json') as json_file:
    data = json.load(json_file)
    for building in data['buildings']:
        print('Name: ' + building['name'])
        print(building['color'])
        print(building['location'])
        print('')
