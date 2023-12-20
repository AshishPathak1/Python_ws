# fetching country data and getting th ecountry name given the county code
# 
import urllib.request
import json

def get_json_data(my_url)->dict:
    response = urllib.request.urlopen(my_url)
    data = response.read().decode("utf-8")
    data =  json.loads(data)["countries"]
    # print(data)
    country_data = {}
    for country in data:
        country_data[country["country"]["country_id"]] = country["country"]["country_name"]
    # print(country_data)
    return country_data
    

def print_country_ids(country_data:dict):
    print("Country IDs:")
    print(",\t".join(list(country_data.keys())))
    # Alternate : Better avoid iteration
    # for country_id in country_data.keys():
    #     print(country_id)

#This function can be used as an alternate in case we want to display the ids in the range of few lines only separated by commas as there are too many ids present in this file
'''def print_country_ids(decoded_json):
    country_ids = [country_data["country"]["country_id"] for country_data in decoded_json["countries"]]
    print("Country IDs:", ", ".join(country_ids))'''


def get_country_name_by_id(country_data, country_id):
    return country_data[country_id]



if __name__ == '__main__':
    url = "http://vocab.nic.in/cla.php?cat=mast&info=country&format=json"
    country_dict = get_json_data(url)
    print_country_ids(country_dict)
    country_id = input("Enter a country ID: ").upper()
    country_name = get_country_name_by_id(country_dict, country_id)

    if country_name is not None:
        print(f"The country with ID {country_id} is {country_name}")
    else:
        print(f"No country found with ID {country_id}")
