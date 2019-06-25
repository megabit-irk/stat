import requests
import json
import links



del_info = requests.get(links.del_ok, verify=False)
json_del=del_info.json()


print(json_del.keys())
print(len(json_del['DATA_1']))
#print(json_del['DATA_1'][0]['deleted'])

d=0
for index in list(range(0,len(json_del['DATA_1']))):
    if json_del['DATA_1'][index]['login_status']!='Отключено':
        d=d+1
print("не отключено: ",d)


с=0
for index in list(range(0,len(json_del['DATA_1']))):
    if json_del['DATA_1'][index]['login_status']=='Отключено':
        с=с+1
print("Отключено: ",с)

b=0
for index in list(range(0,len(json_del['DATA_1']))):
    if json_del['DATA_1'][index]['deleted']=='Да':
        b=b+1
print("удалённые: ",b)

a=0
for index in list(range(0,len(json_del['DATA_1']))):
    if json_del['DATA_1'][index]['login_status']=='Активно':
        a=a+1
print("активные: ",a)
