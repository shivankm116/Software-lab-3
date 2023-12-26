#18.WAP to print the numbers from a given number n till 0 using recursion.
# between 1 to N in reverse order

# Recursive function to print 
# from N to 1
N=int(input("ENETR A POSITIVE INTEGER:::::"))
def PrintReverseOrder(N):
	
	for i in range(N, 0, -1):
		print(i, end = " ");

# Driver code
if __name__ == '__main__':
	
	
	PrintReverseOrder(N);


