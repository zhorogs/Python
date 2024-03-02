#python primitive data types

#string

print("Hello"[0]);

#subscripting
#start counting at 0

#getting the last char
print("Hello"[4]);

#concactenate
print("123" + "456");

#integers

print(123 + 456);

#float

print(3.14159)

#boolean

True or False

#Type error, Type checking and Type Conversion

#num_char = len(input("What is your name?"));
#new_num_char = str(num_char);
#print("Your name contains " + new_num_char + "characters");

a = float(123)
print(type(a))

#print(70 + float("100.5"))
print(str(70) + str(100))

#challenge, add digits to 2 digit number

two_digit_number = input()

first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#add the two integers together
two_digit_number = first_digit + second_digit
print(two_digit_number)

#mathematical operators in addition to adding +

3 + 5
7 - 2
3 * 2
6 / 2

print(type(6/3))
print(2**3)

print(3*3+3/3-3)

#bmi challenge

height = input()
weight = input()

height_as_float = float(height)
weight_as_int = int(weight)
bmi = weight_as_int / (height_as_float ** 2)
