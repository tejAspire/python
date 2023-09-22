#PYTHON-PART B 
#1) Write a program to perform addition, subtraction, multiplication, division, 
#and modulo division on two integers. 
num1 = int(input("Enter the first integer: ")) 
num2 = int(input("Enter the second integer: ")) 
addition = num1 + num2 
print(f"Addition: {addition}") 
subtraction = num1 - num2 
print(f"Subtraction: {subtraction}") 
multiplication = num1 * num2 
print(f"Multiplication: {multiplication}") 
if num2 != 0: 
division = num1 / num2 
print(f"Division: {division}") 
else: 
print("Division by zero is undefined.") 
if num2!= 0: 
modulo = num1 % num2 
print(f"Modulo Division: {modulo}") 
else: 
print("Modulo Division by zero is undefined.") 
OUTPUT: Enter the first integer: 2 
Enter the second integer: 3 
Addition: 5 
Subtraction: -1 
Multiplication: 6 
Division: 0.6666666666666666 
Modulo Division: 2 
#2) Program to find the greatest number from three numbers 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 
num3 = float(input("Enter the third number: ")) 
maximum = max(num1, num2, num3) 
print(f"The greatest number is: {maximum}") 
OUTPUT: 
Enter the first number: 3 
Enter the second number: 4 
Enter the third number: 5 
The greatest number is: 5.0 
#3) Program to calculate roots of a quadratic equation 
import math 
a = float(input("Enter coefficient a: ")) 
b = float(input("Enter coefficient b: ")) 
c = float(input("Enter coefficient c: ")) 
discriminant = b**2 - 4*a*c 
if discriminant > 0: 
root1 = (-b + math.sqrt(discriminant)) / (2*a) 
root2 = (-b - math.sqrt(discriminant)) / (2*a) 
print(f"Root 1: {root1}") 
print(f"Root 2: {root2}") 
elif discriminant == 0: 
root = -b / (2*a) 
print(f"Single root: {root}") 
else: 
real_part = -b / (2*a) 
imaginary_part = math.sqrt(-discriminant) / (2*a) 
print(f"Complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i") 
OUTPUT: 
Enter coefficient a: 5 
Enter coefficient b: 6 
Enter coefficient c: 7 
Complex roots: -0.6 + 1.0198039027185568i and -0.6 - 1.019803902715568i 
#4) Program to classify a given number as prime or composite 
num = int(input("Enter a number: ")) 
if num > 1: 
for i in range(2, int(num/2) + 1): 
if (num % i) == 0: 
print(f"{num} is composite.") 
break 
else: 
print(f"{num} is prime.") 
else: 
print("1 is neither prime nor composite.") 
OUTPUT:  
Enter a number: 3 
3 is prime. 
Enter a number: 4 
4 is composite. 
Enter a number: 1 
1 is neither prim nor composite. 
#5) Program to find whether a given character is present in a given string and 
print its index 
string = input("Enter a string: ") 
char = input("Enter a character to search for: ") 
index = -1 
for i in range(len(string)): 
if string[i] == char: 
index = i 
break 
if index!= -1: 
print(f"The character '{char}' is present at index {index}.") 
else: 
print(f"The character '{char}' is not present in the string.") 
OUTPUT: 
Enter a string: python 
Enter a character to search for: y 
The character 'y' is present at index 1. 
#6) Program to check whether a given year is a leap year or not: 
year = int(input("Enter a year: ")) 
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
print(f"{year} is a leap year.") 
else: 
print(f"{year} is not a leap year.") 
OUTPUT: 
Enter a year: 1990 
1990 is not a leap year. 
#7) Program to find the Greatest Common Divisor (GCD) of two numbers 
import math 
num1 = int(input("Enter the first number: ")) 
num2 = int(input("Enter the second number: ")) 
gcd = math.gcd(num1, num2) 
print(f"The GCD of {num1} and {num2} is: {gcd}") 
OUTPUT: 
Enter the first number: 12 
Enter the second number: 24 
The GCD of 12 and 24 is: 12 

OR
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is:", gcd)
#8) Program to add two complex numbers using a Complex class 
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

def add_complex(complex1, complex2):
    real_sum = complex1.real + complex2.real
    imag_sum = complex1.imag + complex2.imag
    return Complex(real_sum, imag_sum)

# Example usage
n = int(input("Enter the number of complex numbers (N >= 2): "))

if n >= 2:
    complex_numbers = []
    for i in range(n):
        real = float(input(f"Enter real part of complex number {i+1}: "))
        imag = float(input(f"Enter imaginary part of complex number {i+1}: "))
        complex_numbers.append(Complex(real, imag))

    sum_complex = complex_numbers[0]
    for num in complex_numbers[1:]:
        sum_complex = add_complex(sum_complex, num)

    print(f"The sum of the complex numbers is: {sum_complex.real} + {sum_complex.imag}i")

else:
    print("Please enter a valid value for N (N >= 2).")

#9) Program using a Student class to calculate total marks and percentage 
class Student: 
def __init__(self, name, subject1, subject2, subject3): 
self.name = name 
self.subject1 = subject1 
self.subject2 = subject2 
self.subject3 = subject3 
def calculate_total(self): 
return self.subject1 + self.subject2 + self.subject3 
def calculate_percentage(self): 
total_marks = self.calculate_total() 
return (total_marks / 300) * 100 
# Input student details 
name = input("Enter student's name: ") 
marks1 = float(input("Enter marks in subject 1: ")) 
marks2 = float(input("Enter marks in subject 2: ")) 
marks3 = float(input("Enter marks in subject 3: ")) 
student = Student(name, marks1, marks2, marks3) 
total_marks = student.calculate_total() 
percentage = student.calculate_percentage() 
print(f"Student Name: {student.name}") 
print(f"Total Marks: {total_marks}") 
print(f"Percentage: {percentage}%") 
OUTPUT: 
Enter student's name: ABC 
Enter marks in subject 1: 98 
Enter marks in subject 2: 89 
Enter marks in subject 3: 78 
Student Name: ABC 
Total Marks: 265.0 
Percentage: 88.33333333333333% 
#10) Program demonstrating a BankAccount class for account operations 
class BankAccount: 
def __init__(self, account_number, balance): 
self.account_number = account_number 
self.balance = balance 
def deposit(self, amount): 
if amount > 0: 
self.balance += amount 
print(f"Deposited ${amount}. New balance: ${self.balance}") 
else: 
print("Invalid deposit amount.") 
def withdraw(self, amount): 
if 0 < amount <= self.balance: 
self.balance -= amount 
print(f"Withdrew ${amount}. New balance: ${self.balance}") 
else: 
print("Insufficient funds or invalid withdrawal amount.") 
def get_balance(self): 
return self.balance 
# Create a BankAccount instance 
account = BankAccount("12345", 1000) 
# Perform account operations 
account.deposit(500) 
account.withdraw(200) 
print(f"Current balance: ${account.get_balance()}") 
OUTPUT: 
Deposited $500. New balance: $1500 
Withdrew $200. New balance: $1300 
Current balance: $1300 
