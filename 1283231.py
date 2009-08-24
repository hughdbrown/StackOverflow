def find_sum_to_zero(arr):
	arr = sorted(arr)
	for i, target in enumerate(arr):
		lower, upper = 0, len(arr)-1
		while lower < i < upper:
			tmp = target + arr[lower] + arr[upper]
			if tmp > 0:
				upper -= 1
			elif tmp < 0:
				lower += 1
			else:
				yield arr[lower], target, arr[upper]
				lower += 1
				upper -= 1

if __name__ == '__main__':
	# Get a list of random integers with no duplicates
	from random import randint
	arr = list(set(randint(-200, 200) for _ in range(50)))
	for s in find_sum_to_zero(arr):
		print s
