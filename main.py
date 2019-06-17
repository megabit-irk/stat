import requests
import json
import links

#user_info='https://megabit38.ru:9443/admin/index.cgi?qindex=15&UID='+uid+'&SUMMARY_SHOW=1&EXPORT=1&API_KEY=9954782216weDHUSdhgsdGJ544'


f = open('nukuti.txt', 'w')


all_info = requests.get(links.all_info, verify=False)
#user_info = requests.get(links.user_info, verify=False)

json_all=all_info.json()
keys_all=info=json_all.keys()

json_user=user_info.json()

q_users=len(json_all['DATA_1'])
print(q_users)

list_uid=list(range(0,q_users))

for index in list(range(0,q_users)):
    uid=json_all['DATA_1'][index]['uid']
    list_uid[index]=uid

print(list_uid)
user_info = 0
for counter in range(0,len(list_uid)):
    user_info = requests.get('https://megabit38.ru:9443/admin/index.cgi?qindex=15&UID='+list_uid[counter]+'&SUMMARY_SHOW=1&EXPORT=1&API_KEY=9954782216weDHUSdhgsdGJ544', verify=False)
    json_user_info=user_info.json()
    f.write(str(json_user_info) + '\n')





# print(type(json_file['DATA_1']))
# print(json_file['DATA_1'][0])
# print(type(json_file['DATA_1'][0]['login']))
#
# q_users=len(json_file['DATA_1'])
#
# for index in range(0,q_users):
#     login=json_file['DATA_1'][index]['login']
#     name=json_file['DATA_1'][index]['fio']
#     # date_on=json_file['DATA_1'][index]['login']
#     # date_off=json_file['DATA_1'][index]['login']
#     credit=json_file['DATA_1'][index]['credit']
#     deposit=json_file['DATA_1'][index]['deposit']
