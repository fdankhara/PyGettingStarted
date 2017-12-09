def add(num1, num2):
    ans = num1 + num2
    return ans

def sub(num1, num2):
    ans = num1 - num2
    return ans

def mlt(num1, num2):
    ans = num1 * num2
    return ans

def div(num1, num2):
    ans = num1 / num2;
    return ans;

print("Welcome to my two number calculator")
num1 = int(input("Enter number 1:"))
operation = input("Enter operation:")
num2 = int(input("Enter number 2:"))

#print(add(num1, num2))
if(operation == "+"):
    print(add(num1, num2))
elif(operation == "-"):
    print(sub(num1, num2))
elif(operation == "*"):
    print(mlt(num1, num2))
elif(operation == "/"):
    print(div(num1, num2))
