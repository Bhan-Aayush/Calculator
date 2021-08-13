num1 = float(input("Enter a number: "))

op = input("Enter a number: ")

num2 = float(input("Enter another number: "))

if op == "+":
  print(num1 + num2)

elif op == "-":
  print(num1 - num2)
  
 elif op == "/":
  print(num1 / num2)

elif op == "*":
  print(num1 * num2)
  
#use an int function(only for whole numbers!)
result = int(num1) + int(num2)
print(result)

#For decimal numbers we only use float
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = float(num1) + float(num2)
print(result)
