#day-1-printing-start
print("hello world");

#interactive coding challenge
print("Day 1 - Python Print Function");
print("The function is declared like this:");
print("print('what to print')");

#string manipulation and code intelligence
#debug this

# Fix the code below 👇

#print(Day 1 - String Manipulation")
#print("String Concatenation is done with the "+" sign.")
  #print('e.g. print("Hello " + "world")')
#print(("New lines can be created with a backslash and n.")

#fixed
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#python input function
#input() will get the user input in console
#then print() will print the world "Hello" and the user's input
print("Hello" + input("What is your name?"))

#python variables
name = input("what is your name?")
print(name)

length = len(name)
print(length)

#or

print(len(name))

#variables challenge 
# There are two variables, a and b from input
# Write a program that switches the values stored in the variables a and b.
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇


# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#fixed

a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = a
a = b
b = c
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

#band name generator challenge

print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)