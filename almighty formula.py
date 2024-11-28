import math
def alm(a, b, c):
    determinant = (b ** 2) - ( 4 * a * c)
    result=(-b + math.sqrt(determinant))/ (2 * a )
    result1 = (-b - (determinant) ** 0.5 )/ (2 * a ) 
    return result, result1


num1=int(input(" ENTER A:"))
if num1==0:
    print("TRY AGAIN!!!")
    
    
else:

 num2=int(input(" ENTER B:"))
 num3=int(input(" ENTER C:"))
 print((alm(num1, num2, num3)))