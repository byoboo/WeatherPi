#!/usr/bin/python
import urllib2
import json
from time import sleep

def main():
    f = urllib2.urlopen('http://api.wunderground.com/api/9913b5810f41287f/geolookup/conditions/q/TX/Longview.json')
    json_string = f.read()
    parsed_json = json.loads(json_string)
    location = parsed_json['location']['city']
    observation_time = parsed_json['current_observation']['observation_time']
    temp_f = parsed_json['current_observation']['temperature_string']
    humidity = parsed_json['current_observation']['relative_humidity']
    wind = parsed_json['current_observation']['wind_string']
    print "Observation taken at %s" % (observation_time)
    print "Current temperature in %s is: %s" % (location, temp_f)
    print "Current humidity in %s is: %s" % (location, humidity)
    print "The wind in %s is coming %s" % (location, wind)
    print "____________________________________________________________"
    f.close()


if __name__ == '__main__':
	main()