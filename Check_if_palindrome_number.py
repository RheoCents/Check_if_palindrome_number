#Write a program to check if the given number is a palindrome number.

#A palindrome number is a number that is the same after reverse. 
#For example, 545, is the palindrome numbers

user_input_number = input('Good day, please give me a number ')
reversed_user_input_number = int(str(user_input_number)[::-1]) 
quotient_of_original_and_reversed = int(user_input_number)/int(reversed_user_input_number)
if  quotient_of_original_and_reversed == 1.0:
    print('The inputted number is ', user_input_number)
    print('The inputted number is a Palindrome number')
else:
    print('The inputted number is ', user_input_number)
    print('The inputted number is a not Palindrome number')