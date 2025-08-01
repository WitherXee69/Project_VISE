import requests.exceptions
from Data.Imports.local_imports import *
from Data.Imports.global_imports import *
from Data.Speak_All.speak_print_only import speak


def time_say():
    global tevent
    currentH = int(datetime.datetime.now().hour)
    if 0 <= currentH < 12:
        tevent = "Good Morning"
        # speak(f'Good Morning')

    if 12 <= currentH < 15:
        tevent = "Good Afternoon"
        # speak(f'Good Afternoon')

    if 15 <= currentH < 18:
        tevent = "Good Evening"
        # speak(f'Good Evening')

    if currentH >= 18 and currentH != 0:
        tevent = "Good Night"
        # speak(f'Good Night')
    now_time = datetime.datetime.now()
    current_date = now_time.strftime("%B %d %Y")
    current_time = now_time.strftime("%I:%M %p")
    speak(f"{tevent} sir! Today is {current_date}, and time is {current_time}")


def weather():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q": "Colombo,lk", "lat": "0", "lon": "0", "lang": "null", "units": "\"metric\" or \"imperial\"",
                   "mode": "xml, html"}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "91d822cb1emsh7833c1fea965e8ap1128dbjsn79a053492112"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()

        weather_temp = data["main"]
        weather_disk = data["weather"]

        temp = weather_temp["temp"]
        tempc = temp - 273.15
        rtemp = round(tempc, 2)
        disk = weather_disk[0]["description"]
        if rtemp < 20:
            # print("cold")
            speak(
                f"There is {str(disk)} and you feel {str(rtemp)} Celsius temperature in your area Sir! Today will be a "
                f"cold day")
            # TODO make cold warm hot acording to weather data
        elif rtemp > 20:
            # print("warm")
            speak(
                f"There is {str(disk)} and you feel {str(rtemp)} Celsius temperature in your area Sir! Today will be a "
                f"warm day")
        elif rtemp > 25:
            # print("hot")
            speak(
                f"There is {str(disk)} and you feel {str(rtemp)} Celsius temperature in your area Sir! Today will be a "
                f"hot day")
        elif rtemp > 30:
            # print("very hot")
            speak(
                f"There is {str(disk)} and you feel {str(rtemp)} Celsius temperature in your area Sir! Today will be a "
                f"very hot day")

        # speak(f"There is {str(disk)} and you feel {str(rtemp)} Celsius temperature in your area Sir!")

    except requests.exceptions.ConnectionError:
        speak("sorry sir, check your connection with inernet. there is some connection problem on weather")


def sys_status():
    hks = random.choice(human_know_start)
    speak(hks)