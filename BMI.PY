def bodymassindex(kilograms, metres):
    ans =kilograms/(metres^2)
    return ans



 
while True:
     print("THIS IS YOUR BODY MASS INDEX CALCULATOR, ALL YOU NEED IS YOUR MASS AND HEIGHT")
     bmi=int(input("TO CONTINUE PRESS 1 else PRESS 2 TO CANCEL?:"))
     if bmi==1:
      KG=int(input("Enter the mass in kilograms:"))
      met=int(input("Enter the Height in metres:"))
      print(bodymassindex(KG,met))
     elif bmi != 1 and bmi != 2:
        print("TRY AGAIN.")
     elif bmi==2:
        print("Bye and thank you.")
        break
     
        


              

    
