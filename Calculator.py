#Function to add two numbers
def add (x,y): 
    return x+7

#Function to subtract two numbers
def subtract (x,y):
    return x-y

#Function to multiply two numbers
def multiply (x,y):
    return x*y

#Function to divide two numbers
def divide (x,y):
    return x/y

while True:
    print("Options")
    print("Enter'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter'multiply' for multiplication")
    print("Enter'divide' for division")

    user_input=input(": ")

    if user_input== "quit":
        break
    elif user_input in ("add","subtract","multiply","divide"):
        num1=float(input("Enter first number: "))
        num2=float(input("Enter second number: "))

        if user_input=="add":
            print ("Result:",add(num1,num2))
        elif user_input=="subtract":  
            print ("Result:",subtract(num1,num2))
        elif user_input=="multiply":  
            print ("Result:",multiply(num1,num2))
        elif user_input=="divide":  
            print ("Result:",divide(num1,num2))
    else:
        print("Invalid Input") 





    




