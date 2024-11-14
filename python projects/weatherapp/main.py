import requests
import json
import win32com.client
speaker=win32com.client.Dispatch("SAPI.SpVoice")
city=input('enter your city:')
url=f'http://api.weatherapi.com/v1/current.json?key=5eb273ffd11b4cafba0151838241010&q={city}'
r=requests.get(url)
# print(r.text)
weather_dic=json.loads(r.text)
w1=weather_dic["current"]["condition"]["text"]
w2=weather_dic["current"]["temp_c"]
print(f"the current weather of {city} is {w1} with temperature {w2}")
speaker.Speak(f"The current weather of {city} is {w1} with temperature {w2}")
