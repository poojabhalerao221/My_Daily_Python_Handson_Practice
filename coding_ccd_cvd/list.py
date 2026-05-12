my_list=[10,20,30,40]
print(my_list)

#append===>To add the element at end in list
my_list.append(20)
print(my_list)
my_list.append([78,69,88])
print(my_list)


#insert===>add element at specific position
my_list.insert(0,101)
print(my_list)

#extend====>adding multiple elements
my_list.extend([4])
print(my_list)
my_list.extend([44,55,66])
print(my_list)



#remove===>remove specific value
my_list.remove([78,69,88])
print(my_list)

#pop===>removes last element by default and pop(index)
my_list.pop()
print(my_list)

my_list.pop(1)#index
print(my_list)

#clear

#index()===>to know the index of element
print(my_list.index(101))

#count===>Count occurrences
print(my_list.count(20))

#sort==>put in sequence
my_list.sort()
print(my_list)

#reverse==>does the sequence in reverse order
my_list.reverse()
print(my_list)


'''Create a list of 10 numbers and print only even numbers.
Find the sum of all elements in a list.
Find the largest and smallest number in a list.
Count how many times a given number appears in a list.
Reverse a list without using reverse().'''

#Create a list of 10 numbers and print only even numbers.
l=[1,2,3,4,5,6,7,8,9,10]
for i in l:
    if i%2==0:
        print(f"Even Numbers:{i}")
        
#Find the sum of all elements in a list.
s=0
for i in l:
    s=s+i
print(f"Sum of all elements is : {s}")


#Find the largest and smallest number in a list.
print("Maximum",max(l))
print("Minimum",min(l))

#Count how many times a given number appears in a list.
print("Appeared number ",l.count(1),"time")

        
'''Remove duplicate elements from a list.
Merge two lists and sort them.
Find the second largest number in a list.
Check if a list is a palindrome (same forward and backward).
Split a list into even list and odd list.'''

'''Rotate a list to the right by 1 position
👉 Example: [1,2,3,4] → [4,1,2,3]
Find common elements between two lists
👉 [1,2,3] and [2,3,4] → [2,3]
Find elements that are present in one list but not in another
Count positive, negative, and zero numbers separately
Replace all negative numbers with 0'''

'''Find the missing number from a list
👉 [1,2,4,5] → missing = 3
Move all zeros to the end
👉 [0,1,0,3,12] → [1,3,12,0,0]
Find pairs whose sum = given number
👉 [1,2,3,4,5], sum=6 → (1,5),(2,4)
Find the frequency of each element
👉 [1,2,2,3,3,3]
Flatten a nested list
👉 [1,[2,3],[4,5]] → [1,2,3,4,5]'''

'''Find the longest increasing subsequence (basic logic version)
Sort a list without using sort()
Find the first non-repeating element
Rotate list by k positions
Check if two lists are anagrams (same elements, different order)'''