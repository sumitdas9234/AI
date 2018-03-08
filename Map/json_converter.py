import json
data = {}
data['buildings'] = []
data['buildings'].append({
    'name': 'Entrance',
    'color': (89, 98, 117,1.0),
    'location':[(2,24),(2,23),(2,21),(2,20)]
})
data['buildings'].append({
    'name': 'Energy House',
    'color': (231, 127, 103,1.0),
    'location':[(7,19),(8,19),(7,20),(8,20),(9,19),(9,20)]
})
data['buildings'].append({
    'name': 'Block I',
    'color': (89, 98, 117,1.0),
    'location':[(7,17),(8,17),(7,16),(10,16),(7,15),(10,15),(7,14),(8,14),(9,14),(10,14),(9,17),(10,17)]
})
data['buildings'].append({
    'name': 'Block II',
    'color': (89, 98, 117,1.0),
    'location':[(13,14),(14,14),(12,14),(13,13),(14,13),(12,13)]
})
data['buildings'].append({
    'name': 'Block III',
    'color': (89, 98, 117,1.0),
    'location':[(16,14),(17,14),(18,14),(16,13),(17,13),(18,13)]
})
data['buildings'].append({
    'name': 'Block IV',
    'color': (89, 98, 117,1.0),
    'location':[(13,17),(14,17),(12,17),(13,18),(14,18),(12,18)]
})
data['buildings'].append({
    'name': 'Block VI',
    'color': (89, 98, 117,1.0),
    'location':[(13,7),(14,7),(12,7),(13,6),(14,6),(12,6)]
})
data['buildings'].append({
    'name': 'Block V',
    'color': (89, 98, 117,1.0),
    'location':[(16,18),(17,18),(18,18),(16,17),(17,17),(18,17)]
})
data['buildings'].append({
    'name': 'Block VII',
    'color': (89, 98, 117,1.0),
    'location':[(16,7),(17,7),(18,7),(16,6),(17,6),(18,6)]
})
data['buildings'].append({
    'name': 'Block VIII',
    'color': (89, 98, 117,1.0),
    'location':[(25,12),(26,12),(27,12),(25,11),(26,11),(27,11),(28,11),(28,12)]
})
data['buildings'].append({
    'name': 'Block X',
    'color': (89, 98, 117,1.0),
    'location':[(30,12),(31,12),(32,12),(30,11),(31,11),(32,11),(33,11),(33,12)]
})
data['buildings'].append({
    'name': 'Block XI',
    'color': (89, 98, 117,1.0),
    'location':[(35,12),(36,12),(37,12),(35,11),(36,11),(37,11),(38,11),(38,12)]
})
data['buildings'].append({
    'name': 'Food Court',
    'color': (109, 33, 79,1.0),
    'location':[(19,21),(14,21),(15,21),(16,21),(17,21),(19,20),(18,21),(18,20),(14,20),(15,20),(16,20),(17,20)]
})
data['buildings'].append({
    'name': 'Cafeteria',
    'color': (252, 66, 123,1.0),
    'location':[(20,15),(20,16)]
})
data['buildings'].append({
    'name': 'New Amphi',
    'color': (189, 197, 129,1.0),
    'location':[(24,13),(22,13),(23,13),(24,12),(22,12)]
})
data['buildings'].append({
    'name': 'Fighter Jet',
    'color': (89, 98, 117,1.0),
    'location':[(25,7),(26,7),(27,7),(25,6),(26,6),(27,6),(28,6),(28,7)]
})
data['buildings'].append({
    'name': 'Hostel A',
    'color': (89, 98, 117,1.0),
    'location':[(30,7),(31,7),(32,7),(30,6),(31,6),(32,6),(33,6),(33,7)]
})
data['buildings'].append({
    'name': 'R & D Lab',
    'color': (89, 98, 117,1.0),
    'location':[(35,7),(36,7),(37,7),(35,6),(36,6),(37,6),(38,6),(38,7),(35,8),(36,8),(37,8),(38,8)]
})
data['buildings'].append({
    'name': 'Gandhi Chowk',
    'color': (44, 58, 71,1.0),
    'location':[(23,9)]
})
data['buildings'].append({
    'name': 'Grass',
    'color': (50, 255, 126,1.0),
    'location':[(9,16),(8,16),(9,15),(8,15)]
})
data['buildings'].append({
    'name': 'Tree',
    'color': (50, 255, 126,1.0),
    'location':[(20,6)]
})
data['buildings'].append({
    'name': 'Library',
    'color': (89, 98, 117,1.0),
    'location':[(6,2),(7,2),(8,2),(6,3),(7,3),(8,3),(6,4),(7,4),(8,4)]
})
data['buildings'].append({
    'name': 'Block IX',
    'color': (89, 98, 117,1.0),
    'location':[(15,2),(15,3),(16,2),(16,3),(17,2),(17,3)]
})
data['buildings'].append({
    'name': 'IT Tower',
    'color': (89, 98, 117,1.0),
    'location':[(11,2),(12,2),(13,2),(11,3),(12,3),(13,3),(11,4),(12,4),(13,4)]
})
data['buildings'].append({
    'name': 'Divider',
    'color': (255, 77, 77,1.0),
    'location':[(25,9),(26,9),(27,9),(28,9),(29,9),(30,9),(31,9),(32,9),(33,9),(19,9),(18,9),(17,9),(16,9),(15,9),(14,9),(12,9),
    (11,9),(10,9)]
})
print(data)
with open('map.json', 'w') as outfile:
    json.dump(data,outfile, sort_keys=True, indent=2)
outfile.close()
