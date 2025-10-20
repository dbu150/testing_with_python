# your code her
# prforme addition,substraction,multiplication,devision user input
num1=int(input("enter number 1"))
num2=int(input("enter numebr 2"))
oper=(input("enter the operation"))
match oper:
  case "+":
    sum=num1 +num2
    print(f"the sum of two number is {sum}")
  case "-":
    sub=num1-num2
    print(f"the sustraction of two number is {sub}")
  case "*":
    mul=num1*num2
    print(f"the multplication of two numbers is {mul}")
  case "/" :
    if num2!=0:
      div=num1/num2
      print(f"the division of two number is {div}")
  case _:

   print("display in valid opration")
  
