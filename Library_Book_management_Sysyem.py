# Library Book Management System

# load data 
book_list =[]

def load_data():
    try:

        with open("book_library.txt", "r") as file:
            for line in file:
                book_list.append(line.strip())
        return book_list

    except FileNotFoundError:
        print("Error. The file book_library.txt was not found.")

# display menu

def display_menu():
    print("\nHogwarts Librart Management Menu")
    print("1. View all books")
    print("2. Add a new book")
    print("3. Remove a book")
    print("4. Save books")
    print("5. Exit")

# View books

def view_books(book_list):
    print("\nBooks in the library:")
    for i in range(len(book_list)):
        print(f"{i+1}.{book_list[i]}")

# add books

def add_books(book_list):

    # enter a single book number 
    book = input("Enter the title of a new book: ").title().strip()

    if book in book_list:
        print("\nThe book already exist in the library.")
    else:
        book_list.append(book)

    print("\nBook added successfully.")

# remove a book

def remove_book(book_list):

    while True:

        # display a list of books
        view_books(book_list)

        # enter a number corresponding to the book

        try:
            remove = int(input("Enter the number of the book to remove: "))

            if remove <= 0 or remove > len(book_list):
                print("Please enter a valid number from the list.")
            else:
                removed_book = book_list[remove - 1]
                book_list.pop(remove - 1)
                print(f"Removed book: {removed_book} ")
                break

        except ValueError:
            print("Invalid input. Characters are not accepted.")

# save books 

def save_books(book_list):
    try:
        # write content of the list into book_library.txt

        if not book_list:
            print("The list does not have information. Please provide  a with library books.")
        
        else:
            with open("book_library.txt", "w") as file:
                        for book in book_list:
                            file.write(f"{book}\n")
            print("The books were saved successfully.")
    except FileNotFoundError:
        print("Error. The file you want to access does not exist.")
    

# main function

def main():

    option = 0

    while option != 5:
        try:
            display_menu()
            option = int(input("Option: "))

            if option == 1:
                book_list = load_data()
                view_books(book_list)
                print("")

            elif option == 2:
                add_books(book_list)
                print("")

            elif option == 3:
                remove_book(book_list)
                print("")

            elif option == 4:
                book_list = load_data()
                save_books(book_list)

            elif option == 5:
                print("Goodbye...")

            else:
                print("Invalid option. Please enter an option from the menu.")

        except ValueError:
            print("Error. Please enter a valid whole number. Characters are not accepted.")

main()





