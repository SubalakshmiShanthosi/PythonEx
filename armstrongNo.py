#Check if the given number is armstrong number or not 
import math
def armstrongNumber(number):
     
     sum=0
     copyNumber=number
     while number>0:
       
         digit=number % 10
         sum+=math.trunc(digit**3)
         number=math.trunc(number / 10)
      
     if(copyNumber==sum):
            return "Given Number "+str(copyNumber)+" is Armstrong Number"
     else:
            return "Given Number "+str(copyNumber)+" is not Armstrong Number"


#Get number from user
num=int(input("Enter a number:"))
print("Checking if the given number is Armstrong number:")
print(armstrongNumber(num))
