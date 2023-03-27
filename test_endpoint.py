import requests
url='http://localhost:1097/v1/availability?domain=google.com'
c=0
while True:
    response=requests.get(url)
    if response.status_code == 200:
        c+=1
        print(c)
    if response.status_code != 200:
        print('Error')
        break
    