
import requests
import json

#function to get the country name
def check(IP):
    i=f'https://ipinfo.io/{IP}/json'
    response=requests.get(i,verify=True)#requesting the ipinfo api
     
     #if the HTTP request isn't generated properly
    if response.status_code!=200:
        return 'Status:', response.status_code,'Quitting'
        exit()

    output=response.json()

    return output['country']

#input
IP=input("PLease provide the IP address: ")

#this will return the country code
print(check(IP))#output
