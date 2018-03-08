import json
data = {}
data['graph'] = []
data['graph'].append({
    'name': 'Entrance',
    'neighbours': ['Energy House']
})
data['graph'].append({
    'name': 'Energy House',
    'neighbours': ['Block I']
})
data['graph'].append({
    'name': 'Block I',
    'neighbours': ['Block II', 'Block IV']
})
data['graph'].append({
    'name': 'Block II',
    'neighbours': ['Block III']
})
data['graph'].append({
    'name': 'Block IV',
    'neighbours': ['Block V', 'Food Court']
})
data['graph'].append({
    'name': 'Block III',
    'neighbours': ['Cafeteria']
})
data['graph'].append({
    'name': 'Block V',
    'neighbours': ['Food Court', 'Cafeteria']
})
data['graph'].append({
    'name': 'Food Court',
    'neighbours': ['Block V']
})
data['graph'].append({
    'name': 'Cafeteria',
    'neighbours': ['Block III', 'Block V']
})


with open('graph.json', 'w') as outfile:
    json.dump(data,outfile, sort_keys=True, indent=2)
outfile.close()
