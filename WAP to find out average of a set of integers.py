#4. WAP to find average of a set of integers.
answers = int(input("How many numbers would you like to average? "))

numbers = []

for answer in range(1, answers + 1):
    number = int(input("Enter number {}: ".format(answer)))
    numbers.append(number)

average = sum(numbers) / answers
print("The numbers given were:", numbers)
print("The average is:", average)
