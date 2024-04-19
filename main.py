#Import the necessary libraries
from dotenv import load_dotenv
from requests import post
import os
import base64 
import json

#Load the environment variables
load_dotenv()

# Get our API key from the environment
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

#Print the API key to make sure it was loaded correctly
#print(client_id, client_secret)

#Create a function to get the token
def get_auth_token():
    auth_str = client_id + ':' + client_secret
    auth_byte = auth_str.encode('utf-8')
    
    #returns a base64 object, we need to convert it to a string
    auth_base64 = str(base64.b64encode(auth_byte), 'utf-8')
    
    #write the url we want to send the request to
    url = "https://accounts.spotify.com/api/token"
    
    #create headers to send our authentication data and verify the user
    headers = { "authorization": "Basic " + auth_base64, "content-type": "application/x-www-form-urlencoded"}
    
    #create the data we want to send to the server
    data = {"grant_type": "client_credentials"}
    
    #the body of the request
    res = post(url, headers=headers, data=data)
    
    json_res = json.loads(res.content)
    token = json_res['access_token']
    
    return token

token = get_auth_token()
print(token)

#Now when we have the authentication token we can use it to make requests to the Spotify API.
def get_auth_header():
    return {"Authorization": "Bearer " + token}
    
#Search for an artist
