#this api is for dreams.html page in the Project Solo app. this code is to be inserted into the project. At this point, I don't know where it goes. 
#response.text
#response.json()
#print(response.json())
#print(quote[0]["h"], quote[0]["a"], quote[0]["h"]) is used to call the different indexes. 


import requests

def quote():
    response = requests.get("https://zenquotes.io/api/random")
    quote = response.json()
    return response