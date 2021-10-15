def decorator_function(parameter_function):

	def internal_function():

		print("el valor de la suma es: ")

		#additional actions that decorates
		parameter_function()



		#Additional actions that decorates

		print("el valor de substract es: ")
	
	return internal_function