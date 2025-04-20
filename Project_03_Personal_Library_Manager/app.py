def add_book():
    book_title = input("Enter the book title: ")
    book_author = input("Enter the book author: ")
    book_year = input("Enter the year of publication: ")
    book_genre = input("Enter the genre of the book: ")
    book_readed = input("Have you read this book? (yes/no): ").lower()
    
    bookInfo = {
        "title": book_title,
        "author": book_author,
        "year": book_year,
        "genre": book_genre,
        "readed": "Read" if book_readed == "yes" else "Unread"
    }

    with open("books.txt", "a") as file:
        file.write(f"{bookInfo['title']},{bookInfo['author']},{bookInfo['year']},{bookInfo['genre']},{bookInfo['readed']}\n")
    
    print(f"✅ Book '{book_title}' by {book_author} added successfully!")

def remove_book():
    remove_book_title = input("Enter the title of the book to remove: ")

    try:
        with open("books.txt", "r") as file:
            lines = file.readlines()

        with open("books.txt", "w") as file:
            removed = False
            for line in lines:
                if not line.lower().startswith(remove_book_title.lower()):
                    file.write(line)
                else:
                    removed = True

        if removed:
            print(f"✅ Book '{remove_book_title}' removed successfully.")
        else:
            print(f"❌ Book '{remove_book_title}' not found in the list.")

    except FileNotFoundError:
        print("⚠️ books.txt file not found.")

def search_book():
    try:
        with open("books.txt", "r") as file:
            lines = file.readlines()

        print("Search by:\n1. Title\n2. Author")
        search_choice = input("Enter your choice: ")

        keyword = input("Enter the search term: ").lower()
        matches = []

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) < 5:
                continue
            title, author = parts[0].lower(), parts[1].lower()

            if (search_choice == "1" and keyword in title) or (search_choice == "2" and keyword in author):
                matches.append(line.strip())

        if matches:
            print("\nMatching Books:")
            for i, match in enumerate(matches, 1):
                print(f"{i}. {match.replace(',', ' - ')}")
        else:
            print("❌ No matching books found.")

    except FileNotFoundError:
        print("⚠️ books.txt file not found.")

def display_all_books():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        if books:
            print("\n📚 Your Library:")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book.strip().replace(',', ' - ')}")
        else:
            print("Your library is empty.")
    except FileNotFoundError:
        print("⚠️ books.txt file not found.")

def display_statistics():
    try:
        with open("books.txt", "r") as file:
            books = file.readlines()

        total = len(books)
        read = sum(1 for book in books if "read" in book.lower())

        if total > 0:
            percentage = (read / total) * 100
            print(f"📊 Total books: {total}")
            print(f"📖 Percentage read: {percentage:.1f}%")
        else:
            print("No books in the library to show stats.")

    except FileNotFoundError:
        print("⚠️ books.txt file not found.")

# Main Program Loop
while True:
    print("\nWelcome to your Personal Library Manager!  ")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        add_book()
    elif option == "2":
        remove_book()
    elif option == "3":
        search_book()
    elif option == "4":
        display_all_books()
    elif option == "5":
        display_statistics()
    elif option == "6":
        print("📁 Library saved to file. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please choose between 1 and 6.")
