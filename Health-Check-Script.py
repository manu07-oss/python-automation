import requests

def health_check(url):
    try:
        response = requests.get(url, timeout=3)
        if response.status_code == 200:
            return "UP"
        else:
            return "DOWN"
    except:
        return "DOWN"

print(health_check("https://google.com"))



####################output#################
#Run started
#Initializing environment
#Installing packages
#Running code
#DOWN

#Run completed in 3513.10000000149ms
