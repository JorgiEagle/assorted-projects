from bs4 import BeautifulSoup
from collections import defaultdict
import requests
import re
import csv
'''
Returns a dictionary, for which the first element is is the value as an int and the second is the key, 
the given list normally has two elements, material and number needed, in the case of there being one, then the number
needed is infered to be one
:param list of materials and number needed
returns dictionary
'''


def write_material_to_file(write_file_, material_, artefact_, individual_amount_, amount_needed_, materials_needed_):
    write_file_.write('Material: ' + material_ + '\nArtefact: ' + artefact_ + '\nIndividual amount: ' + str(individual_amount_) + '\nAmount needed: ' + str(amount_needed_) + '\nTotal: ' + str(individual_amount_*amount_needed_))
    write_file_.write('\n\n' + str(materials_needed_) + '\n\n\n')


def write_main_output_to_file(write_file_output, artefact_materials_output, all_artefacts_output, materials_needed_output):
    write_file_output.write('Artefact Materials\n\n')
    separator = '\t'
    for key, value in artefact_materials_output.items():
        write_file_output.write(key + '\n')
        for mat_dic in value:
            for material, amount in mat_dic.items():
                write_file_output.write((separator + material + separator + str(amount) + '\n'))
    write_file_output.write('\nAll Artefacts\n\n')
    for key, value in all_artefacts_output.items():
        write_file_output.write(key + separator + str(value) + '\n')
    write_file_output.write('\nMaterials Needed\n\n')
    for key, value in materials_needed_output.items():
        write_file_output.write(key + separator + str(value) + '\n')


def write_main_output_to_file_csv(write_file_output, artefact_materials_output, all_artefacts_output, materials_needed_output):
    separator = ','
    csv_writer = csv.writer(write_file_output, delimiter=separator)
    csv_writer.writerow(['Artefact Materials'])
    for key, value in artefact_materials_output.items():
        csv_writer.writerow([key])
        for mat_dic in value:
            [csv_writer.writerow(['',material, amount]) for material, amount in mat_dic.items()]
    csv_writer.writerow(['All Artefacts'])
    [csv_writer.writerow([key, value]) for key, value in all_artefacts_output.items()]
    csv_writer.writerow(['Materials Needed'])
    [csv_writer.writerow([key, value]) for key, value in materials_needed_output.items()]


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


if input('Write as a CSV file? (Y/N)').upper() == 'Y':
    file_format = 'csv'
    csv_file_ = True
else:
    file_format = 'txt'
    csv_file_ = False

with open('runescape_arch_materials.' + file_format, 'w', newline='') as write_file:
    if csv_file_:
        write_main_output_to_file_csv(write_file, artefact_materials, all_artefacts, materials_needed)
    else:
        write_main_output_to_file(write_file, artefact_materials, all_artefacts, materials_needed)
