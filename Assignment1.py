""" Question-1
Both for loops and while loops are used for repetition in Python, 
but they are generally suited for different scenarios. 
Here's an explanation with examples:

1. for loop:

When to use:  Use a for loop when you know in advance how many times you need to iterate.  
This is often the case when you are working with a sequence (like a list, tuple, string, or range) or any iterable object.
"""
#Example-
# Iterating through a list of fruits
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

"""
2. while loop:

When to use: Use a while loop when the number of iterations is not known in advance and depends on a certain condition being met.  
The loop continues as long as the condition is True.
"""

#Examples:
# Counting until a certain value
count = 0
while count < 10:
    print(count)
    count += 1

""" 
Question2-
"""
sum = 0
for i in range(1, 11):
    sum = sum + i
    print("Sum of first 10 natural no: ", sum)
    