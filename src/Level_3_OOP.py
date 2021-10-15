from bs4 import BeautifulSoup
import requests
import re

import phonenumbers

class Level_3:
	def __init__(self, x_headers, x_whichCountry, x_companyName, x_companyAddress,  x_span_Class_Name, x_h3_Class_Name, x_div_Class_Name, x_children_tag_container_of_data_with_phonenumber, chooseExcel_File, choose_SHEET_Of_Your_Excel_File, wb, sh, rowM, string_Of_number_Of_Row_With_Name_Of_Companies):
		
		self.x_headers = x_headers # Will be asigned in Level_1
		self.x_whichCountry = x_whichCountry
		self.x_companyName = x_companyName 
		self.x_companyAddress = x_companyAddress 
		self.x_span_Class_Name = x_span_Class_Name 
		self.x_h3_Class_Name = x_h3_Class_Name
		self.x_div_Class_Name = x_div_Class_Name
		self.x_children_tag_container_of_data_with_phonenumber = x_children_tag_container_of_data_with_phonenumber
		self.chooseExcel_File = chooseExcel_File # Will be asigned in Level_1
		self.choose_SHEET_Of_Your_Excel_File = choose_SHEET_Of_Your_Excel_File
		self.wb = wb
		self.sh = sh
		self.rowM = rowM
		self.string_Of_number_Of_Row_With_Name_Of_Companies = string_Of_number_Of_Row_With_Name_Of_Companies


		#CREATING URL FOR GOOGLE SEARCHING
		text = ("phone number of {0} {1} ".format(self.x_companyName, self.x_companyAddress))
		myCurrentURL = 'https://google.com/search?q=' + text

		response = requests.get(myCurrentURL, headers=self.x_headers)

		content_HTML = response.text
		soup = BeautifulSoup(content_HTML, "lxml")

		# print(soup.prettify())

		search_classMW31ZE = soup.find_all('span', attrs={'class': self.x_span_Class_Name})# Level 1 'mw31Ze'
		search_CompanyName = soup.find_all('h3', text = re.compile(self.x_companyName), attrs = {'class' : self.x_h3_Class_Name})# Level 3 step 1 'LC20lb DKV0Md'

		search_Each_div_Container = soup.find_all('div', attrs={'class': self.x_div_Class_Name})# Level 3 step 2 'tF2Cxc'

		for divs in search_Each_div_Container:
			if search_CompanyName:
				chaotic_SPAN = divs.findChildren(self.x_children_tag_container_of_data_with_phonenumber) #'span'
				# print(chaotic_SPAN)
				for each_SPAN in chaotic_SPAN:
					new_SPAN_That_Needs_To_Be_STRING = str(each_SPAN)
					for match in phonenumbers.PhoneNumberMatcher(new_SPAN_That_Needs_To_Be_STRING, self.x_whichCountry):
						global only_Number
						only_Number = phonenumbers.format_number(match.number, phonenumbers.PhoneNumberFormat.E164)
						# print(only_Number)
						self.sh['F' + self.string_Of_number_Of_Row_With_Name_Of_Companies] = only_Number
						self.wb.save(filename = self.chooseExcel_File)

						