import requests, lxml
from lxml import html
import urllib

f=open('credentials.txt','r')
username=f.readline().strip()
password=f.readline().strip()
f.close()

##print username
##print password

s = requests.session()
login = s.get('login-page-url')
login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')
form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
print form

## inspect element and find the tag ids for login and password fields.

form['login_tag_id']= username
form['password_tag_id']= password
response = s.post('login-page-url', data=form)

#print response.text

with open('response.html', 'w') as fid:
    fid.write(response.text)

ids=set()
for line in open('ID.txt','r'):
    ids.add(line.strip())


url='home-page-url'
r2 = s.get(url, headers=dict(refer=url))
tree = html.fromstring(r2.content)

with open('homepage.html', 'w') as fid:
    fid.write(r2.content)  

