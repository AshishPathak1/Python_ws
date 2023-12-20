# write a program to print all the district Id from tamilnadu
# given the district_id print name of all the talukas from that district
# "http://vocab.nic.in/cla.php?cat=mast&info=taluk&state=tn&format=json"

import urllib.request
import json

def get_taluka_data(my_url):
    import pprint as pp
    response = urllib.request.urlopen(my_url)
    data = response.read().decode("utf-8")
    pp.pprint( json.loads(data))

def get_taluka_by_id(decoded_json):
    taluk_id = input('Please enter the taluka ID: ')
    for taluka_data in decoded_json["taluks"]:
        if taluka_data["taluk"]["taluk_id"] == taluk_id:
            print(f'Taluka ID: {taluk_id}')
            print(f'Taluka Name: {taluka_data["taluk"]["taluk_name"]}')
            break
    else:
        print(f"Taluka with ID {taluk_id} does not exist")

def explore_talukas_by_starting_letter(decoded_json):
    starting_letter = input('Please enter the first letter of the talukas: ').upper()
    matching_talukas = []

    for taluka_data in decoded_json["taluks"]:
        taluka_name = taluka_data["taluk"]["taluk_name"]
        if taluka_name.startswith(starting_letter):
            matching_talukas.append(taluka_name)

    if matching_talukas:
        print(f'Talukas starting with letter {starting_letter}:')
        for taluka_name in matching_talukas:
            print(taluka_name)
    else:
        print(f"No talukas found starting with letter {starting_letter}")


if __name__ == '__main__':
    url = "http://vocab.nic.in/cla.php?cat=mast&info=taluk&state=tn&format=json"
    json_data = get_taluka_data(url)
    # get_taluka_by_id(json_data)
    # explore_talukas_by_starting_letter(json_data)
