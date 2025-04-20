# 📚 Personal Library Manager (CLI App)

A command-line Python application to help you manage your personal book collection!  
Add, remove, search, and track your reading progress with a simple and interactive interface.

---

## 🔧 Features

- ✅ Add books with title, author, year, genre, and read status  
- ❌ Remove books by title  
- 🔍 Search books by title or author  
- 📋 Display all stored books in a clean format  
- 📊 View statistics: total books and percentage read  
- 💾 File handling to save and load data from `books.txt`

---

## 📂 Book Format (Stored in `books.txt`)

Each book is stored in a CSV-style format:

Example: The Great Gatsby,F. Scott Fitzgerald,1925,Fiction,Read 1984,George Orwell,1949,Dystopian,Unread

---

## 🖥️ How It Works

### When you run the program, you’ll see this menu:

```bash
Welcome to your Personal Library Manager!
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit
```
---

### ✅ Add a Book

```bash
Enter the book title: The Alchemist  
Enter the author: Paulo Coelho  
Enter the year of publication: 1988  
Enter the genre: Fiction  
Have you read this book? (yes/no): yes 
```

---

### ❌ Remove a Book
``` bash
Enter the title of the book to remove: The Alchemist  
✅ Book 'The Alchemist' removed successfully.
```

---

### 🔍 Search for a Book

```bash
Search by:
1. Title
2. Author
Enter your choice: 2
Enter the author: George Orwell

1. 1984 by George Orwell (1949) - Dystopian - Unread
```

---

### 📋 Display All Books
```bash
1. The Great Gatsby by F. Scott Fitzgerald (1925) - Fiction - Read  
2. 1984 by George Orwell (1949) - Dystopian - Unread  
```

---

### 📊 Display Statistics

```bash
Total books: 5  
Percentage read: 60.0%
```