from bs4 import BeautifulSoup
from collections import defaultdict
import requests
import re

'''
Returns a dictionary, for which the first element is is the value as an int and the second is the key, 
the given list normally has two elements, material and number needed, in the case of there being one, then the number
needed is infered to be one
:param list of materials and number needed
returns dictionary
'''
def dict_from_list(given_list):
    try:
        return {given_list[1]: int(given_list[0])}
    except IndexError:
        return {given_list[0]: 1}


def clean_entry(entry):
    cleaned = entry.text.strip().replace('\n', '_')
    cleaner_list = []
    for index, element in enumerate(cleaned.split('_')):
        if index == 1:
            continue
        if re.search(',', element):
            break
        cleaner_list.append(element.replace('-', ' '))
    return cleaner_list


def get_table(table_no):
    return tables[table_no].find_all('tr')


def extract_number_needed(given_table):
    pass


url = 'https://runescape.wiki/w/Artefact'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

tables = soup.findAll('table', class_='wikitable')

list_of_artefact_materials = get_table(3)

all_artefact_tables = [get_table(x) for x in range(5,12)]
'''
List of each source by table number 
kharid_et = 5
infernal_source = 6
everlight = 7
senntisten = 8
stormguard = 9
warforge = 10
orthen = 11
'''
# keys of this dictionary are the artefacts. The value is a list of dictionaries, the key for each is the material
# and the value is the number needed for that material
artefact_materials = dict()
for item in list_of_artefact_materials[2:]:
    cleaned_list = clean_entry(item)
    artefact_materials[cleaned_list[0]] = [dict_from_list(material.split(' x ')) for material in cleaned_list[5:-1]]

# iterate through all artefact tables, for every table extract the amount needed for every artefact, no two artefacts can
# come from different sources
all_artefacts = dict()
for table in all_artefact_tables:
    for artefact in table[1:]:
        artefact_raw = artefact.text.strip().replace('-', ' ').replace('\n', '_').split('_')
        all_artefacts[artefact_raw[0]] = int(artefact_raw[4])


materials_needed = defaultdict(int)
for artefact, amount_needed in all_artefacts.items():
    for material_dict in artefact_materials[artefact]:
        for material, individual_amount in material_dict.items():
            materials_needed[material] += individual_amount*amount_needed

with open('runescape.txt', 'w') as write_file:
    write_file.write('Artefact Materials\n\n')
    for key, value in artefact_materials.items():
        write_file.write(key + ' ' + str(value) + '\n')
    write_file.write('\n All Artefacts\n\n')
    for key, value in all_artefacts.items():
        write_file.write(key + ' ' + str(value) + '\n')
    write_file.write('\n Materials Needed\n\n')
    for key, value in materials_needed.items():
        write_file.write(key + ' ' + str(value) + '\n')
