#Name: Team Jared Butler                                                    #
#email: halverhc@mail.uc.edu                                              #
#Assignment Title: Assignment 10                                          #
#Course: IS 4010                                                          #
#Semester/Year: Spring 2023                                               #
#Brief Description: This project creates an API for jokes
#                                                                         #
#Anything else that's relevant: no 
#Citations:                                                               #
#https://www.geeksforgeeks.org/get-post-requests-using-python/            #
#https://realpython.com/api-integration-in-python/                        #
###########################################################################


import requests


#URL Data Request / Server submit
url = "https://api.chucknorris.io/jokes/random"
response = requests.get(url)

#Recieving Results From Server
if response.status_code == 200:
    data = response.json()
    joke = data["value"] #Puts data into dictionary
    print(joke) #outputs interesting data from dictionary
else:
    print(f"Error: {response.status_code}")
    


