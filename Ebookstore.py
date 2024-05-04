import sqlite3

# Function to create the database and table
def create_database():
    # Connect to the database
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    # Create table if not exists
    cursor.execute('''CREATE TABLE IF NOT EXISTS book
                 (id INTEGER PRIMARY KEY,
                 title TEXT,
                 author TEXT,
                 qty INTEGER)''')

    # Insert initial data
    initial_books = [
        (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
        (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
        (3003, 'The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 25),
        (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
        (3005, 'Alice in Wonderland', 'Lewis Carroll', 12),
        (3006, 'The Golden Compass', 'Philip Pullman', 15),
        (3007, 'The Lightning Thief', 'Rick Riordian', 7),
        (3008, 'Neverwhere', 'Neil Gaiman', 20),
        (3009, 'The Magicians', 'Lev Grossman', 35),
        (3010, 'Shadow and Bone', 'Leigh Bardugo', 10)
    ]

    # Insert initial books, handling conflicts if book ID already exists
    for book in initial_books:
        try:
            cursor.execute('INSERT INTO book VALUES (?, ?, ?, ?)', book)
        except sqlite3.IntegrityError:
            # Book ID already exists, skip insertion
            pass

    # Commit changes and close connection
    db.commit()
    db.close()

# Function to add a new book
def add_book():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    title = input("Enter book title: ")
    author = input("Enter author name: ")
    qty = int(input("Enter quantity of books: "))

    cursor.execute("INSERT INTO book (title, author, qty) VALUES (?, ?, ?)", (title, author, qty))
    db.commit()

    print("Book added successfully!")

    db.close()

# Function to update book information
def update_book():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    book_id = int(input("Enter book ID to update: "))
    qty = int(input("Enter new quantity: "))

    cursor.execute("UPDATE book SET qty = ? WHERE id = ?", (qty, book_id))
    db.commit()

    print("Book information updated successfully!")

    db.close()

# Function to delete a book
def delete_book():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    book_id = int(input("Enter book ID to delete: "))

    cursor.execute("DELETE FROM book WHERE id = ?", (book_id,))
    db.commit()

    print("Book deleted successfully!")

    db.close()

# Function to search for a book
def search_books():
    db = sqlite3.connect('ebookstore.db')
    cursor = db.cursor()

    search_book = input("Enter title or author to search: ")
    cursor.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ?", ('%' + search_book + '%', '%' + search_book + '%'))
    books = cursor.fetchall()

    if len(books) == 0:
        print("No matching books found.")
    else:
        print("Matching Books:")
        for book in books:
            print(book)

    db.close()

# Main function to display menu and handle user input
def main():
    create_database()

    while True:
        print("\nMenu:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
