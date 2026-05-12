
def calculate_total(m1,m2,m3):
    total1=m1+m2+m3
    #print("Total Marks",total1)
    return total1
def calculate_avg(total):
    total=total/3
    return total
def assign_grade(avg):
    if avg>=90:
        return ("A")
    elif avg>=70:
        return ("B")
    elif avg>=50:
        return ("C")
    else:
        return ("fail")
def show_report_card(name,total,avg,grade):
    print("=======Report Card======")
    print(f"Name of Student:{name}")
    print(f"Total Marks:{total}")
    print(f"Average:{avg}")
    print(f"Grade:{grade}")
    
name=input('Enter the name:')
m1=int(input("Enter m1:"))
m2=int(input("Enter m2:"))
m3=int(input("Enter m3:"))
total1=m1+m2+m3
avg=total1/3
grade=assign_grade(avg)

show_report_card(name,total1,avg,grade)