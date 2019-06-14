import requests
import json
import links

r = requests.get(links.link2, verify=False)

json_file=r.json()
keys=json_file.keys()
print(json_file['DATA_1'][50]['uid'])

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
