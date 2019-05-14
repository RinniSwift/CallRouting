class SolutionOne(object):
    
	def __init__(self, phone_file, carrier_file_array):
		""" Initialize a new SolutionOne object
			- Parameters:
				- phone_file :
				- carrier_file_array : """

		self.phone_file = phone_file
		self.carrier_file_array = carrier_file_array


	def create_route_dictionary(self):
		''' create a key-value pair for each route and its cost

			Time Complexity : O(n * m) where n is the number of lines, m is the length of each line 
			Space Complexity : O(n) where n is the size of the dictionary
		'''
		route_costs_dict = {}  # O(1) time | O(1) space

		try:
			with open(self.route_file) as txt_file: # O(1) time | O(1) space

				for line in txt_file: # O(n) time 

					arr_per_line = line.split(",") # O(n) time | O(n) space
					if arr_per_line[0] in route_costs_dict:
						
						route_costs_dict[arr_per_line[0]].append(arr_per_line[1][:-1]) # O(1) time | O(1) space
					else:
						route_costs_dict[arr_per_line[0]] = [arr_per_line[1][:-1]] # O(1) time | O(1) space
						
		except IOError as error:
			print("error {} found while opening file {}".format(error, self.route_file))

		return route_costs_dict


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
	

def main():
	pass



if __name__ == "__main__":
	main()