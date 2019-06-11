import requests
r = requests.get('https://megabit38.ru:9443/admin/index.cgi?get_index=dv_users_list&EXPORT_CONTENT=INTERNET_USERS_LIST&header=1&json=1&PAGE_ROWS=1000000&API_KEY=9954782216weDHUSdhgsdGJ544', verify=False)
print(r.text[1])
