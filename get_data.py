# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 30:34:37 2023

@author: Akhilesh
"""

import pandas as pd
import numpy as np
from datetime import datetime
import requests

class GetData :
    
    def __init__(self, username, password):
        
        self.username = username
        self.password = password
        self.base_url = "https://opensky-network.org/api"
        
    def get_states(self, time = None, icao24 = None):
        
        states_url = self.base_url + "/states/all"
        updated_url = None

        if time and icao24:
            updated_url = states_url + "?time=%d&icao24=%s"%(time, icao24)     
        else:
            print("Provide both begin and end dates")
        
        if updated_url:     
            print("Querying url - ", updated_url)
            s = requests.get(updated_url, timeout = 5)
        else:
            print("Querying url - ", states_url)
            s = requests.get(states_url, timeout = 5)
        
        return s
    
    def get_flights_in_time_interval(self, begin = None, end = None):
        
        flights_url = self.base_url + "/flights/all"
        updated_url = None
        
        
        if begin and end:
            updated_url = flights_url + "?begin=%d&end=%d"%(begin, end)
        else:
            print("Provide both begin and end dates")
            
        if updated_url:
            print("Querying url - ", updated_url)
            s = requests.get(updated_url, timeout = 30)
        else:
            print("Querying url - ", flights_url)
            s = requests.get(flights_url, timeout = 30)
            
        return s
    
    def get_flights_by_aircraft(self, icao24 = None, begin = None, end = None):
        
        flights_url = self.base_url + "/flights/aircraft"
        updated_url = None
        

        if icao24 and begin and end:
            updated_url = flights_url + "?icao24=%s&begin=%d&end=%d"%(icao24, begin, end)   
        else:
            print("Provide icao24, begin and end")
        
        if updated_url:
            print("Querying url - ", updated_url)
            s = requests.get(updated_url, timeout = 30)
        else:
            print("Querying url - ", flights_url)
            s = requests.get(flights_url, timeout = 30)
            
        return s
    
    def get_flights_by_arrivals(self, airport = None, begin = None, end = None):
        
        flights_url = self.base_url + "/flights/arrival"
        updated_url = None
            
        if airport and begin and end:
            updated_url = flights_url + "?icao24=%d&begin=%d&end=%d"%(airport, begin, end)   
        else:
            print("Provide icao24, begin and end")
        
        if updated_url:
            print("Querying url - ", updated_url)
            s = requests.get(updated_url, timeout = 30)
        else:
            print("Querying url - ", flights_url)
            s = requests.get(flights_url, timeout = 30)    
            
        return s

    def get_flights_by_departures(self, airport = None, begin = None, end = None):
        
        flights_url = self.base_url + "/flights/departure"
        updated_url = None
            
        if airport and begin and end:
            updated_url = flights_url + "?icao24=%s&begin=%d&end=%d"%(airport, begin, end)   
        else:
            print("Provide icao24, begin and end")
        
        if updated_url:
            print("Querying url - ", updated_url)
            s = requests.get(updated_url, timeout = 30)
        else:
            print("Querying url - ", flights_url)
            s = requests.get(flights_url, timeout = 30)
        
        return s

username = "akpa2888"
password = "fi5m!iRYRuj473X"

test_obj = GetData(username, password)    
#response = test_obj.get_states()
#response = test_obj.get_flights_in_time_interval()
#print(response)