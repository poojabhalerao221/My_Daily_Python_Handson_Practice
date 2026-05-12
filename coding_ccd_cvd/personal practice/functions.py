city=['pune','mumbai']

def print_len(l):
    d=len(l)
    return d
s=print_len(city)
print(s)

def ele_list(l):
    for i in l:
        print(i,end=" ")
    
ele_list(city)

def fact(n):
    f=1
    for j in range(1,n+1):
        f*=j
    print(f)
fact(6)

def con_usd(n):
    print("USD value:",n)
    n=n*83
    print(n,"USD =",n,"INR")
    
con_usd(12)
    
    
def str_show():
    in_str=int(input("Enter the Number:"))
    if in_str%2==0:
        print(in_str,"is Even")
    else:
        print(in_str,"is Odd")
        
str_show()
    