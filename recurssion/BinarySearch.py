def Binary_search(data,target,low,high):
	print(data,"\n",target,"\n",low,"\n",high)
	if target < low:
		return False
	else:
		mid = (low + high) // 2
		print(mid)
		if target == data[mid]:
			return True
		elif target < data[mid]:
			return Binary_search(data, target, low, mid -1)
		else:
			return Binary_search(data,target,mid + 1, high)

data = [10,12,14,16,18,20,22,24,26,28,30]
target = 24
result = Binary_search(data, target, 0, len(data) - 1)

if result:
    print(f'Target {target} found in the list data is {data}.')
else:
    print(f'Target {target} not found in the list data is {data}.')