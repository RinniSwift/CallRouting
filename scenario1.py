
class SolutionOne(object):

	def __init__(self, file_name):
		self.file_name = file_name

	def create_number_dictionary(self):

		route_costs_dict = {}

		with open(self.file_name) as txt_file:
			for line in txt_file:
				arr_per_line = line.split(",")
				route_costs_dict[arr_per_line[0]] = arr_per_line[1][:-1]

		return route_costs_dict

	def search_number(self, number):
		all_route_costs = self.create_number_dictionary()

		while len(number) > 1:

			try:
				if all_route_costs[number] is not None:
					return all_route_costs[number]
			except:
				number = number[:-1]

		return None


def main():
	solution = SolutionOne("route-costs-100.txt")

	print(solution.search_number("+44918964408384"))

if __name__ == "__main__":
	main()