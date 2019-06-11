import requests
import json
import links

r = requests.get(links.link1, verify=False)
jason_file=r.json()
keys=jason_file.keys()
print(keys)

print(len(jason_file['DATA_1'][0]))
print(type(jason_file['DATA_1'][0]))
print(jason_file['DATA_1'][0])

login=
