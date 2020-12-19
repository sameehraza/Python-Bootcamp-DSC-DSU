import requests as r
import json
import csv

link = 'https://directory.ntschools.net/api/System/GetAllSchools'
res = r.get(link)
parsed_res = json.loads(res.content)

link = 'https://directory.ntschools.net/api/System/GetSchool?itSchoolCode='

with open ("School_Scraping.csv","w",encoding="utf-8") as file:
    file.write("Name,Address,Principal/Admin,Position,Email,Telephone\n")

school_codes =[]
for code in parsed_res:
    school_codes.append(code['itSchoolCode'])

for i in range(50):
    school_data =r.get(link+school_codes[i])
    parsed_data = json.loads(school_data.content)

    print(parsed_data['name'])
    print(parsed_data['physicalAddress']['displayAddress'])
    print(parsed_data['schoolManagement'][0]['firstName']+' '+parsed_data['schoolManagement'][0]['lastName'])
    print(parsed_data['schoolManagement'][0]['position'])
    print(parsed_data['schoolManagement'][0]['email'])
    print(parsed_data['telephoneNumber'])

    with open("School_Scraping.csv","a",encoding="utf-8") as file:
        file.write(f"{parsed_data['name']},{parsed_data['physicalAddress']['displayAddress'].replace(',',' ')},{parsed_data['schoolManagement'][0]['firstName'] + ' ' + parsed_data['schoolManagement'][0]['lastName']},{parsed_data['schoolManagement'][0]['position']},{parsed_data['schoolManagement'][0]['email']},{parsed_data['telephoneNumber']}\n")