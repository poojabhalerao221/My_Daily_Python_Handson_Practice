#square
'''
n=5
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()'''
    
'''n=4
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()'''
'''    
n=6
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()'''
'''  
n=4
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()   '''
    
name=input("Enter the user:")
res=''
for i,j in  enumerate(name):
    if i%2==1:
        res+=str(i)
        print(res)
    
        
 
    
    
