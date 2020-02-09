from writer import create_json

#This is an example of how the module works

#*****************************************************
#       Fetching data from a url                     *
#*****************************************************

#Fetching data from a website
url = "https://api.github.com/search/repositories?q=language:python"

#Header is api specific. Not usually required but some api
#needs you to specify 
header = "Accept: application/vnd.github.v3+json"

#File path you want the created JSON file to be stored
#Example: "F:\\My project\\json_writer\\created_file.json"
filename = "created_file_url.json"

#Create a JSON file
create_json(url= url, header= header, filename= filename)

#*****************************************************
#       Passing a file path                          *
#*****************************************************

#Passing the file directory
filepath = "hard_to_read_example.json"

#File path you want the created JSON file to be stored
#Example: "F:\\My project\\json_writer\\created_file.json"
filename = "created_file_directory.json"

#Create a JSON file
create_json(filepath = filepath, filename= filename)
