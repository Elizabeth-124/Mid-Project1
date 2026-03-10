import random
import string

class Book:

    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True


class Member:

    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.books_issued = []


class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def generate_id(self, prefix):

        characters = string.ascii_uppercase + string.digits
        random_part = ''.join(random.choices(characters, k=5))

        return f"{prefix}-{random_part}"

    def add_book(self, title, author):

        new_id = self.generate_id("B")
        new_book = Book(title, author, new_id)

        self.books.append(new_book)

        return f"Success! New book added with ID: {new_id}"

    def add_member(self, name):

        new_id = self.generate_id("M")
        new_member = Member(name, new_id)

        self.members.append(new_member)

        return f"Success! New member added with ID: {new_id}"

    def issue_book(self, book_id, member_id):

        book = None
        member = None

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        if not book:
            return "Error: Book not found"

        if not member:
            return "Error: Member not found"

        if not book.is_available:
            return "Error: Book already issued"

        book.is_available = False
        member.books_issued.append(book)

        return f"Success: Book '{book.title}' issued to {member.name}"

    def return_book(self, book_id):

        for b in self.books:

            if b.book_id == book_id:

                if b.is_available:
                    return f"Error! Book '{b.title}' was not borrowed"

                b.is_available = True
                return f"Success! Book '{b.title}' returned"

        return f"Error! Book with ID '{book_id}' not found"