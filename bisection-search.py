##building a bisection search algorithm from scratch. yikes!

def in_bisect(list, search_val):
	'''returns whether search_val is in the list, using bisection search'''
	list = sorted(list)
	start_val = int(len(list))/2
	upper_bound = len(list)-1
	lower_bound = 0
	num_iterations = 0
	while num_iterations < len(list):
		print("Iteration #" + str(num_iterations+1))
		print("Searching at position " + str(start_val))
		if start_val >= len(list) and search_val != list[-1]:
			return False
		elif search_val == list[-1]:
			return True
		elif search_val == list[start_val]:
			return True
		elif search_val < list[start_val]:
			print("The search value is below the start value.")
			upper_bound = start_val
			start_val = int((upper_bound - lower_bound)/2) + lower_bound
			num_iterations += 1
		elif search_val > list[start_val]:
			print("The search value is above the start value.")
			lower_bound = start_val
			start_val = int((upper_bound - lower_bound)/2) + lower_bound
			num_iterations += 1
		print("Search position for next round is " + str(start_val))

x = [i for i in range(1000)]

print(in_bisect(x,270))
