class Library:
    def __init__(self):
        self.books={
            (1,"The jungle book",25),
            (2,"Avengers",20),
            (3,"The hulk",10),
            (4,"power rangers",5),
            (5,"barbie",12)
        }
        self.collect_book_list=[]
        
        def view_books(self):
            print("Available Books:\n")
            for book_no,info in self.books.items():
                book_avail,name=info
                print(f"Book number:{book_avail} & Book name:{name}")
            print()
            
class LibraryManagementSystem(Library):
    def burrow_book(self):
        book_u_want=input("Enter the book from the list:")
        book_no=int(input("Enter the book number from above list:"))
        if book_no in self.books:
            book_u_want,book_avail=self.books[book_no]
            if book_avail>0:
                self.books[book_no]=(book_u_want,book_avail-1)
                
                lib_pass={
                 "book_u_want":book_u_want,   
                 "book_no":book_no,
                 
                }
                self.collect_book_list.append(lib_pass)
                print("Took the book successfully")
            else:
                print("No such book available")
        else:
            print("Book not found")