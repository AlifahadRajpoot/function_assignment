# Basic Functions:

# Write a function to calculate the area of a circle given its radius.

# def calculate_circle_area():
#     pi_1= float(input("Enter the value of PI:"))
#     radius_1=float(input("Enter the radius of the circle:"))
#     area = pi_1 * (radius_1 ** 2)
#     return area

# print(calculate_circle_area())

# Create a function that takes two numbers and returns their sum.

# def add_numbers():
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
#     return num1 + num2
# print(add_numbers())

#  Write a function that takes a string and returns it reversed.

# def reverse_string():
#     string = input("Enter a string: ")
#     return string[::-1]
# print(reverse_string())

# Write a function to count the vowels in a given string.

# def count_vowels():
#     string = input("Enter a string: ")
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in string:
#         if char in vowels:
#             count += 1
#             return count
# print(count_vowels())

#                                       ________________________________________

# Intermediate Functions:

#  Create a function that takes a list of numbers and returns the largest number.

# def find_largest():
#     num = [1,2,32,42,21,55]
#     return max(num)
# print(find_largest())
        
#  Write a function to check whether a string is a palindrome.

# def check_palindrome(s):
#     txt = s[::-1]
#     if txt == s:
#         return True
#     else:
#         return False
# print(check_palindrome("radar"))

# Create a function that takes a list of integers and returns the sum of all even numbers.

# def sum_even_numbers():
#     numbers = [1, 2, 3, 4, 5, 6]
#     even_sum = 0
#     for num in numbers:  
#         if num % 2 == 0:  
#             even_sum += num  
#     if even_sum > 0:
#         return even_sum  
#     else:
#         return "There are no even numbers in the list."

# print(sum_even_numbers())

#  Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#         return abs(a)
# print(gcd(48, 18))

# Create a function that accepts a dictionary and returns the key with the highest value.

# def find_highest_value_key(dictionary):
#     return max(dictionary, key=dictionary.get)
# print(find_highest_value_key({"a": 1, "b": 2, }))

#                      _________________________________________________

# Advance Functions:

# Write a function that calculates the power of a number without using the ** operator.

# def power(base, exponent):
#     if exponent == 0:
#         return 1
#     elif exponent < 0:
#         return 1 / power(base, -exponent)
#     else:
#         return base * power(base, exponent - 1)
# print(power(2, 3))  

# Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.

# def convert_temperature(celcius):
#     fahrenheit = (celcius * 9/5) + 32
#     return fahrenheit
# print(convert_temperature(0))  

# Create a function to check if two strings are anagrams.

# def are_anagrams(str1, str2):
#     return sorted(str1) == sorted(str2)
# print(are_anagrams("listen", "silent"))  

#  Write a function that takes a list and removes all duplicate elements.

# def remove_duplicates(lst):
#     return list(set(lst))
# print(remove_duplicates([1, 2, 2, 3, 4, 4]))

#                           ___________________________________________________________