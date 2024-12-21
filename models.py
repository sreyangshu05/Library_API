from typing import List, Dict, Optional

class Book:
    def __init__(self, book_id: int, title: str, author: str):
        self.book_id = book_id
        self.title = title
        self.author = author

    def to_dict(self) -> Dict[str, str]:
        return {"id": self.book_id, "title": self.title, "author": self.author}

class Member:
    def __init__(self, member_id: int, name: str):
        self.member_id = member_id
        self.name = name

    def to_dict(self) -> Dict[str, str]:
        return {"id": self.member_id, "name": self.name}

class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.members: List[Member] = []
        self.next_book_id = 1
        self.next_member_id = 1

    def add_book(self, title: str, author: str) -> Dict[str, str]:
        book = Book(self.next_book_id, title, author)
        self.books.append(book)
        self.next_book_id += 1
        return book.to_dict()

    def get_book(self, book_id: int) -> Optional[Dict[str, str]]:
        for book in self.books:
            if book.book_id == book_id:
                return book.to_dict()
        return None

    def update_book(self, book_id: int, title: str, author: str) -> Optional[Dict[str, str]]:
        for book in self.books:
            if book.book_id == book_id:
                book.title = title or book.title
                book.author = author or book.author
                return book.to_dict()
        return None

    def delete_book(self, book_id: int) -> bool:
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def search_books(self, title: str, author: str, page: int, per_page: int) -> List[Dict[str, str]]:
        results = [
            book.to_dict()
            for book in self.books
            if (not title or title.lower() in book.title.lower())
            and (not author or author.lower() in book.author.lower())
        ]
        start = (page - 1) * per_page
        return results[start:start + per_page]

    def add_member(self, name: str) -> Dict[str, str]:
        member = Member(self.next_member_id, name)
        self.members.append(member)
        self.next_member_id += 1
        return member.to_dict()

    def get_member(self, member_id: int) -> Optional[Dict[str, str]]:
        for member in self.members:
            if member.member_id == member_id:
                return member.to_dict()
        return None

    def update_member(self, member_id: int, name: str) -> Optional[Dict[str, str]]:
        for member in self.members:
            if member.member_id == member_id:
                member.name = name or member.name
                return member.to_dict()
        return None

    def delete_member(self, member_id: int) -> bool:
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                return True
        return False

    def get_all_members(self) -> List[Dict[str, str]]:
        return [member.to_dict() for member in self.members]
