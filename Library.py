class Library():
    def __init__(self,list_of_books,Library_name):
        # creating a dictionary of all books keys
        self.lend_data = {}
        self.list_of_books = list_of_books
        self.library_name = Library_name

        # adding books to dictionary
        for books in self.list_of_books:
            # none means No author have lend this book
            self.lend_data[books] = None
 
    def display_books(self):
        for index,books in enumerate(self.list_of_books):
            print(f"{index+1}>  {books}")

    def lend_book(self,book,author):
        if book in self.list_of_books:
            if self.lend_data[book] is None:
                self.lend_data[book] = author
            else:
                print(f"Sorry This book is lend by {self.lend_data[book]}")
        else:
            print("You have written wrong book name")

    def return_book(self,book,author):
        if book in self.list_of_books:
            if self.lend_data[book] is not None:
                self.lend_data.pop(book)
            else:
                print("Sorry but This book is not Lend")
        else:
            print("You have written wrong book name")

    def add_book(self,book_name):
        self.list_of_books.append(book_name)
        self.lend_data[book_name] = None

    def delete_book(self,book_name):
        self.list_of_books.remove(book_name)
        self.lend_data.pop(book_name)

def main():
    # By deafault variables
    list_books = ['Cookbook', 'Learn C# in 100 pages', 'A day of Instien', 'Warren\'s Hasting story', 'Hello World with Coding', 'Sherlock Holmes', 'Chacha_chaudhary', 'Rich Dad and Poor Dad']
    Library_name = 'KRISHNA'
    secret_key = 9876543210

    Harry = Library(list_books,Library_name)

    print(f"Welecome To {Harry.library_name} library\n\nq for exit \nDisplay Book Using 'd' and add lend book using 'l' and Return a Book using 'r' \nAdd Book Using 'a' and Delete Book using 'del' \n ")

    Exit = False
    while (Exit is not True):
        _input = input("Option: ")
        print("\n")
        
        if _input == "q":
            Exit = True

        elif _input == "d":
            Harry.display_books()

        elif _input == "l":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to lend:")
            print("\n Book Lend \n")
            Harry.lend_book(_input3,_input2)

        elif _input == "a":
            _input2 = input("Book name:")
            Harry.add_book(_input2)

        elif _input == "del":
            _input_secret = int(input("Write the secret key to delete:"))
            if (_input_secret == secret_key):
                _input2 = input("Book Which you want to delete:")
                Harry.delete_book(_input2)
            else:
                print("Sorry We can't Delete the Book")

        elif _input == "r":
            _input2 = input("What is your name:")
            _input3 = input("Which Book Do you want to return:")
            Harry.return_book(_input3,_input2)
        
        else:
            print('Wrong Option selected')
            continue

if __name__ == "__main__":
    main()