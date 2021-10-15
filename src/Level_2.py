from bs4 import BeautifulSoup
import requests
import re
import phonenumbers
import urllib.request

import openpyxl
from openpyxl  import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter, column_index_from_string


#******* AVOID BEING BLOCKED *******
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

companyName = "Caprock Academy"
companyAddress = "headquarters"
whichCountry = "US"

#CREATING URL FOR GOOGLE SEARCHING
text = ("phone number of {0} {1} ".format(companyName, companyAddress))
myCurrentURL = 'https://google.com/search?q=' + text

#ACCESING TO URL's INFO
response = requests.get(myCurrentURL, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

title_H2 = soup.find('h2', attrs={'class':'qrShPb kno-ecr-pt PZPZlf mfMhoc'}).text
# this comparison must to turn title and companyName into lower case so that can be compared without errors
if title_H2.lower() == companyName.lower():
    box_Of_Info = soup.find('div', attrs={"class": "UDZeY OTFaAf"})   
    STRING_box_Of_Info = str(box_Of_Info)
    
    for match in phonenumbers.PhoneNumberMatcher(STRING_box_Of_Info, whichCountry):
        only_Number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
        print(only_Number)

# tagSearched_Level_2= soup.find_all('div', attrs={'class': 'liYKde g VjDLd'})# Level 2
# # search_CompanyName = soup.find_all('span', text = re.compile(companyName))# Level 2

# whichCountry = "US"


# if tagSearched_Level_2:
# 	for divs in tagSearched_Level_2:
# 		spans_In_Container_Right_Side = divs.findChildren("span")
# 		spans_In_Container_Right_Side_To_String = str(spans_In_Container_Right_Side)
# 		if companyName in spans_In_Container_Right_Side_To_String:
# 			for match in phonenumbers.PhoneNumberMatcher(spans_In_Container_Right_Side_To_String, whichCountry):
# 				only_Number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
# 				print(only_Number)

                # letter_Of_Column_To_Put_Phone_Number = "E"
                # concatenater_Row_With_Column_For_Number = letter_Of_Column_To_Put_Phone_Number + string_Of_number_Of_Row_With_Name_Of_Companies
                # sh[concatenater_Row_With_Column_For_Number] = only_Number
                # wb.save(filename = chooseExcel_File)

