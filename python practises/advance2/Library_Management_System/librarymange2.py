class Library:
    def __init__(self, listofBooks):
        self.books = listofBooks

    def availableBooks(self):
        print("Available Books are:\n")
        for index, book in enumerate(self.books):
            print((index+1), ":", book)

    def borrowBook(self,bookName):
        if bookName in self.books:
            print("\nYou have issued the book,\please return it before 30 days\n")
            print(f"you have entered the name of this book:{bookName}\nplease return it before 30 days")
            self.books.remove(bookName)
            return True
        elif bookName!=self.books:
            print(f"There is no such book in the Library called {bookName}")
        else:
            print("sorry The book is already issued")
            return False

    def returnBook(self, book):
        print("Thanks for returning the book,\n have a great day\n")
        if book==self.books:
          self.books.append(book)
        else:
            print(f"You did not issue the book named {book}")


class Student:
    def reqBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book
    
    def returnBook(self):
        self.book=input("Enter the book name you want to return: ")
        return self.book

if __name__ == "__main__":
    centralLibary = Library(["Algorithm", "java", "python", "Notes", "sql"])
    student=Student()
    while(True):
        welcomemsg=''' \t===Welcome To central Library===
        press 1 for watching the availability of the book
        press 2 for requesting a book from the Library
        press 3 for returning the issued book from the Library
        press 4 to exit the Library'''
        print(welcomemsg)
        a=int(input("Enter your choice : "))
        if a==1:
            centralLibary.availableBooks()
        elif a==2:
            centralLibary.borrowBook(student.reqBook())
        elif a==3:
            centralLibary.returnBook(student.returnBook())
        elif a==4:
             print("Thanks for coming , visit again")
             exit()
        else:
            print("Invalid choice")