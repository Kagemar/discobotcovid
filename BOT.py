import discord



import requests
import json
from tabulate import tabulate





def jprint(countryInput):
    response = requests.get(r"https://coronavirus-19-api.herokuapp.com/countries/{}".format(countryInput))
    # create a formatted string of the Python JSON object
    text = response.json()
    return text
    #print(response.json()['cases'])
    #return text

jprint("poland")

#{"country":"Poland","cases":2420,"todayCases":109,"deaths":36,"todayDeaths":3,"recovered":7,"active":2377,"critical":50,"casesPerOneMillion":64,"deathsPerOneMillion":1,"firstCase":"\nMar 03 "}






TOKEN = 'NjkyMTI1MDMyODM0NTMxMzI5.XoTGhg.RDWBAbbDrxLPK4VPbNnWEJowq2Q'
client = discord.Client()


@client.event
async def on_message(message):  # event that happens per any message.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")
    if "wirus" in message.content.lower():
        
        countryInput = message.content.lower().replace("wirus","")
        COUNTRY = str(jprint(countryInput.strip())['country']).replace('"','')
        CASES = str(jprint(countryInput.strip())['cases'])
        DEATHS = str(jprint(countryInput.strip())['deaths'])
        TodayCases = str(jprint(countryInput.strip())['todayCases'])
        TodayDeaths = str(jprint(countryInput.strip())['todayDeaths'])
        #mess_text = COUNTRY+"_"+CASES
        #print(COUNTRY)
        mess_text = tabulate([[COUNTRY, CASES, DEATHS, TodayCases, TodayDeaths]], headers=['Country', 'Cases', 'Deaths' , "Today new cases",'Today new deaths'], tablefmt="plain")
        
    
        if "mordziunia" in message.author.name.lower():
            mess_text = "Jedyny wirus na tym discordzie to ty Mordziunia!"
    await message.channel.send(mess_text)   

    

    

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


