from bs4 import BeautifulSoup
import requests
import re
import phonenumbers
import urllib.request

import openpyxl
from openpyxl  import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter, column_index_from_string


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
whichCountry = "US" # this variable MUST BE DINAMIC FROM Excel

companyName = 'Flagstaff Academy Inc' 


# WRITING IN EXCEL FILE


#CREATING URL FOR GOOGLE SEARCHING
text = ("phone number of {0} headquarters ".format(companyName))
myCurrentURL = 'https://google.com/search?q=' + text

response = requests.get(myCurrentURL, headers=headers)

content_HTML = response.text
soup = BeautifulSoup(content_HTML, "lxml")

# print(soup.prettify())

search_classMW31ZE = soup.find_all('span', attrs={'class': 'mw31Ze'})# Level 1
search_CompanyName = soup.find_all('h3', text = re.compile(companyName), attrs = {'class' : 'LC20lb DKV0Md'})# Level 2

search_Each_div_Container = soup.find_all('div', attrs={'class': 'tF2Cxc'})# Level 3

for divs in search_Each_div_Container:
	if search_CompanyName:
		chaotic_SPAN = divs.findChildren('span')
		# print(chaotic_SPAN)
		for each_SPAN in chaotic_SPAN:
			new_SPAN_That_Needs_To_Be_STRING = str(each_SPAN)
			for match in phonenumbers.PhoneNumberMatcher(new_SPAN_That_Needs_To_Be_STRING, whichCountry):
				global only_Number
				only_Number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)				
				print(only_Number)

