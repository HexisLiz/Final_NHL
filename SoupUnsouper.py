
import os 
import pandas as pd
from bs4 import BeautifulSoup
i=0
n=1979

#Function that handles missing values and makes them into "NaN"
def nanhandle (data, index):
 
    if len(data[index].text.strip()) > 0:
        return data[index].text.strip()
    else:
        return ("NaN")
    
    
#Function that handles the two types of season data, playoffs [1] and seasonal [0]
def seasonalityhandle (data, index):
    if seasonality.lower() == "playoffs":
        return 0
    else:
        return 1
    
#

files = os.listdir ("NHL")

for file in files :
    df = []
    text = open("NHL/"+file, "r").read() 
    soup = BeautifulSoup (text, features = "lxml")


    try:
        table = soup.findAll("table")
        table_season = table [0]
        
    except: 
        print ("error in file for FindAll (table) ", file)
        
    try:
        rows = table_season.findAll ("tr")
        
    except:
       print ("error in table_Season.findAll occured")
     
    try:
        seasonality_data = soup.findAll ("h2")
        seasonality = seasonality_data[1].text.strip()
        
        if seasonality.lower() == "playoffs":
            seasonality = 0
        else:
            seasonality = 1
        
    except: 
        print ("error indexing seasonality")     


    for row in rows:
        gamedate_data = row.findAll ("th") 
        gamedata = row.findAll ("td")
        i = i+1

        try:
              game_date = nanhandle (gamedate_data, 0)
              visitor_team = nanhandle (gamedata, 1)
              visitor_goals = nanhandle (gamedata, 2)
              home_team = nanhandle (gamedata, 3)
              home_goals = nanhandle (gamedata, 4)
              game_decided = nanhandle (gamedata, 5)
              game_lenght = nanhandle (gamedata, 7)
              attendance = nanhandle (gamedata, 6)
             
              
              
              df.append([game_date, visitor_team,visitor_goals,home_team,home_goals, attendance, game_lenght,game_decided, seasonality])
              
        except: #To errors,første error error in data to variable indexing for [] NHL_1980.html 1 og en error for alle seasonality 
              print ("error in data to variable indexing for",row(i), file, i)
              
     
    n = n+1
    df = pd.DataFrame(df,columns =["game_date", "visitor_team", "visitor_goals","home_team","home_goals", "attendance", "game_lenght","game_decided", "seasonality"])
    df.to_csv("NHL_CSV_" + str(n)+ ".csv", index=False, encoding="utf-8")
    print ("year" + str(n)+"saved sucessfully")
    break #Bare for ikke at køre 40 loops





        
            

