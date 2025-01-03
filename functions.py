#Activity 1
# def intro(name):
    
#     print("Hello, Good morning! I am", name)

# user_name = input("Enter your name")
# intro(user_name)

#Activity 2
# Factorial of a number using recursion
# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)

# num = int(input("Enter a number"))

# # check if the number is negative
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", recur_factorial(num))

#Activity 3
# # Program make a simple calculator

# # This function adds two numbers
# def add(x, y):
#     return x + y

# # This function subtracts two numbers
# def subtract(x, y):
#     return x - y

# # This function multiplies two numbers
# def multiply(x, y):
#     return x * y

# # This function divides two numbers
# def divide(x, y):
#     return x / y

# num1 = int(input("Enter Number 1 : "))
# num2 = int(input("Enter Number 2 : "))

# print("Sum :", add(num1, num2))
# print("Difference :", subtract(num1, num2))
# print("Product :", multiply(num1, num2))
# print("Quotient :", divide(num1, num2))

#ACP
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = int(input("Enter Number of Terms :"))

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))

