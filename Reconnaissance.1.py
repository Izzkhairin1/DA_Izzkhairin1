#Q5 to demonstrate reconnaissance
#Question 5i
#Use the Request Library
import requests
#Set the target webpage which is http://172.17.50.43/creative
url = 'http://172.17.50.43/creative'
r = requests.get(url)
#This will get the full page
print(r.text)
#Question 5ii
#This will get the status code and display 'OK' return status
print("Status code:OK")
print("\t*",r.status_code)
#Question 5iii and 5iv
#This will just get the headers
h = requests.head(url)
print("Header:")
print("******")
#To print line by line
for x in h.headers:
    print('\t',x,':',h.headers[x])
print('*******')
#This will modify the headers user-agent to display mobile on 5iv
header={
    'User-Agent': 'Mobile'
}
#Test it on an external site change to headers.php on 5iii
url2 = 'http://172.17.50.43/headers.php'
rh = requests.get(url2, headers=header)
print(rh.text)


