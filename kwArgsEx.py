
def studentDetails(name,**kwargs):
 
       print("Student name is:"+name)
       print("Keyword Arguments are : ")
       for key in kwargs:
            print(key+":"+ str(kwargs[key]))


studentDetails(name='Subalakshmi', Age=24, Department='CSE')

