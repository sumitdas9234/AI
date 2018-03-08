import json
data = {}
data['pallete'] = []
data['pallete'].append({
    'name': 'Weisteria',
    'color': (142, 68, 173,1.0)
})
data['pallete'].append({
    'name': 'Alizarin',
    'color': (231, 76, 60,1.0)
})
data['pallete'].append({
    'name': 'Color1',
    'color': (183, 21, 64,1.0)
})
data['pallete'].append({
    'name': 'Color2',
    'color': (243, 104, 224,1.0)
})
data['pallete'].append({
    'name': 'Color3',
    'color': (120, 111, 166,1.0)
})


with open('pallete.json', 'w') as outfile:
    json.dump(data,outfile, sort_keys=True, indent=2)
outfile.close()
