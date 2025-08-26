


# 36-dars
# namuna funktsiya
# def name_function(value1, value2):
#     # body_function
#     return f'{value1}  {value2}'.upper()

# Yangi fileda test function yozamiz 
# funktsiya yoziladigan file nomi mavjud funksiya nomi bilan boshlanishi maqsadfa muvofiq
# masalan funktsiyamiz yangi.py fileda test funktsiyamiz esa yangi_test.py nomlanishi maqul ko'riladi

def get_titled(val1, val2):
    return f'{val1}  {val2}'.title()

# test file ichida 
import unittest
from Function import get_titled

# class ni ham function.py nomiga mos boshlanishi maqul
clas FuncTest(unittest.TestCase):
    def test_get_titled(self):
        text=get_titled('value1', 'value2')
        self.assertEqual(text, 'Value1 Value2')

unittest.main()
    
# shu tarzda funktsiyalar tekshiriladi bu namuna edi



num=int(input('Please enter a number:'))

# Even or odd

word='even' if num%2==0 else 'odd'

# Prime Check

if num>1:
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            prime_status='not prime'
            break
        
    else:
        prime_status='prime'
else:
    prime_status='not prime'
    
print(f"{num} is {word} and {prime_status}.")


# Check if a number is even, odd, or prime.

# num = int(input('Please enter a number: '))

# # Even or Odd
# word = 'even' if num % 2 == 0 else 'odd'

# # Prime Check
# if num > 1:
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             prime_status = 'not prime'
#             break
#     else:
#         prime_status = 'prime'
# else:
#     prime_status = 'not prime'

# print(f"{num} is {word} and {prime_status}.")


# Convert temperatures between Celsius, Fahrenheit, and Kelvin.



# def Celsius():
#     print("Convert Celsius to :")
#     print("1. Fahrenheit")
#     print("2. Kelvin")
    
#     def Kelvin(amount):
#         return amount+273.15
    
#     def Fahrenheit(amount):
#         return (amount*9/5) + 32
#     change={
#         "1": Fahrenheit,
#         "2": Kelvin
#     }
#     to_do=input("Enter a number 1 or 2 : ")
    
#     converter=change.get(to_do, None)

#     if converter:
#         amount=float(input("Enter temperature in Celsius : "))
#         print(f"Converted temperature : {converter(amount)}")
#     else:
#         print("Invalid choice!!!")
        
        
# def Kelvin():
#     print("Convert Celsius to :")
#     print("1. Fahrenheit")
#     print("2. Celsius")
    
#     def Celsius(amount):
#         return amount-273.15
    
#     def Fahrenheit(amount):
#         return (amount-273.15)*9/5 + 32
#     change={
#         "1": Fahrenheit,
#         "2": Kelvin
#     }
#     to_do=input("Enter a number 1 or 2:  ")
    
#     converter=change.get(to_do, None)

#     if converter:
#         amount=float(input("Enter temperature in Celsius : "))
#         print(f"Converted temperature : {converter(amount)}")
#     else:
#         print("Invalid choice!!!")
        
        
# def Fahrenheit():
#     print("Convert Celsius to :")
#     print("1. Kelvin")
#     print("2. Celsius")
    
#     def Kelvin(amount):
#         return (amount-32)*5/9+273.15
    
#     def Celsius(amount):
#         return (amount-32)*5/9
#     change={
#         "1": Kelvin,
#         "2": Celsius
#     }
#     to_do=input("Enter a number 1 or 2:  ")
    
#     converter=change.get(to_do, None)

#     if converter:
#         amount=float(input("Enter temperature in Celsius : 2"))
#         print(f"Converted temperature : {converter(amount)}")
#     else:
#         print("Invalid choice!!!")

# while True:
#     print('Please choose one of scales')
#     print("1. Celsius")
#     print("2. Kelvin")
#     print("3. Fahrenheit")
#     print("To exit enter x")
#     choice=input('Please enter (1-3) :')
#     if choice.lower()=='x':
#         print('Bye')
#         break
#     option={
#         "1" : Celsius,
#         "2" : Kelvin,
#         "3" : Fahrenheit
#     }
#     action=option.get(choice, None)
#     if action:
#         action()
#     else:
#         print('Invalid choice.')
        






# Reverse a string without using slicing.


# word=input('Enter your word please: ')
# list_result=list(reversed(word))
# str1="".join(list_result)
# print(list_result)
# print(str1)
# print(f"Entered word was {str1[::-1]}")



# Count vowels, consonants, digits, and special characters in a string.

# word=input("Please enter anything you want :")
# vowels='AOIUEaoiue'
# num_vowel=0
# nums=0
# characters=0
# for char in word:
#     if char in vowels:
#         num_vowel+=1
#     elif char.isdigit():
#         nums+=1
#     elif char.isalpha():
#         pass
#     else:
#         characters+=1
        
# # Better Output
# print(f"\nAnalysis of '{word}':")
# print(f"Vowels: {num_vowel}")
# print(f"Numbers: {nums}")
# print(f"Special characters: {characters}")




# Generate a list of squares of numbers from 1 to 20 using list comprehension.


# squares=[i**2 for i in range(1, 21)]

# print(f'The result is {squares}')

# Find the largest and smallest number in a list without using max() and min().
# works for only positive integers
# try:
#     new_list = []
#     while True:
#         num = input("Enter a number to add to list (or hit enter to stop): ")
#         if not num.isdigit():
#             print("Bye")
#             break
#         else:
#             n = int(num)
#             new_list.append(n)

#     if not new_list:  # Prevent IndexError if no numbers were entered
#         raise IndexError

#     # Calculate min and max AFTER collecting input
#     minimum = new_list[0]
#     maximum = new_list[0]
#     for num in new_list:
#         if minimum > num:
#             minimum = num
#         elif maximum < num:
#             maximum = num

#     print(new_list)
#     print(f"The greatest number in list {maximum}")
#     print(f"The smallest number in list {minimum}")

# except NameError:
#     print('Invalid value')
# except IndexError:
#     print("Exit")



# Remove duplicates from a list while keeping the original order.

# original_list=[ 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 8, 89, 1, 2, 212, 2, 3, 25, 36, 4 ]
# new_list=[]

# for item in original_list:
#     if item not in new_list:
#         new_list.append(item)

# print(new_list)


# unique_list=list(dict.fromkeys(original_list))

# print(unique_list)
# seen=set()
# unique_new_list=[x for x in original_list if not (x in seen or seen.add(x))]

# print(unique_new_list)



# Create a dictionary from two lists (keys and values).

# keys=[1, 2, 3, 4, 5]
# values=['python', 'c++', 'c#', 'java', 'go']
# my_dict=dict(zip(keys, values))

# print(my_dict)



# Sort a list of tuples by the second element.

# data=[(1, 6), (3, 2), (5, 4), (7, 1)]
# sorted_data=sorted(data, key=lambda x: x[1])
# print(sorted_data)

# Create a multiplication table (1–10) using nested loops.


# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i*j}")
#     print()

# sentence = "apple orange apple banana orange apple"
# words = sentence.split()

# frequency = {}  # empty dictionary

# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1

# print(frequency)










