print("Conditional Logic Exercises")
# Practice if/elif/else statements here.
a=int(input("enter the number "))
b=int(input("enter the number "))
c=int(input("enter the number"))
if a > b:
  if a > c:
    print("the lager number is" ,a)
  else:
    print("the lager number is" ,c)
elif b > c:
  print("the lager number is" ,b)
else:
  print("the lager number is "  ,c) 
