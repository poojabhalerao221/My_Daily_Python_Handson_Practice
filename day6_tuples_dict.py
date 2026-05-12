my_tup=(1,"Hello",3.14,True)
print(my_tup)

my_color=(255,255,255)
print(my_color)


student={
    "Name":"Pooja",
    "age":12,
    "grade":"7th",
    "Subject":"Math"
}

print(student)


empty_dict={}

empty_dict["city"]="Jaipur"
print(empty_dict)
empty_dict["state"]="Rajasthan"
print(empty_dict)

empty_dict["state"]="R"
print(empty_dict)

print("Name:",student["Name"])
print("Age:",student['age'])
print("Grade:",student['grade'])
print("Subject:",student['Subject'])

age=student.get('age')
print(age)

hobby=student.get("hobby","Not Available")
print(hobby)

address=student.get("address")
print(address)


#Task

book_info={
    "Title":"The Blue Umbrella",
    "Author":"Riskin Bond",
    "Year":1974,
    "Genre":"Fiction"
}


book_info['rating']=4.5
book_info['Year']=2026

book=book_info.get('publisher',"Unknown")

print(book_info)
print(book)