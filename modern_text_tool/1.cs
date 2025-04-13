using System;
using System.Collections.Generic;

namespace LibraryManagementSystem
{
    // Book class to represent a book
    class Book
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Author { get; set; }
        public bool IsAvailable { get; set; } = true;

        public Book(int id, string title, string author)
        {
            Id = id;
            Title = title;
            Author = author;
        }
    }

    // Library class to manage books
    class Library
    {
        private List<Book> books = new List<Book>();

        public void AddBook(Book book)
        {
            books.Add(book);
            Console.WriteLine($"Book '{book.Title}' added successfully.");
        }

        public void RemoveBook(int id)
        {
            Book book = books.Find(b => b.Id == id);
            if (book != null)
            {
                books.Remove(book);
                Console.WriteLine($"Book '{book.Title}' removed successfully.");
            }
            else
            {
                Console.WriteLine("Book not found.");
            }
        }

        public void BorrowBook(int id)
        {
            Book book = books.Find(b => b.Id == id && b.IsAvailable);
            if (book != null)
            {
                book.IsAvailable = false;
                Console.WriteLine($"You borrowed '{book.Title}'.");
            }
            else
            {
                Console.WriteLine("Book not available.");
            }
        }

        public void ReturnBook(int id)
        {
            Book book = books.Find(b => b.Id == id && !b.IsAvailable);
            if (book != null)
            {
                book.IsAvailable = true;
                Console.WriteLine($"You returned '{book.Title}'.");
            }
            else
            {
                Console.WriteLine("Book not found or already returned.");
            }
        }

        public void DisplayBooks()
        {
            if (books.Count == 0)
            {
                Console.WriteLine("No books in the library.");
                return;
            }

            Console.WriteLine("Library Books:");
            foreach (var book in books)
            {
                Console.WriteLine($"{book.Id}. {book.Title} by {book.Author} - {(book.IsAvailable ? "Available" : "Borrowed")}");
            }
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Library library = new Library();

            // Adding books
            library.AddBook(new Book(1, "The Great Gatsby", "F. Scott Fitzgerald"));
            library.AddBook(new Book(2, "1984", "George Orwell"));
            library.AddBook(new Book(3, "To Kill a Mockingbird", "Harper Lee"));

            // Display books
            library.DisplayBooks();

            // Borrow a book
            library.BorrowBook(2);

            // Try borrowing the same book again
            library.BorrowBook(2);

            // Return a book
            library.ReturnBook(2);

            // Remove a book
            library.RemoveBook(3);

            // Display updated books list
            library.DisplayBooks();
        }
    }
}
