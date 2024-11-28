def tempconversion(option, x):
    if option == 2:
        name="fahrenhiet"
        ans = ((x - 32) * (5/9))
    elif option == 1:
        name="celsius"
        ans = ((x * 9/5) + 32)
    elif option == 3: 
        name="kelvin"
        ans =str(x + 273)+name
       
    elif option == 4:
        name="celsius"
        ans  = str(x - 273)+name
       
  
    return ans 

  
while True:
   
    opt = int(input('This is your temp converter. Press 1 to convert from F to C or 2 to convert from C to F and press 3 to convert C to K and 4 to convert K to C: '))
    f= int(float(input('Enter the values: ')))
    print(tempconversion(opt,f))
   
# print((f - 32) * (5/9)) 
# i also want to add units to the temperature values
