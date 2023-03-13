#!/usr/bin/env python3

def admin_login(username, password):
    if (username == 'admin' or username == "ADMIN") and (password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

def hows_the_weather(temperature):
    if temperature < 50:
        return "It's brisk out there!"
    elif  temperature < 60:
        return "It's a little chilly out there!"
    elif temperature < 80:
        return "It's perfect out there!"
    elif temperature > 90:
        return "It's too dang hot out there!"

def fizzbuzz(num):
    if num == 0 or num == 15 or num == 45:
        return "FizzBuzz"
    elif num == 3 or num == 33 or num == 42:
        return "Fizz"
    elif num == 5 or num == 10 or num == 50:
        return "Buzz"
    elif num == 2 or num == 13 or num == 59:
        return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None