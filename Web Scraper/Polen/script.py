import requests
import os.path as io
from datetime import date,timedelta
import time
from colorama import Fore,Style

print(Fore.BLUE)
print("--- [ Polen script by Đole ] ---")
print(Style.RESET_ALL)
time.sleep(1)

print(Fore.BLUE)
days = input("Unesite broj dana: ")
print(Style.RESET_ALL)
today = date.today()
_date = today - timedelta(2 + int(days))


if not io.isfile("locations.txt"):
    with open("locations.txt","w", encoding="utf-8") as f:

        locations_list = requests.get("https://data.gov.rs/sr/datasets/r/c7821029-ec4e-45c1-ac86-d469eafc6f91")
        locations_list = locations_list.json()
        locations_list = sorted(locations_list,key = lambda x:x['id'])

        for i in locations_list:
            f.write(f"{i['id']}: {i['name']}")
        f.close()
        
locations = open("locations.txt","r",encoding="utf-8")

for line in locations:
    print(f"{Fore.BLUE}{line}{Fore.RESET}",end="")
locations.close()

print(Fore.BLUE)
location = input("Unesi id mesta: ")
print(Style.RESET_ALL)

pollens_list = requests.get(f"http://polen.sepa.gov.rs/api/opendata/pollens/?location={location}&date_after={_date}")
pollens_list = pollens_list.json()

polen = pollens_list['results']

for i in polen:
    print(f"Za dan:{Fore.BLUE} {i['date']}{Fore.RESET}")
    for j in i['concentrations']:    
        concentrations = requests.get(f"http://polen.sepa.gov.rs/api/opendata/concentrations/{j}")
        concentrations = concentrations.json()
        

        allergen = requests.get(f"http://polen.sepa.gov.rs/api/opendata/allergens/{concentrations['allergen']}")
        allergen = allergen.json()
        
        current_value = concentrations['value']
        
        if current_value > allergen['margine_top']:
            print(f"{Fore.RED}Koncentracija polena je {allergen['localized_name']} {allergen['name']} je visoka!{Fore.RESET}")
        elif allergen['margine_top'] >= current_value >= allergen['margine_bottom']:
            print(f"{Fore.YELLOW}Koncentracija polena je {allergen['localized_name']} {allergen['name']} je srednja!{Fore.RESET}")
        else:
            print(f"{Fore.GREEN}Koncentracija polena je {allergen['localized_name']} {allergen['name']} je niska!{Fore.RESET}")
    print(Fore.BLUE)
    print("========================================================")
    print(Style.RESET_ALL)
