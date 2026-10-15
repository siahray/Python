name = "Siah"
age = 21


print(f"My name is {name}, and I am {age} years old")


print("_________________________________________________")
print("Calculator")

print("Choose an Operation: ")
print("A. Addition")
print("B. Subtraction")
print("C. Multiplication")
print("D. Division")
print("Others:")
print("E. Multiplication Table")

user_choice = input("Enter the letter of your Choice: ")

case user_choice
if user_choice == 'A':
    num1 = input("Input a number: ")
    num2 = input("input another number")

    sum = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum}")

elif user_choice == 'B':
    num1 = input("Input a number: ")
    num2 = input("input another number")

    diff = num1 - num2
    print(f"The difference of {num1} and {num2} is {sum}")  


elif user_choice == 'C':
    num1 = input("Input a number: ")
    num2 = input("input another number")

    prod = num1 * num2
    print(f"The product of {num1} and {num2} is {sum}")  

elif user_choice == 'D':
    num1 = input("Input a number: ")
    num2 = input("input another number")

    quo = num1 * num2
    print(f"The quotient of {num1} and {num2} is {sum}")  

elif user_choice == 'E':
    num = input("Input a number: ")
    for i in range(10):
        prod = num * i
        print(prod) 
        









