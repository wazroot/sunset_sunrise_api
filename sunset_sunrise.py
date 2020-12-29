
import requests
import urllib.parse
import datetime



riseset_api_url = 'https://api.sunrise-sunset.org/json?'
zonedb_api = 'http://api.timezonedb.com/v2.1/get-time-zone?key=BX1JWRU9QG3O&format=json&by=position&'
zonedb_key = 'BX1JWRU9QG3O'
postal_api = 'http://api.positionstack.com/v1/forward?access_key=6bf283c90bcdabaa23977dee1386460e&'

#latitude and longitude user input
while True:
    lat = input('Latitude?: ')
    if lat == 'quit' or lat == 'q':
        break
    lng = input('Longitude?: ')
    if lng == 'quit' or lng == 'q':
        break
    
    
    postal = input('Give your postal code and country ID(e.g 20810,FI)?: ')
    #print('=======================================================================')
    #sunset sunrise api + user input(lat & lng)     
    url = riseset_api_url + urllib.parse.urlencode({'lat':lat, 'lng':lng})
    #print('URL: ' + url) 
    
    #print('=======================================================================')
    #TimeZone api + lat&lng
    url_one = zonedb_api + urllib.parse.urlencode({'lat':lat, 'lng':lng})
    #print('URL: ' + url_one) 
    #print('=======================================================================')
    #Postal code url parse
    
    url_two = postal_api + urllib.parse.urlencode({'query' : postal})
    #print('URL: ' + url_two) 
    print('========================================================================')
    #data in json for lat&lng
    json_data = requests.get(url).json()
    #data in json for TimeZonedb
    TimeZone_json = requests.get(url_one).json()
    #data in json for postal code
    postal_json = requests.get(url_two).json()
    
    #Prints latitude and longitude
    print('Coordinates: ' + lat + ' latitude' + ' and ' + lng + ' longitude')

    # Rise and set time in UTC+0
    sun_rise = (json_data['results']['sunrise'])
    sun_set = (json_data['results']['sunset'])
    print('Sunrise: ' + str(sun_rise))
    print('Sunset: ' + str(sun_set))
    print('===========================================================================')
    
    #Automated time conversion from lat&lng with TimeZonedb api 
    oOffset=datetime.datetime.now()- datetime.datetime.utcnow()
    oSunriseLTime = datetime.datetime.strptime(str(sun_rise), '%I:%M:%S %p') + oOffset
    oSunsetLTime = datetime.datetime.strptime(str(sun_set), '%I:%M:%S %p') + oOffset
    print('Local sunrise: ' + (str(oSunriseLTime.time()) + ' AM'))
    print('Local sunset: ' + (str(oSunsetLTime.time()) + ' PM'))
    print("Local time offset is " + str(oOffset))
    print('===========================================================================')
    
    #Postal code to lat&lng
    
    print('Latitude of given postal code: ' + str(postal_json['data'][0]['latitude']))
    print('Longitude of given postal code: ' + str(postal_json['data'][0]['longitude']))
    print('===========================================================================')
    
    #Converts from UTC+0 to local sunrise/set time
    LOCAL_TIME_RISE = []
    LOCAL_TIME_SET = []
    USER_TIME = input('How many hours from UTC+0 (ex.-3 or 3 ) is your local time?: ')
    
    for i in json_data['results']['sunrise']:
        LOCAL_TIME_RISE.append(i)
    local_sunrise = str(int(LOCAL_TIME_RISE[0]) + int(USER_TIME)) + ':' + LOCAL_TIME_RISE[2] + LOCAL_TIME_RISE[3] + ':' + LOCAL_TIME_RISE[5] + LOCAL_TIME_RISE[6] + ' ' + LOCAL_TIME_RISE[8] + LOCAL_TIME_RISE[9]
    print('Local sunrise: ' + (local_sunrise))
    for b in json_data['results']['sunset']:
        LOCAL_TIME_SET.append(b)
    local_sunset = str(int(LOCAL_TIME_SET[0]) + int(USER_TIME)) + ':' + LOCAL_TIME_SET[2] + LOCAL_TIME_SET[3] + ':' + LOCAL_TIME_SET[5] + LOCAL_TIME_SET[6] + ' ' + LOCAL_TIME_SET[8] + LOCAL_TIME_SET[9]
    print('Local sunset: ' + (local_sunset))

    print('============================================================================')


    
