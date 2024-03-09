def add (x,y):
    return x+y

def subrtract (x,y):
    return x-y

def multiply (x,y):
    return x,y

def divide (x,y):
    return x,y

print("Select desired operation what you want to perform: ")
print("Press 1 for addtion-- ")
print("Press 2 for subtraction-- ")
print("Press 3 for multiplication-- ")
print("Press 4 for division-- ")

while True:
    choice = input("Enter choice according to desired operation(1 OR 2 OR 3 OR 4):")

    if choice in('1', '2', '3','4'):
        try:
            num1 = float(input("Enter your first desired number : "))
            num2 = float(input("Enter your second desired number: "))

        except ValueError:
            print('Invalid input. Please enter a number: ')
            continue

        if choice == '1' :
            print(num1, "+", num2, "=", (num1+num2))
            print("So the value of your desired no. is: ",num1+num2)

        if choice == '2':
            print(num1, "-", num2, "=", (num1-num2))
            print("So the value of your desired no. is: ",num1-num2)


        if choice == '3': 
            print(num1, "*", num2, "=", (num1*num2))
            print("So the value of your desired no. is: ",num1*num2)


        if choice == '4':
            print(num1, "/", num2, "=", (num1/num2))
            print("So the value of your desired no. is: ",num1/num2)
  

