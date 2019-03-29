# Sum of first 1... limit natural numbers 
def sumOfNNos(limit):
       total=0
       for i in range (1,limit+1):
            total+=i

       return total

#Get input from user
limit=int(input("Enter the value of limit:"))
ans=sumOfNNos(limit)
print("Sum of first "+str(limit)+" numbers is:"+str(ans))


