#Task1:Print the variable value and its type(variablename)

#1.string(text data)
school="Green Valley School"
print("String is:",school)
print(type(school))

#2.Integer(Whole numbers)
num=12
print("Number is:",num)
print(type(num))

#3.Float(Decimal numbers)
price=10.32
print("Flaoting number is:",price)
print(type(price))


#4.Boolean(True or False)
correct=True
print("Boolean Value:",correct)
print(type(correct))


#write the code for the following:
'''1. Ask your name
2.asks 3 subjects
3.calculate the average 
4.print result'''


name=input("Enter the name:")
s1=int(input("Enter the marks of subject1:"))
s2=int(input("Enter the marks of subject2:"))
s3=int(input("Enter the marks of subject3:"))
add=s1+s2+s3
average=add/3
print("Result:",name,"has scored",average,"subject1 score:",s1,"subject2 score:",s2,"Subject3 score:",s3)


