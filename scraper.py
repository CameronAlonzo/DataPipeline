import requests 
import typing
from bs4 import BeautifulSoup
'''
    Set up beautiful soup to make the request, format the data. This is awkward, as their site is coded in a strange way
    This function takes in a str: teamName and returns 
'''
def makeRequest(teamName: str) -> dict:
    #the url to scrape from
    URL = "https://collegepigskin.gg/schools/"+teamName
    #Grab it
    print(URL)
    page = requests.get(URL)
    
    soup = BeautifulSoup(page.content, "html.parser")
    soup.prettify()

    div_main = soup.find("div", {"class": "grid grid-cols-2 md:grid-cols-3 px-6 md:px-0 text-center"}).get_text(" ")
    keys = {
        "AP Poll Rank": 8,
        "Last Season Record": 5,
        "All-Time Record": 4,
        "Bowl Game Record": 5,
        "National Championships": 3,
        "Conference Championships": 3,
        "Heisman Winners": 3,
        "All Americans": 3,
        "Draft Picks": 3
}
    values = div_main.split()
    data_dict = {}

    i = 0
    for key, value_count in keys.items():
        data_dict[key]=' '.join(values[i:i+value_count])
        i+= value_count
    return data_dict


if __name__ == '__main__':
    teams = ["florida", "georgia", "lsu", "auburn", "alabama", "texas", "oklahoma", "texas-am",
             "missouri", "kentucky", "tennessee", "south-carolina", "ole-miss"]
    
    with open('cfbdata.txt', 'w') as f:
        for team in teams:
            data = makeRequest(team)
            f.write(f"{team}:\n")
            for key, value in data.items():
                f.write(f"{value}\n")
            f.write(f"\n")





