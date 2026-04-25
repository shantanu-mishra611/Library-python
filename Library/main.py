def login(user, password):
    global a
    with open("Library/directory.txt", "r") as f:
        users_db = {}
        for line in f:  
            if ":" in line:
                u, p = line.strip().split(":")
                users_db[u] = p
    if user in users_db and users_db[user] == password:
        print("Login successful!")
        a = 1
    else:
        print("Invalid username or password.")
        a = 0



def register(user, password):
    with open("Library/directory.txt", "a") as f:
        f.write(f"{user}:{password}\n")
    print(f"User {user} registered successfully!")



mode = input('Do you want to login or register? ').lower()
a = 0

if mode == 'login':
    user = input('User id: ')
    password = input('password: ')
    login(user, password)
    
    
elif mode == 'register':
    user = input('User id: ')
    password = input('password: ')
    register(user, password)
    

else:
    print("Invalid option. Please type 'login' or 'register'.")
    

def check_book_availability(Book):
    with open("Library/book_list.txt", "r") as f:
        content = f.read()
        book_list = [item.strip().lower() for item in content.split(",")]
    if Book in book_list:
        print('We have the book')
    else:
        print('We dont have the book at this moment.')
        choice = input('Do you want to add it to the library? (yes/no) ').strip().lower()
        if choice == 'yes':
            with open("Library/book_list.txt", "a") as f:
                f.write(f", {Book}")
            print(f'The book "{Book}" has been added to the library.')
    

def borrow_book(user, book_name):
    
    with open("Library/book_list.txt", "r") as f:
        content = f.read()
        library_books = [b.strip().lower() for b in content.split(",")]

    if book_name in library_books:
        with open("Library/borrowed_log.txt", "a") as f:
            f.write(f"{user}:{book_name}\n")
        
        library_books.remove(book_name)
        with open("Library/book_list.txt", "w") as f:
            f.write(", ".join(library_books))
            
        print(f"Success! You have borrowed '{book_name}'.")
    else:
        print("Sorry, that book is not available.")
def return_book(user, book_name):
    with open("Library/borrowed_log.txt", "r") as f:
        borrowed_entries = f.readlines()
        
    with open("Library/borrowed_log.txt", "w") as f:
        for entry in borrowed_entries:
            if entry.strip() != f"{user}:{book_name}":
                f.write(entry)
        
    with open("Library/book_list.txt", "a") as f:
        f.write(f", {book_name}")
        
    print(f"Success! You have returned '{book_name}'.")

if a == 1:

    action = input("Do you want to 1.check availability, 2.borrow, 3.return a book? ").strip().lower()
    if action == 'check availability':
        Book = input('Enter the book name: ').strip().lower()
        check_book_availability(Book)
    elif action == 'borrow':
        user = input('User id: ')
        book_name = input('Enter the book name to borrow: ').strip().lower()
        borrow_book(user, book_name)
    elif action == 'return':
        user = input('User id: ')
        book_name = input('Enter the book name to return: ').strip().lower()
        return_book(user, book_name)
    else:
        print("Invalid action. Please choose 'check availability', 'borrow', or 'return'.")

else:
    pass
