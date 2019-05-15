class SolutionOne(object):
    
	def __init__(self, phone_file, carrier_file_array):
		""" Initialize a new SolutionOne object
			- Parameters:
				- phone_file :
				- carrier_file_array : """

		self.phone_file = phone_file
		self.carrier_file_array = carrier_file_array


	def create_route_dictionary(self, carrier_file):
		''' create a key-value pair for each route and its cost

			Time Complexity : O(n * m) where n is the number of lines, m is the length of each line 
			Space Complexity : O(n) where n is the size of the dictionary
		'''
		route_costs_dict = {}  # O(1) time | O(1) space

		try:
			with open(carrier_file) as txt_file: # O(1) time | O(1) space

				for line in txt_file: # O(n) time 

					arr_per_line = line.split(",") # O(n) time | O(n) space
					if arr_per_line[0] in route_costs_dict:
						
						route_costs_dict[arr_per_line[0]].append(arr_per_line[1][:-1]) # O(1) time | O(1) space
					else:
						route_costs_dict[arr_per_line[0]] = [arr_per_line[1][:-1]] # O(1) time | O(1) space
						
		except IOError as error:
			print("error {} found while opening file {}".format(error, carrier_file))

		return route_costs_dict


	def find_cost(self, number, route_dict):
		''' look up number in dictionary of route-cost.

			Time Complexity : O(n) worst case where n is the length of the number | O(1) best case if initial number is the route
			Space Complexity : O(1) space
		'''
		while len(number) > 1: # O(n-1) time worst case | O(1) time best case if initial number is the route
			try: 
				if route_dict[number] is not None: #O(1) time 
					costs = route_dict[number]
					return min(costs)
					
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
				minimum_costs = []
				for carrier_file in self.carrier_file_array:
					
					current_carrier_dict = self.create_route_dictionary(carrier_file)
					curr_min_cost = self.find_cost(num, current_carrier_dict)
					if curr_min_cost:
						minimum_costs.append(curr_min_cost)

				if len(minimum_costs) > 1:
					num_cost_dict[num] = min(minimum_costs)
					
					
		return num_cost_dict
	
	
def main():
	
	arr_of_carriers = ["route-costs-106000.txt", "route-costs-600.txt"]
	solution = SolutionOne("phone-numbers-3.txt", arr_of_carriers)

	print(solution.create_route_numbers_dict())



if __name__ == "__main__":
	main()