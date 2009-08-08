def costed_sort(unsorted):
	def exchange(unsorted, i, j):
		src_val, dst_val = unsorted[i], unsorted[j]
		move_cost = src_val + dst_val
		print "Moving (%d,%d) at cost of %d" % (src_val, dst_val, move_cost)
		unsorted[i], unsorted[j] = dst_val, src_val
		return move_cost
	s = sorted(unsorted)
	d = dict((i, v) for i, v in enumerate(s))
	cost = 0
	print unsorted
	out_of_place = [ (i, sorted_val, unsorted_val) for i, sorted_val, unsorted_val in zip(range(len(arr)), s, arr) if sorted_val != unsorted_val]

	elim = []
	for i in range(len(out_of_place)):
		xi, s_val1, un_val1 = out_of_place[i]
		for j in range(i+1, len(out_of_place)):
			xj, s_val2, un_val2 = out_of_place[j]
			if s_val1 == un_val2 and s_val2 == un_val1:
				elim.append(i)
				elim.append(j)
				cost += exchange(arr, xi, xj)
				break
	for x in sorted(elim, reverse=True):
		out_of_place.pop(x)
	if not len(out_of_place):
		return cost
	else:
		left, right = out_of_place[0], out_of_place[1:]
		sum_right = sum(rval for _, rval, _ in right)
		projected_cost = len(right) * left[1] + sum_right
		if left[0] != 0:
			alternative_cost = (len(right) + 1) * s[0] + sum_right + 2*left[1]
			if alternative_cost < projected_cost:
				src_index, dst_index = 0, arr.index(left[1])
				print src_index, dst_index
				cost += exchange(arr, dst_index, src_index)

	for i, src_val in enumerate(s) :
		src_index = arr.index(src_val)
		# While the lowest cost item is out of place...
		while src_index != i:
			# Find out which belongs in current spot
			dst_val = d[src_index]
			dst_index = arr.index(dst_val)

			# Swap lowest cost misplaced item with the correct item
			cost += exchange(arr, src_index, dst_index)

			print arr
			src_index = dst_index
	return cost


if __name__ == '__main__':
	#arr = [1] + list(range(4,10))
	#for _ in range(100):
	#	shuffle(arr)
	#	print "----"
	#	print costed_sort(arr)
	arr = [80,1,90,100, 110, 70]
	print costed_sort(arr)
