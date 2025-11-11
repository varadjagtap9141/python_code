arr = [10,45,20,30,40,50,60]
print("Original Array: ",arr)

# if you want to add an element into arr use append()
arr.append(100)
print("append array:",arr)

# if you want to sort an array into ascending order

arr.sort()
print("ascending array:",arr)

# if you want to sort an array into descending order use 
arr.reverse()
print("reverse array:",arr)

# if you want to delete last element of array
arr.pop()
print("after remove last element:",arr)

# if you want to remove any value in the array
arr.remove(45)
print("remove array element:",arr)

# if you want to delete any value by the index
del arr[2]
print("after deleting element:",arr)

# if you want to clear all element in array
arr.clear()
print("all array is empty:",arr)

# if you want to insert array in any index
arr.insert(0,10)
arr.insert(1,20)
arr.insert(2,30)
arr.insert(3,40)
print("after inserting array element:",arr)

arr2=[50,55,60,65]
print("Arr:",arr)
print("Arr 2:",arr2)

# if you want to merge two array
arr.extend(arr2)
print("extending arr is:",arr)