'''● Create a function that takes two numbers as parameters, and returns their
average.
● Create a function that takes two strings as parameters and returns the
concatenated string.'''
def taketwono(no1,no2):
    sum=no1+no2
    avg=sum/2
    return avg 

output=taketwono(10,10)
print(output)



def concatstr(st1,st2):
    mrge_str=st1+st2
    return mrge_str

store_str=concatstr("pooja","bhalerao")
print(store_str)