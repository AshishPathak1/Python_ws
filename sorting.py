# def insertionsort(arr,n):
#     for i in range(1,n):
#         key=arr[i]
#         j=i-1
#         while j>=0 and arr[j]>key:
#             arr[j+1] = arr[j]
#             j-=1
#         arr[j+1]=key

# def selectionsort(arr,n):
#     for i in range(n):
#         min_idx = i
#         for j in range(i,n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i],arr[min_idx] = arr[min_idx],arr[i]

# def quicksort(arr:list,left:int,right:int):
#     if left < right:
#         pos = partition(arr,left,right)
#         quicksort(arr,left,pos-1)
#         quicksort(arr,pos+1,right)

# def partition(arr,left,right):
#     i = left
#     j = right - 1
#     pivot = arr[right]
#     while i<j:
#         while i<right and arr[i] < pivot:
#             i+=1
#         while j>left and arr[j] >= pivot:
#             j-=1
#         if i<j:
#             arr[i],arr[j] = arr[j],arr[i]
#     if pivot < arr[i]:
#         arr[i],pivot = pivot,arr[i]
       
#     return i



def partition(array, low, high):

	pivot = array[high]
	i = low - 1
	for j in range(low, high):
		if array[j] <= pivot:
			i = i + 1
			(array[i], array[j]) = (array[j], array[i])
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	return i + 1

def quickSort(array, low, high):
	if low < high:
		pi = partition(array, low, high)
		quickSort(array, low, pi - 1)
		quickSort(array, pi + 1, high)


data = [3,5,6,9,5,6,6,9]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
