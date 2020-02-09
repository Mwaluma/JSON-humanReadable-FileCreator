import json
import requests

def create_json(url = None, header= None, filepath= None, filename = None, indent= 4, sort= False):
    '''
    Takes a file in JSON that is not easy to read and parses it for easy reading
    Creates a file of the parsed JSON object
    Enables you to obtain JSON file automatically directly from a website
    
    url - pass a url that you are webscarraping. The response in JSON will be parsed
    filepath - pass the location of the JSON file present locally
    filename - pass the name of the new created file. You can specify path. Required
    indent - pass the size of the identation. Default is a indent number of 4
    sort - pass a 'True' if you want to sort the dictionary
    '''

    url_file = None
    path_file = None

    #Check if its a url or file path or both
    if url != None:
        url_file = web_scrap(url, header)

    if filepath != None:
        with open(filepath) as file:
            path_file = json.load(file)


    #Write to file
    if url_file != None:
        with open(filename, 'w') as file:
            json.dump(url_file, file, indent = indent, sort_keys = sort)

    if path_file != None:
        with open(filename, 'w') as file:
            json.dump(path_file, file, indent = indent, sort_keys = sort)




def web_scrap(url, header= None):
    '''
    Makes a request to the url and gets a response in JSON format
    '''
    r = requests.get(url, header)
    json_file = r.json()

    if r.status_code != 200:
        print("There was a problem fetching the data. Please check the url")

    return json_file



