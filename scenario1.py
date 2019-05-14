
class SolutionOne(object):

	def __init__(self, file_name):
		self.file_name = file_name

	def create_number_dictionary(self):
		''' create a key-value pair for each route and its cost

			Time Complexity : O(n * m) where n is the number of lines, m is the length of each line 
			Space Complexity : O(n) where n is the size of the dictionary
		'''
		route_costs_dict = {}  # O(1) time | O(1) space

		try:
			with open(self.file_name) as txt_file: # O(1) time | O(1) space

				for line in txt_file: # O(n) time 

					arr_per_line = line.split(",") # O(n) time | O(n) space
					if arr_per_line[0] in route_costs_dict:
						
						route_costs_dict[arr_per_line[0]].append(arr_per_line[1][:-1]) # O(1) time | O(1) space
					else:
						route_costs_dict[arr_per_line[0]] = [arr_per_line[1][:-1]] # O(1) time | O(1) space
						
		except IOError as error:
			print("error {} found while opening file {}".format(error, self.file_name))

		return route_costs_dict 



	def find_cost(self, number):
		''' look up number in dictionary of route-cost.

			Time Complexity : O(n) worst case where n is the length of the number | O(1) best case if initial number is the route
			Space Complexity : O(1) space
		'''

		all_route_costs = self.create_number_dictionary() # O(n) time | O(n) space 
		
		while len(number) > 1: # O(n-1) time worst case | O(1) time best case if initial number is the route
			try: 
				if all_route_costs[number] is not None: #O(1) time 
					costs = all_route_costs[number]
					return min(costs)
			except:
				number = number[:-1] # O(1) time | O(n) space


def main():
	solution = SolutionOne("route-costs-106000.txt")
	print(solution.find_cost("+13053909087"))



if __name__ == "__main__":
	main()