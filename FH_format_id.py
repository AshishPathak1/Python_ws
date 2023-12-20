# Fetch the format inforation of all formats from "http://vocab.nic.in/cla.php?cat=mast&info=format&format=json"
# and print the details of a particulat format give its id

def get_json_data(my_url)->dict:
    import urllib.request
    import json
    response = urllib.request.urlopen(my_url)
    data = response.read().decode("utf-8")
    data = json.loads(data)["formats"]
    format_dict = {}
    # create a dictionary having the format_id as key and 
    # format name and description as values
    for aformat in data:
        format_dict[aformat["format"]["format_id"]] = [aformat["format"]["format_name"],aformat["format"]["format_desc"]]
    return format_dict
        

def get_format_info(format_info:dict,format_id:int)->None:
    format_details = format_info.get(format_id)
    if format_details:
        print(f"format name : {format_details[0]}")
        print(f"format description : {format_details[1]}")
    else:
        print(f"The format id {format_id} is not existing")
        
if __name__ == '__main__':
    url = "http://vocab.nic.in/cla.php?cat=mast&info=format&format=json"
    format_info = get_json_data(url)
    format_id = input('Please enter the format ID: ')
    get_format_info(format_info,format_id)
