import pycountry


# # ****************** Country and its Code ****************** 
# listOfCountries = pycountry.countries #constant
# whichCountry = 'United States'# dynamic variable

# nameOfCountry = listOfCountries.get(name=whichCountry)#
# yourCode = nameOfCountry.alpha_2
# print("{0} \n".format(nameOfCountry))
# print('your code is ' + yourCode)



# Constructor of Codes for eachCountry
class GetCountryCode:
	def __init__(self, my_whichCountry):
		listOfCountries = pycountry.countries #constant
	
		self.my_whichCountry = my_whichCountry

		nameOfCountry = listOfCountries.get(name=self.my_whichCountry)#
		global yourCode
		yourCode = nameOfCountry.alpha_2
		print(yourCode)



#********************** List of Countries *****************

def Get_all_countries():
	listOfCountries = list(pycountry.countries)
	whichCountry = 'United States'

	number = 0
	for x in listOfCountries:
		print("{0}".format(listOfCountries[number].name))
		number += 1