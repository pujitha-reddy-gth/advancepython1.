#1.Syntax Error Check
#Write a small code snippet that will produce a compile-time (syntax) error. Then fix it.
#Example: Missing colon in an if statement.
#if True 
   # print("hello")
if True:
    print("hello")
#2.ZeroDivisionError
#Take two numbers from the user and perform division. Handle the case when the denominator is 0.
try:
   x=int(input('enter the x value:'))  
   y=int(input('enter the y value:'))
   op=x/y
   print("op=",op)
except ZeroDivisionError: 
   print('error: divided by the zero not allowed')
#3.ValueError
#Ask the user for their age. Handle the case when the user enters a string instead of a number.
try:
   age=int(input('enter you age:'))
   print('enter you age:',age)
except ValueError:
   print('error: please enter a valid for age')
#4.TypeError
#Try adding an integer and a string together. Handle the error.
try:
   num1 = 5
   num2 ="pujitha"
   sum=num1+num2
   print(sum)
except TypeError:
   print('error:cannot add integer and string together')

#5.Finally Block
#Write a program that takes an integer input. No matter what error occurs, print "Program Completed" using finally.
try:
   number=int(input('enter integer number:'))
   print('enter integer',number)
except ValueError:
   print('error:enter valid integer ')
finally:
   print('completed program')

#6.Multiple Exceptions
#Ask the user for two numbers and perform division. Handle both ZeroDivisionError and ValueError separately.
try:
   numx=int(input('enter the numx value :'))
   numy=int(input('enter the numy value :'))
   result=numx/numy
   print('result :',result)
except ZeroDivisionError:
   print('error: zero divide by  not valid number')
except ValueError:
   print('enter valid integer valu ')

#7.File Handling Error
#Try to open a file named student_data.txt. If it doesn’t exist, show a proper error message.
try:
    open('./pujitha.txt','r')
except FileNotFoundError:
    print('file not found')

#8.Catch All Exceptions
#Write a program that asks for a number and prints its square. Use Exception to handle any unexpected errors.
try:
   num1=int(input('enter the  number'))
   print('square:',num1**2)
except Exception as e:
   print('an error occurred:',e)

#9.Custom Error Message
#If the user enters a negative age, raise a ValueError with a custom message: "Age cannot be negative!".
try:
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print("Your age is", age)
except ValueError as e:
    print("Error:", e)

#10.Safe Calculator
#Create a simple calculator (add, subtract, multiply, divide) that takes input from the user. Handle errors like invalid input, division by zero, etc.
def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        op = input("Enter operation (+, -, *, /): ")

        if op == '+':
            print("Result =", num1 + num2)
        elif op == '-':
            print("Result =", num1 - num2)
        elif op == '*':
            print("Result =", num1 * num2)
        elif op == '/':
            print("Result =", num1 / num2)
        else:
            print("Error: Invalid operator.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input, please enter numbers only.")

calculator()

   






