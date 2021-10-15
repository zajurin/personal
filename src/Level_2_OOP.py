from bs4 import BeautifulSoup
import requests
import re
import phonenumbers
import urllib.request

import openpyxl
from openpyxl  import load_workbook
from openpyxl import Workbook
from openpyxl.utils import get_column_letter, column_index_from_string

class Level_2:
    def __init__(self, x_companyName, x_companyAddress, x_headers, x_className_of_H2, x_className_of_div_with_Info, x_whichCountry, chooseExcel_File, choose_SHEET_Of_Your_Excel_File, wb, sh, rowM, string_Of_number_Of_Row_With_Name_Of_Companies):
        self.x_companyName = x_companyName
        self.x_companyAddress = x_companyAddress
        self.x_headers = x_headers
        self.x_className_of_H2 = x_className_of_H2
        self.x_className_of_div_with_Info = x_className_of_div_with_Info
        self.x_whichCountry = x_whichCountry
        self.chooseExcel_File = chooseExcel_File
        self.choose_SHEET_Of_Your_Excel_File = choose_SHEET_Of_Your_Excel_File
        self.wb = wb
        self.sh = sh
        self.rowM = rowM
        self.string_Of_number_Of_Row_With_Name_Of_Companies = string_Of_number_Of_Row_With_Name_Of_Companies

        #******* AVOID BEING BLOCKED *******
        # headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

        # companyName = "Caprock Academy"
        # companyAddress = "headquarters"
        # whichCountry = "US"

        #CREATING URL FOR GOOGLE SEARCHING
        text = ("phone number of {0} {1} ".format(self.x_companyName, self.x_companyAddress))
        myCurrentURL = 'https://google.com/search?q=' + text

        #ACCESING TO URL's INFO
        response = requests.get(myCurrentURL, headers=self.x_headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # title_H2 = soup.find('h2', attrs={'class':'qrShPb kno-ecr-pt PZPZlf mfMhoc'}).text
        title_H2 = soup.find('h2', attrs={'class': self.x_className_of_H2})
        print(title_H2)
        # # this comparison must to turn title and companyName into lower case so that can be compared without errors
        # if title_H2.lower() == self.x_companyName.lower():
        #     # box_Of_Info = soup.find('div', attrs={"class": "UDZeY OTFaAf"})   
        #     box_Of_Info = soup.find('div', attrs={"class": self.x_className_of_div_with_Info})   
        #     STRING_box_Of_Info = str(box_Of_Info)
            
        #     for match in phonenumbers.PhoneNumberMatcher(STRING_box_Of_Info, self.x_whichCountry):
        #         global only_Number
        #         only_Number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
        #         # print(only_Number)
        #         self.sh['F' + self.string_Of_number_Of_Row_With_Name_Of_Companies] = only_Number
        #         self.wb.save(filename = self.chooseExcel_File)