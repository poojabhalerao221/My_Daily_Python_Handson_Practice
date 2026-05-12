"""Access the third element of a list
List Length: Print the total number of items
Check if the list is empty"""




numbers = [10, 20, 30, 40, 50]
print("Third element of list",numbers[2])
print("Total number of items",len(numbers))
if len(numbers)==0:
    print("Empty")
else:
    print("not empty")
    
    
#2.list manipulation
"""Change Element: Change the second element of a list to 200 and print the updated list.
Append Element: Add 600 o the end of a list and print the new list.
Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
Remove Element (by value): Remove 600 from the list and print the list.
Remove Element (by index): Remove the element at index 0 from the list print the list."""

Initial_List= [100, 50, 400, 500]
Initial_List[1]=200
print(Initial_List)

Initial_List.append(600)
print(Initial_List)

Initial_List.insert(2,300)
print(Initial_List)

Initial_List.remove(600)    #removed by value
print(Initial_List)

Initial_List.pop(0)         #removed by index
print(Initial_List)


"""Calculate the total sum of all integers in a list and find the arithmetic mean (average)"""
Numbers= [10, 20, 30, 40, 50]
total_sum=sum(Numbers)
avg=total_sum/len(Numbers)
print("Sum of numbers:",total_sum)
print("Average of numbers:",avg)


"""Identify the largest and smallest numerical values within a provided list."""
Data= [45, 12, 89, 2, 67]
maximum_num=max(Data)
Minimum_num=min(Data)
print("Maximum",maximum_num)
print("Minimum num:",Minimum_num)


'''Multiply every number in a list together to find the total product.'''
Factors= [2, 3, 5, 7]
prod=1
for i in Factors:
    prod=prod*i
print(prod)

""" Given a list of integers, iterate through the items and count how many are even and how many are odd."""    
Numbers= [10, 21, 4, 45, 66, 93, 11]
e_c=0
o_c=0
for i in Numbers:
    if i%2==0:
        e_c+=1
    else:
        o_c+=1
        
print("Even num:",e_c)
print("Odd num",o_c)


"""Take a list and reverse the order of its elements."""
List= [100, 200, 300, 400, 500]
print(List[::-1])


"""Sort a list of numbers in ascending order (lowest to highest)."""
Unsorted= [56, 12, 89, 3, 22]
Unsorted.sort()
print(Unsorted)

"""Merge two separate lists into a single, unified list."""
ListA= ["Physics", "Chemistry"]
ListB= ["Maths", "Biology"]
print(ListA+ListB)

"""Given a list, extract a “slice” containing the middle three elements."""
List= [10, 20, 30, 40, 50, 60, 70]
print(List[2:5])


"""Write a script to swap the positions of two elements in a list based on their indices."""
List=[23, 65, 19, 90]
ind1,ind2=0,2
List[ind1],List[ind2]=List[ind2],List[ind1]
print(List)

""" Given a “list of lists,” access a specific item hidden inside the inner list."""
Nested_List= [[1, 2], [3, 4, 5], [6, 7]]
print(Nested_List[1][2])

"""Write a check to see if a certain value exists within a list and print a message based on the result."""
Inventory=["Laptop", "Mouse", "Monitor", "Keyboard"]
Target= 'Tablet'
if Target in Inventory:
    print("True")
else:
    print("No")
    
    
"""In a list of strings, identify which string has the most characters."""
Words= ["PHP", "Exercises", "Backend", "Python"]
long=max(Words,key=len)
print(long)

"""Given a list of numbers, create a new list where each number is replaced by its square (n2) using a single line of code."""
List= [1, 2, 3, 4, 5]
print([i*i for i in List])

""" Find out how many times a specific value appears in a list."""
List= [10, 20, 30, 10, 40, 10, 50]
Target= 10
count_occ=List.count(Target)
print(count_occ)

"""Count each element occured how many times"""
for i in List:
    cont_occ=List.count(i)
    print(i ,"Occurs",cont_occ,"Times")
    
    
"""Delete every instance of a specific value from a list."""
List= [5, 20, 15, 20, 25, 50, 20]
Itemtoremove= 20
l=[i for i in List if i!=Itemtoremove]
print(l)


""" Take a list of strings that contains empty entries ("") and remove them to keep only the valid text."""
List= ["Mike", "", "Emma", "Kelly", "", "Brad"]
l=list(filter(None,List))
print(l)


""" Given a list of integers, use list comprehension to create a new list that contains only the even numbers from the original list.

Exercise Purpose: This is the “Filter” part of the Map-F"""
List= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Output: Even Numbers: [2, 4, 6, 8, 10]
l=[i for i in List if i%2==0]
print(l)

"""Concate two lists"""
List1= ["Py", "is", "awes"]
List2= ["thon", " ", "ome"]
res=[i+j for i,j in zip(List1,List2)]
print(res)

"""Iterate both athe list at once"""
List1= [10, 20, 30]
List2= [100, 200, 300]
for i,j in zip(List1,List2):    
    print(i,j)
    
""" Find a specific item in a list and insert a new item immediately after it."""
List= [10, 20, 30, 40, 50]
Target= 30
NewItem= 35

l=List.index(Target)
print(l)
List.insert(l+1,NewItem)
print(List)

"""Find the first occurrence of a specific value in a list and replace it with a new value."""
List= [5, 10, 15, 20, 25]
Find= 20
Replacewith= 200
if Find in List:
    l=List.index(Find)
    List[l]=Replacewith
    print(List)
    