print("Enter a number to check if it is")
print("--------NUMBER -----------------")
print("1. Positive number")
print("2. Negative number")
print("3. Zero")
number=int(input("Enter a number to check it's type: "))
if number > 0 :
      print("Given number "+str(number)+" is positive");
elif number < 0: 
      print("Given number "+str(number)+" is negative");
else:
      print("Given number "+str(number)+" is zero");

