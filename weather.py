import requests


def get_weather_data(w): # module for getting weather data
    api_key = "b3f0bee3bc55275ea190ea722ea1fdd1"
    if w == 1:
        location = input("enter your city of residence:")
        data = requests.get("http://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key)
    elif w == 2:
        location = input("enter your zip code:")
        data = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=" + location + ",us&appid=" + api_key)
    json_object = data.json()
    temperature = float(json_object ['main']['temp']) # this pulls out the temperature
    temperature = (temperature - 273.15) * 1.8 + 32 #convert from kelvin to fahrenheit
    temperature = int(temperature) # set variable to a interger
    return temperature


    

def menu(i):
    print("what city or zip code would you like to pull weather data from?")
    print("enter 1: to enter a city name.2 2: to enter a zip code.")
    w = int(input("enter selection:"))
    weather_data = None
    weather_data = get_weather_data(w)
    weather_data = str(weather_data) # set to string to output
    print("the temperture is " + weather_data)
    print("do you want to run this program again?")
    i = int(input("enter 0 for yes and 1 for no:"))
    return i




i = 0
while i == 0:
    i = menu(i)
print("program ended")