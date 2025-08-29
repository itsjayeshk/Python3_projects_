import requests
city = "London"
url = 'http://api.weatherapi.com/v1/current.json?key=1201e76f09ce4650a88150738252908&q='+city+'&aqi=no'
response = requests.get(url)
weather_json = response.json()

temp = weather_json.get('current').get('temp_c')
climate = weather_json.get('current').get('condition').get('text')

print("Todays temperature is " , temp)
print("Todays climate is " , climate)