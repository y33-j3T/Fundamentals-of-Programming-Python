import urllib.request

def noaa_string():
    url = "http://tgftp.nws.noaa.gov/data/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.request.urlopen(url).read()
    return noaa_data_string.decode("utf-8")

def  noaa_temperature(s):
    for line in s.split('\n'):
        if line.startswith("Temperature"):
            print(line[(line.find('(')+1):line.find('C')])

noaa_temperature(noaa_string())
