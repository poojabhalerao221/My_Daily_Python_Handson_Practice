#sum and avg of all num

num=[12,56,48,66,94,75]
sum=0
for i in num:
    sum=sum+i
    avg=sum/6
print("Sum",sum,"Avg",avg)


#max min
scores = [55, 89, 32, 98, 45]
print(max(scores))
print(min(scores))

#list modification
fruits = ['apple', 'banana', 'cherry']
fruits[1]='Orange'
print(fruits)
fruits.append('Mango')
print(fruits)
fruits.insert(1,'grapes')
print(fruits)


#access 5
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][1])

#check for the item is present "tea"
beverages = ["coffee", "juice", "milk", "tea"]
if "tea" in beverages:
    print("yes")
else :
    print("no")
    
    
#remove the duplicate vales
duplicates = [1, 2, 3, 2, 1, 4, 5, 4, 4]
store=[]
[store.append(i) for i in duplicates if i not in store]
print(store)

#filter odd and even
numbers = [12, 5, 8, 19, 22, 17, 30]
[ i for i in numbers if i%2==0 ]
print(i)