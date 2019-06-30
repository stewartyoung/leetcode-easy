egList1 = [1,2,4]
egList2 = [1,3,4]

def mergeTwoSortedListsUL(test_list1, test_list2):
	size_1 = len(test_list1) 
	size_2 = len(test_list2) 
	res = [] 
	i, j = 0, 0
	while i < size_1 and j < size_2: 
		if test_list1[i] < test_list2[j]: 
			res.append(test_list1[i]) 
			i += 1

		else: 
			res.append(test_list2[j]) 
			j += 1

	res = res + test_list1[i:] + test_list2[j:]

	return res

print(mergeTwoSortedListsUL(egList1, egList2))
