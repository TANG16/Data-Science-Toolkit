#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'calcMissing' function below.
#
# The function accepts STRING_ARRAY readings as parameter.
#

def calcMissing(readings): 
    import pandas as pd
    time = []
    value = []
    for line in readings:
        line_split = line.split("\t")
        time.append(line_split[0])
        value.append(line_split[1])
    
    data = pd.DataFrame({"time": time, "value": value})
    
    values = data["value"]
    for i in values:
        if "Missing" in i:
            data[values][i] = None    
            
    values.isnull().sum()
    
    
    #df = pd.DataFrame({"time": split_line[0], "value": split_line[1]})
    #print(df)
    
    
        
        
    
    # Write your code here
if __name__ == '__main__':
    
    readings_count = int(input().strip())

    readings = []

    for _ in range(readings_count):
        readings_item = input()
        readings.append(readings_item)

    calcMissing(readings)

    
    
    
    