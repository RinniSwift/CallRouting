
class SolutionOne(object):

	def create_number_dictionary(self, file):

		route_costs_dict = {}

		with open(file) as txt_file:
			for line in txt_file:
				arr_per_line = line.split(",")
				route_costs_dict[arr_per_line[0]] = arr_per_line[1][:-1]

		print(route_costs_dict)


def main():
	solution = SolutionOne()
	solution.create_number_dictionary("route-costs-100.txt")

if __name__ == "__main__":
	main()