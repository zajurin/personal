from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

from listOfCountries_and_codes import GetCountryCode

# Delete them
from Level_3 import only_Number
print(only_Number)

# GetCountryCode('United States')

# ______________________________________________________________________________________________________________________


# from googletrans import Translator

# spanish_country = 'Irlana del Norte'

# translator = Translator()

# translate_text = translator.translate(spanish_country, dest='en')  
# print(translate_text.text)

#__________________________________________________________________________________________




# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

# # myCurrentURL = "http://www.pythonscraping.com/pages/warandpeace.html"

# myCurrentURL = "https://www.google.com/search?q=phone+number+of+caprock+academy+headquarters&rlz=1C1CHBD_esMX778MX778&oq=&aqs=chrome.0.35i39i362l3j35i19i39i362j35i39i362l2j35i19i39i362j35i39i362...8.508012590j0j7&sourceid=chrome&ie=UTF-8"

# response = requests.get(myCurrentURL, headers=headers)
# soup = BeautifulSoup(response.text, 'html.parser')
	

# for x in soup:
# 	# nameList_second_filter = soup.find_all('h3', text = "Caprock Academy")
# 	nameList = list(soup.find_all('h2', attrs = {'class': 'qrShPb kno-ecr-pt PZPZlf mfMhoc'}, text = "Caprock Academy"))
# 	if nameList:
# 		for x in nameList:
# 			print(x)
# 	# print(nameList[0].contents)

# # for name in list(nameList.descendants):
# # 	print(name)
