´´´
Create a function that accepts a list and returns the last item in the list.
The list can be either homogeneous or heterogeneous.
´´´
def getLastItem(lst):
	last = lst[0];
		for element in lst:
			last = element
	return last
