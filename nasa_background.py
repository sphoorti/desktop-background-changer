from bs4 import BeautifulSoup
import urllib2, re, datetime, os

#URL used to fetch the background image
url='http://apod.nasa.gov/apod/'
response=urllib2.urlopen(url)
content=response.read()
response.close()

soup = BeautifulSoup(content)

url=url+str(re.search(r'"([A-Za-z0-9_\./\\-]*)"', str(soup.find_all('a')[
response=urllib2.urlopen(url)
store = open ( str(datetime.date.today())+".jpg" , 'w')
store.write ( response.read())
store.close()
response.close()

#Change this line with respect to the Desktop Environment
os.system("feh --bg-fill " + str(datetime.date.today())+".jpg")
