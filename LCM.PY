from math import gcd
def lcm(x, y):
 product = x * y
 
 gcd_result = gcd(x, y)
 lcm_result = product // gcd_result
 return lcm_result

from math import gcd
def lcm2(x,y,z):
 product = (x*y*z) 
 gcd2_result = gcd(x, y, z)
 lcm2_result = product // gcd2_result
 return lcm2_result
      

  
BIS=int(input("HOW MANY NUMBERS ARE IN THE DATA:"))
if BIS==1:
    print("TRY AGAIN!!!")
if BIS==2:
    Hey=int(input(" ENTER FIRST NUMBER:"))
    hey=int(input(" ENTER SECOND NUMBER:"))
    
    print(lcm(Hey, hey))

if BIS==3:
    SHey=int(input(" ENTER FIRST NUMBER:"))
    Sey=int(input(" ENTER SECOND NUMBER:"))
    THE=int(input(" ENTER THIRD NUMBER:"))
    
    print(lcm2(SHey, Sey, THE))


 

