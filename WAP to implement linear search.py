#21.WAP to implement linear search.
def linear_search(list1, n, key):
  
    # Searching list1 sequentially
    for i in range(0, n):
        if (list1[i] == key):
            return i
  
    return -1
  
# Driver code
list1 = [10, 20, 8, 19, 45, 23, 73, 90]
n = len(list1)
key = 23
  
# Function call
res = linear_search(list1, n, key)
  
if (res != -1):
    print("Element is present at index", str(res))
else:
    print("Element is not present in array")
