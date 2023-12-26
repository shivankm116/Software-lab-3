#14.WAP to display all integers within the range 100-200 whose sum of digits is an even number.
list=[]                   # empty list to store final Integers
for i in range(100,201):  # generating range 100-200
    i=str(i)              # convert i to string so that we can separate digits
    sum=0                 # sum of digits of individual number 
    for j in i:           # seprating every digit from integer
        j=int(j)          # conver it to integer for calculation
        sum=sum+j         
    if sum%2==0:          # if sum/2 gives reminder zero then it is even number
        list.append(i)    # if condition satisties we append i integer to list not the sum
print('All Integers Within The Range 100-200 Whose Sum Of Digits Is An Even Number is =',list)
