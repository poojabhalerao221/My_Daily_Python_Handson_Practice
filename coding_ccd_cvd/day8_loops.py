#numbers=[1,2,3,4,5,6]
#for i in numbers:
    #if i%2==0:
        #print(f"{i} is even number")
        
"""student=['pooja','janhavi']
subjects=['Coding','Robotics']

for i in student:
    for j in subjects:
        print(f"{i} studying {j}")
        """
        
#looping through list using len
animals=['Elephant','Tiger','Lion']
print(len(animals))

#for  index in range(len(animals)):
#    print(f"{index} :{animals[index]}")


#Looping  through  the list in reverse order

#colors=["Red","Blue","Yellow"]
#for i in range(len(colors)-1,-1,-1):
 #   print(colors[i])
 
 
 #Task 1
#Loop  through a list 10-20
for i in range(10,21):
    #print(f"The numbers are {i} ")
    if i %2 !=0:
        print(f"{i} is Odd")
        
        
#Task 2
for i in range(1,6):
    for j in range(len(i)-1,-1):
        print("*")

