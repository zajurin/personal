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


tagsSeparatedByComma = [tag.name for tag in soup.find_all()]
tagsWithClasses= [str(tag) for tag in soup.find_all("h3")]

print(tagsWithClasses)
#Look for this tag
# tagSearched = soup.find_all('span', attrs={'class': 'mw31Ze'})# Level 1
# tagSearched2 = soup.findAll('h3', text = re.compile(companyName), attrs = {'class' : 'LC20lb DKV0Md'})# Level 2

# [tag.name for tag in soup.find_all()]