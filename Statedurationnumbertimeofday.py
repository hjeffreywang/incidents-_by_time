# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 10:59:43 2019

@author: Jeffrey Wang
"""

import json
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

# read file
with open('Resources/CleanedData.json', 'r') as myfile:
    data=myfile.read()
    
obj = json.loads(data)
summarydf=pd.DataFrame(obj)



#Find total incidents duration by State
Totalincidentduration= pd.pivot_table(summarydf,index='State', values='Duration_(seconds)')

#Find total incidents by state
Incidentsbystate=summarydf.groupby('State').count()
Incidentsbystate=Incidentsbystate.rename(columns={"ID": "Total Incident Count"})
Incidentsbystatecount=Incidentsbystate["Total Incident Count"]
#-------------------------------------------------------------------------------
#Graphing time of day of accidents


#turn to time of day to datetime
datetimeconv=[]
time_of_day=[]
print(len(summarydf))

for times in range(0,len(summarydf)):
    datetimeconv.append(datetime.strptime(summarydf['Start_time'][times], '%Y/%m/%d %X'))
    time_of_day.append(datetimeconv[times].hour)


timeofdaydict=dict(Counter(time_of_day))

keyss=[]
valuess=[]
for key in timeofdaydict:
    keyss.append(key)
    valuess.append(timeofdaydict[key])
    
f, ax = plt.subplots(figsize=(18,5))
plt.bar(keyss,valuess)
