from json import *

with open('phare_de_France.json') as json_data:
    data_dict = load(json_data)
    
phares = {}
for i in range(len(data_dict['features'])):
    if data_dict['features'][i]['geometry']['type'] == 'Point':
        if list(data_dict['features'][i]['properties'].keys()).__contains__('name'):
            phares[data_dict['features'][i]['properties']['name'].replace('Ã©', 'e').replace('Ã¼', 'u').replace('Ã«', 'e').replace('ÃŽ', 'I').replace('Ãª', 'e').replace('Ã‰', 'E').replace('Ã´', 'o').replace('Ã®', 'I').replace('Ã¨', 'e').replace('Ã ', 'a').replace('Ã¢', 'a').lower()] = (data_dict['features'][i]['geometry']['coordinates'][0], data_dict['features'][i]['geometry']['coordinates'][1])

# si on veut afficher le dict
"""for i in range(len(list(phares.keys()))):
    print(list(phares.keys())[i], phares[list(phares.keys())[i]])"""