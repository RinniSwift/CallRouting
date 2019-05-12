class SolutionOne(object):

	def __init__(self, route_file, number_file):

		self.route_file = route_file
		self.number_file = number_file


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
			print("error {} found while opening file {}".format(error, self.file_name))

		return route_costs_dict 


	def create_number_array(self):

		num_arr = []
		with open(self.number_file) as file:

			for line in file:
				num_arr.append(line[:-1])
		return num_arr


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

	def create_route_numbers_dict(self):

		numbers = self.create_number_array()
		route_dict = self.create_route_dictionary()
		result_dict = {}

		for num in numbers:
			cost = self.find_cost(num, route_dict)
			result_dict[num] = cost

		return result_dict 


def main():
	solution = SolutionOne("route-costs-106000.txt", "phone-numbers-1000.txt")
	print(solution.create_route_numbers_dict())



if __name__ == "__main__":
	main()