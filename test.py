print("1-add")
print("2-substract")
print("3-multiply")
print("4-multiply")
option = int(input("choose an operator:"))

if(option in [1,2,3,4]):
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    
if(option==1):
    result = num1 + num2
elif(option==2):
    result = num1 - num2
elif(option==3):
    result = num1 * num2
elif(option==5):
    print("invalid operation")
print("the result of of the operator is {}".format(result))