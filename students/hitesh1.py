# -*- coding: utf-8 -*-
"""
Sun Jul 29 22:25:22 2018: Dhiraj
"""

import requests
import json
import csv
import pandas
url = 'http://adminapi.fat.test.fleetmode.io/temperature-regions/get-history/'
data = {"TemperatureRegionID" : 419,"StartDate" : "07/23/2018 01:55:45 PM","StopDate" : "07/23/2018 09:55:45 PM","Interval" : "Minute"}
r = requests.post(url = url,data = json.dumps(data))
data2 = r.text
print(data2)
f = csv.writer(open("test.csv", "wb+"))
f.open
df=pandas.read_json(data2)
df.head()
df



input = open(sys.argv[1])
data = json.load(input)
input.close()

output = csv.writer(sys.stdout)

output.writerow(data[0].keys())  # header row

for row in data:
    output.writerow(row.values())


pandas.df_csv(r.text)








x=r.text
x=r.loads
# Write CSV Header, If you dont need that, remove this line
#f.writerow(["pk", "model", "codename", "name", "content_type"])

for x in x:
    f.writerow([x["TemperatureRegionID"],
                x["StartDate"],
                x["StopDate"],
                x["Interval"],
                ])
    
    
    

pastebin_url = r.text
print(pastebin_url)
print
f = open('r.json')
Data = json.loads(str(f))
Dishwasher_data = open('/Users/hiteshady/Documents/MUIT-PGD/Python/Python-Projects/pastebin_url.txt', 'r')