#Write a program to check if the given number is a palindrome number.

#A palindrome number is a number that is the same after reverse. 
#For example, 545, is the palindrome numbers

user_input_number = input('Good day, please give me a number ')
number_of_places_in_the_number = len(user_input_number)
print (number_of_places_in_the_number)
negative_number_of_places_in_the_number = int(number_of_places_in_the_number) - int(number_of_places_in_the_number)*2 
print (negative_number_of_places_in_the_number)

for i in range (-1, negative_number_of_places_in_the_number, -1):
    if user_input_number == user_input_number[i]:
        print('The inputed number is a Palindrome number')
    else:
        print('The inputed number is a Palindrome number')