# import module
from operator import truediv
import requests
from bs4 import BeautifulSoup

HEADERS = ({'User-Agent':
			'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
			AppleWebKit/537.36 (KHTML, like Gecko) \
			Chrome/90.0.4430.212 Safari/537.36',
			'Accept-Language': 'en-US, en;q=0.5'})

def getdata(url):
	r = requests.get(url, headers=HEADERS)
	return r.text

def html_code(url):

	# pass the url
	# into getdata function
	htmldata = getdata(url)
	soup = BeautifulSoup(htmldata, 'html.parser')

	# display html code
	return (soup)

def product_info(soup):

	# find the Html tag
	# with find()
	# and convert into string
	data_str = ""
	pro_info = []

	for item in soup.find_all("ul", class_="a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list"):
		data_str = data_str + item.get_text()
		pro_info.append(data_str)
		data_str = ""
	return pro_info

def stringsuche(Quelle,Suchbegriff):
  Ergebnis = [s for s in Quelle if Suchbegriff in s]
  return(Ergebnis)

def Stringteilung(Quelle):
	Ergebnis = Quelle.split()
	return(Ergebnis[3])

def Buchrang(url):
	soup = html_code(url)
	pro_result = product_info(soup)
	Zeile = stringsuche(pro_result,"Amazon Bestseller")
	satz =" ".join(Zeile)
	return Stringteilung(satz)

