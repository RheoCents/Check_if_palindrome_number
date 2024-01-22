#Write a program to check if the given number is a palindrome number.

#A palindrome number is a number that is the same after reverse. 
#For example, 545, is the palindrome numbers

user_input_number = input('Good day, please give me a number ')
number_of_places_in_the_number = len(user_input_number)
reversed_user_input_number = int(str(user_input_number)[::-1]) 
print (number_of_places_in_the_number)
quotient_of_original_and_reversed = int(user_input_number)/int(reversed_user_input_number)
if  quotient_of_original_and_reversed == 1:
    print('The inputed number is a Palindrome number')
else:
    print('The inputed number is a Palindrome number')