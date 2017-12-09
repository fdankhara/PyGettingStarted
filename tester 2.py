def sub(num1, num2):
    ans = num1 - num2
    return ans

num1 = int(input("Enter number 1:"))
operation = input("Enter operation:")
num2 = int(input("Enter Number 2:"))

answer=0
if(operation == "-"):
    answer = sub(num1, num2)

print(answer)
