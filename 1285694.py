visited = set()
queue = Queue()
r = random tile
queue.add(r)
while not queue.empty():
	current = queue.pop()
	visited.add(current)
	for neighbor in current.neighbors():
		if neighbor not in visited:
			queue.add(neighbor)
if visited == set(all tiles):
	print "No islands"
else:
	print "Island starting at ", r


