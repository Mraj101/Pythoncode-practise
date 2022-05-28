class Library:
    def __init__(self,books):
        print("welcome to the central library")
        self.bookList=books
        print(self.bookList)
        self.books=books
    
    def showAvalilabeBooks(self):
       for index,avaBooks in enumerate(self.books):
           print(index+1,avaBooks)
    
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"you requested {bookName} book")
            self.books.remove(bookName)
            return True
        else:
             print("This book is not available")
             return False

    def returnBook(self,book):
        if book in self.bookList:
            print("thanks for returning")
            self.books.append(book)
        else:
            print("this is no the book you borrowed")
        
class Student:
    def reqBook(self):
        self.book=input("enter the book name to request: ")
        return self.book
    def returnBook(self):
        self.book=input("enter the name of the book you wanna return: ")
        return self.book

library=Library(["python notes","algorithm","networking","database"]   )
student=Student()
while(True): 
    choice=int(input("enter your choice: "))
    if choice==1:
        library.showAvalilabeBooks()
    elif choice==2:
        library.borrowBook(student.reqBook())
    elif choice==3:
        library.returnBook(student.returnBook())
