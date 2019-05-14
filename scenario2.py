class SolutionTwo(object):

	def __init__(self, route_file, number_file):

		self.route_file = route_file
		self.number_file = number_file


	def create_route_dictionary(self):
		''' 

			Time Complexity : 
			Space Complexity : 
		'''
		route_costs_dict = {}  # O(???) time | O(???) space


		with open(self.route_file) as txt_file: # O(???) time | O(???) space

			for line in txt_file: # O(???) time 
				arr_per_line = line.split(",") # O(?) time | O(?) space
				route_costs_dict[arr_per_line[0]] = arr_per_line[1][:-1] # O(?) time | O(?) space

		return route_costs_dict


	def create_number_array(self):

		num_arr = []
		with open(self.number_file) as file:

			for line in file:
				num_arr.append(line[:-1])
		return num_arr


	def find_price(self, number, route_dictionary):
		''' 

			Time Complexity :
			Space Complexity : 
		'''

		while len(number) > 2: # O(?) time worst case | O(?) time best case 

			try: 
				if route_dictionary[number] is not None: #O(1) time 
					return route_dictionary[number] # O(1) time
			except:
				number = number[:-1] # O(?) time | O(?) space

		return None

	def create_route_numbers_dict(self):

		numbers = self.create_number_array()
		route_dict = self.create_route_dictionary()

		result_dict = {}
		for num in numbers:
			#print(num)
			price = self.find_price(num, route_dict)
			result_dict[num] = price

		return result_dict


def main():
	solution = SolutionTwo("route-costs-106000.txt", "phone-numbers-100.txt")
	print(solution.create_route_numbers_dict())





if __name__ == "__main__":
	main()