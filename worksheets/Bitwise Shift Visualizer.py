"""
Input an integer and number of shift positions.

Show results of left shift and right shift.

Print the binary form before and after.
"""
integer=int(input("enter the integer number")) #this will be shifted number

snumber =int(input("ente shift number"))
result1 =integer << snumber #caculate the left shift number
print("this left shift=",result1)
result2= integer >> snumber #calculate the right shiift
print("this right shift=",result2)
# binart before 
binary_before=bin(integer)[2:] #before the shift of the number

print( "this is the binary of before left and right shift the integer number is ",binary_before)
#the binary number of after the shift
print("the binary of left shift integer=",bin(result1)[2:])
print("the binary of right shift integer=",bin(result2)[2:])


