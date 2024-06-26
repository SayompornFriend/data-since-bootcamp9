
## import 'requests' module only 'get' function
## and 'time' module only 'sleep' function
from requests import get
from time import sleep
import pandas as pd # manage dataframe


## test request api
url = "https://swapi.py4e.com/api//people/"

test_resp = get(url)

print(test_resp)


## build for loop request index 1-5 url

data = [] # for collect result into dictionary

for i in range(1, 6) : # python start index = 0

    new_url = url + str(i) # use str() change index int >>> to string
    resp = get(new_url).json() # get url >>> show data in json format

    # Extract data from 5 column
    name = resp[ "name" ]
    height = resp[ "height" ]
    mass = resp[ "mass" ]
    gender = resp[ "gender" ]
    homeworld_url = resp[ "homeworld" ]

    # extract data from "name" column in homeworld url
    if homeworld_url:
        homeworld_resp = get(homeworld_url).json()
        homeworld = homeworld_resp[ "name" ]
    else:
        homeworld = "Unkown"

    print( name, height, mass, gender, homeworld )

    # append result into disctionary above
    data.append(
        { "name": name,
          "height": height,
          "mass": mass,
          "gender": gender,
          "homeworld": homeworld }
    )

    sleep(1) # will stop 1 sec when finish 1 loop


## return data from for loop into dataframe
df = pd.DataFrame(data)

## write to csv file
df.to_csv("5_star_wars_people.csv", index = False)
