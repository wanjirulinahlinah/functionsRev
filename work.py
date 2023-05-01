# Write a Python function that takes two arguments (a and b) and returns their sum.
def add_num(a,b):
    
    return a+b
num1=25 
num2=55
print("The sum is",add_num(num1,num2)) 

# Write a Python function that takes a string as input and returns the string reversed.
def reverse_string(str):  
    str1 = ""   
    for i in str:  
        str1 = i + str1  
    return str1   
     
str = "AkiraChix"        
print("The original string is: ",str)  
print("The reverse string is",reverse_string(str)) # Function call  
# Write a Python function that takes a list of integers as input and returns the sum of all the integers in the list.
def sum(numbers):
    result = 0
    for x in numbers:
        result += x
    return result
print(sum((28, 72, 23, 50, 67)))

# Write a Python function that takes a list of integers as input and returns a new list with all the even numbers removed.
# def number (num b)_{
#     new_nums = []
#     for i in num
#     if i % 2! = 0:
#         new _ nums.append()
#         return new__nums
#         print(number([2,5,7,8,9]))S
# }

# Write a Python function that takes a list of integers as input and returns the highest value in the list.

list1 = [10, 20, 4, 45, 99]
list1.sort()
print("Largest element is:", list1[-1])

# Write a Python function that takes a list of strings as input and returns a new list with all the strings capitalized.

def wordCasing(word):
    return word.capitalize() if len(word)>3 else word.lower()
title = ('rose', 'sound', 'and')
result = list(map(wordCasing, title))
result[0] =result[0].capitalize()
print (result)

