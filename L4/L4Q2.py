import urllib.request

def noaa_string():
    ''' Download the specified webpage and return 
        it as a string''' 
        
    url = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.request.urlopen(url).read()
    return noaa_data_string.decode("utf-8")

def  noaa_temperature(s):
    ''' Given parameter s, take string s returned from 
        noaa_string() as the input argument,
        extract the temperature in degree Celsius from the string
        and return this temperature as an integer number '''
        
    for line in s.split('\n'):
        if line.startswith("Temperature"):
            print(line[(line.find('(')+1):line.find('C')])

noaa_temperature(noaa_string())