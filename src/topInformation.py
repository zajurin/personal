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

# #******* AVOID BEING BLOCKED *******
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}


#CREATING URL FOR GOOGLE SEARCHING
companyAddress = "headquarters"
# Uso headquarters porque en el level 2 se da por hecho que el level 1 fallo porque no tenia el domicilio de los headquarters. 
# El cual debe ser extraido de Linkedin

companyName = "Caprock Academy" #Este valor debe ser dinamico desde excel porque ahi esta el nombre de la empresa a buscar

text = ("phone number of {0} {1} ".format(companyName, companyAddress)) 
#Esta variable es lo que comunmente se coloca en el buscador de google. Variable text con campos dinamicos para ser cambiados desde excel

myCurrentURL = 'https://google.com/search?q=' + text#Concatenacion de la URL de google search with text variable

response = requests.get(myCurrentURL, headers=headers) 
# this variable with the reuest method is used to specified which URL is going to be scraped.
# And headers are builded like so, to avoid the Forbiden 403 error.

soup = BeautifulSoup(response.text, 'html.parser')# Here I specified to read this URL in HTML format.parser
 
chaotic_Info = soup.body #Readme body tag in the URL (specified in myCurrentURL) 

whichCountry = "US" # this variable MUST BE DINAMIC FROM Excel

# for eachTD in chaotic_Info.find_all('span'):
#     new_TD = str(eachTD)
#     for match in phonenumbers.PhoneNumberMatcher(new_TD, whichCountry):
#         onlyTheNumber = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
#         converting_To_Strings = str(onlyTheNumber)
#         converting_To_LIST = list(converting_To_Strings)

#         joining_Phone = ''.join(converting_To_LIST)
#         print(onlyTheNumber)

myBODY = soup.body
all_My_H3 = myBODY.find_all('h3', {'class': "LC20lb DKV0Md"})

children = all_My_H3.findChildren('span', recursive=False)
for child in children:
    print(children)


# tagSearched2 = soup.findAll('h3', text = re.compile("Caprock Academy"), attrs = {'class' : 'LC20lb DKV0Md'})# Level 2

# if tagSearched2:
#     children = tagSearched2.findChildren("span" , recursive=False)
#     for child in children:
#         print(child)

        # concatenatingPhoneNumbers = ''.join(listOfPhoneNumbers + converting_To_LIST)

        # arrayOfPhoneNumbers = None
        # turnIntoString = phonenumbers.parse(match.number, whichCountry)

        # onlyTheNumber = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
        # # print(turnIntoString)
        # print(type(onlyTheNumber))
        # print(type(onlyTheNumber))
        # print(type(myString))
        # print(type(myNumber))
