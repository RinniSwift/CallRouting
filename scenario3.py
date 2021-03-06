class SolutionOne(object):
    
	def __init__(self, phone_file, carrier_file_array):
		""" Initialize a new SolutionOne object
			- Parameters:
				- phone_file :
				- carrier_file_array : """

		self.phone_file = phone_file
		self.carrier_file_array = carrier_file_array
		self.all_route_dict = {}
		self.create_route_dictionary()

	def create_route_dictionary(self):
		''' create a key-value pair for each route and its cost

			Time Complexity : O(n * m) where n is the number of lines, m is the length of each line 
			Space Complexity : O(n) where n is the size of the dictionary
		'''
		#route_costs_dict = {}  # O(1) time | O(1) space

		for file_name in self.carrier_file_array:

			try:
				with open(file_name) as txt_file: # O(1) time | O(1) space
					for line in txt_file: # O(n) time 

						route_number , price = line.split(",") # O(n) time | O(n) space

						if route_number in self.all_route_dict:
							if float(price) < self.all_route_dict[route_number]:

								self.all_route_dict[route_number] = float(price) # O(1) time | O(1) space
						else:
							self.all_route_dict[route_number] = float(price) # O(1) time | O(1) space
							
			except IOError as error:
				print("error {} found while opening file {}".format(error, file_name))
				


	def find_cost(self, number):
		''' look up number in dictionary of route-cost.

			Time Complexity : O(n) worst case where n is the length of the number | O(1) best case if initial number is the route
			Space Complexity : O(1) space
		'''
		
		while len(number) > 1: # O(n-1) time worst case | O(1) time best case if initial number is the route
			try:
				if self.all_route_dict[number] is not None: #O(1) time 
					costs = self.all_route_dict[number]

					# print(costs)
					return costs
					
			except:
				number = number[:-1] # O(1) time | O(n) space

		return None
		
	def create_number_array(self):

		""" Creates an ...
			- Worst Case Runtime :
			- Worst Case Space : 
		"""

		phone_num_arr = []
		try:
			with open(self.phone_file) as file:
				for line in file:
					phone_num_arr.append(line[:-1])
		except IOError as error:
			print("error {} found while opening file {}".format(error, self.phone_file))
		
		return phone_num_arr

	
	def create_route_numbers_dict(self):

		numbers = self.create_number_array()
		num_cost_dict = {}

		for num in numbers:
			if num:

				curr_min_cost = self.find_cost(num)
				if curr_min_cost:
					num_cost_dict[num] = curr_min_cost

		return num_cost_dict
	
	
def main():
	
	arr_of_carriers = ["route-costs-100.txt", "route-costs-35000.txt", "route-costs-106000.txt", "route-costs-10000000.txt"]
	solution = SolutionOne("phone-numbers-1000.txt", arr_of_carriers)

	print(solution.create_route_numbers_dict())
	# solution.create_route_dictionary()



if __name__ == "__main__":
	main()