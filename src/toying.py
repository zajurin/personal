import openpyxl
import requests
import bs4
from openpyxl  import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter, column_index_from_string
from bs4 import BeautifulSoup

import re

import urllib.request
import phonenumbers


#******* AVOID BEING BLOCKED *******
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

companyName = "Caprock Academy"
companyAddress = "headquarters"

#CREATING URL FOR GOOGLE SEARCHING
text = ("phone number of {0} {1} ".format(companyName, companyAddress))
myCurrentURL = 'https://google.com/search?q=' + text

#ACCESING TO URL's INFO
response = requests.get(myCurrentURL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# alldivs = soup.find_all('div')
# twoNine5Div = alldivs[292]
# segunEso = soup.find_all('div', attrs = {'class': 'liYKde g VjDLd'})

# print(twoNine5Div)

# utiles
tagsSeparatedByComma = [tag.attrs for tag in soup.find_all("div")]
searchAttrs = {'class': ['liYKde', 'g', 'VjDLd']}
which_Index_Is_This_Tag = tagsSeparatedByComma.index(searchAttrs)# Output: index 292

print(which_Index_Is_This_Tag)# tell me in which index is the tag searched

# twoNine5Div92 = tagsSeparatedByComma[292]

# tagsWithClasses= [str(tag) for tag in soup.find_all("div")]

alldivs = soup.find_all('div')
twoNine5Div = alldivs[which_Index_Is_This_Tag]
for divs in twoNine5Div:
	spans_In_Divs = divs.findChildren("span")
	# spans_In_Divs_TO_STRING = str(spans_In_Divs)#convertir a String por si acaso
	# matching_CompanyName = spans_In_Divs_TO_STRING.find(companyName) #Trate de sustituir el buscar con RE 
	# if matching_CompanyName:# si companyName coincidia con el nombre en el span habria de imprimirse
	# 	print(matching_CompanyName)


	# matchs_Of_CompanyName = soup.findAll('span', text = re.compile(companyName))# Level 2
	# if matchs_Of_CompanyName:
	# 	print(matchs_Of_CompanyName)
	# else:
	# 	print(False)

#Look for this tag
# tagSearched = soup.find_all('span', attrs={'class': 'mw31Ze'})# Level 1
# tagSearched2 = soup.findAll('h3', text = re.compile(companyName), attrs = {'class' : 'LC20lb DKV0Md'})# Level 2

# [tag.name for tag in soup.find_all()]