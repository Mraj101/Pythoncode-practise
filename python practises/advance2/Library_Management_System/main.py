class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("\n\t_____Books present in this Library are_____")
        for index, book in enumerate(self.books):
            print(f"{index+1}:-  {book}")

    def borrowBook(self, bookName):
        if bookName in self.books:
            print(
                f"You have been issued{bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book has already been issued to someone,\n\t Please wait until the book is returned ")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning the book. Have a great day ahead")


class Student:
        # def __init__(self):
        #     self.book=

        def requestBook(self):
            self.book = input("Enter the name of the book you want to borrow: ")
            return self.book

        def returnBook(self):
            self.book=input("Enter the name of the book you want to return: ")
            return self.book




if __name__ == "__main__":
    centralLibrary = Library(
        ["Algorithm", "clrs", "Django", "PythonBook", "PythonNotes"])
    
    student=Student()
    while(True):
        welcomeMsg='''\n\t====Welcome to Central Library====
        please choose and option:
        1. Listing all the books
        2. Request a book
        3. Return a book
        4. Exit the Library\n
        '''
        print(welcomeMsg)
        a=int(input("\nEnter a choice: "))
        if a==1:
            centralLibrary.displayAvailableBooks()
        elif a == 2:
            centralLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("\nThanks for choosing CentralLibary\n  Have a great day ahead!!!!!\n")
            exit()
        else:
            print("Invalid Choice")
        
