#13.WAP to display all the multiples of 3 within the range 10 to 50.
list=[]                                    # Empty list to store values
for i in range (10,51):                    # getting values from 10-50 using for loop 
    if i%3==0:                             # divide by 3 and reminder should be 0
        list.append(i)                     # values which satisfies condition appends to list
print('Numbers multiple of 3 within the range 10-50 is',list)
