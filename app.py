from flask import Flask, request, jsonify, abort # type: ignore
from models import Library, Book, Member
from services import authenticate, generate_token

app = Flask(__name__)
library = Library()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data:
        abort(400, "Missing username")
    token = generate_token(data['username'])
    return jsonify({"token": token})

@app.route('/books', methods=['GET', 'POST'])
@authenticate
def books():
    if request.method == 'POST':
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        if not title or not author:
            abort(400, "Missing title or author")
        book = library.add_book(title, author)
        return jsonify(book), 201

    # Handle GET for books
    title = request.args.get('title')
    author = request.args.get('author')
    page = int(request.args.get('page', 1))
    per_page = int(request.args.get('per_page', 5))
    books = library.search_books(title, author, page, per_page)
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET', 'PUT', 'DELETE'])
@authenticate
def book_operations(book_id):
    if request.method == 'GET':
        book = library.get_book(book_id)
        if not book:
            abort(404, "Book not found")
        return jsonify(book)

    if request.method == 'PUT':
        data = request.get_json()
        title = data.get('title')
        author = data.get('author')
        updated_book = library.update_book(book_id, title, author)
        if not updated_book:
            abort(404, "Book not found")
        return jsonify(updated_book)

    if request.method == 'DELETE':
        if library.delete_book(book_id):
            return '', 204
        else:
            abort(404, "Book not found")

@app.route('/members', methods=['GET', 'POST'])
@authenticate
def members():
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        if not name:
            abort(400, "Missing name")
        member = library.add_member(name)
        return jsonify(member), 201

    members = library.get_all_members()
    return jsonify(members)

@app.route('/members/<int:member_id>', methods=['GET', 'PUT', 'DELETE'])
@authenticate
def member_operations(member_id):
    if request.method == 'GET':
        member = library.get_member(member_id)
        if not member:
            abort(404, "Member not found")
        return jsonify(member)

    if request.method == 'PUT':
        data = request.get_json()
        name = data.get('name')
        updated_member = library.update_member(member_id, name)
        if not updated_member:
            abort(404, "Member not found")
        return jsonify(updated_member)

    if request.method == 'DELETE':
        if library.delete_member(member_id):
            return '', 204
        else:
            abort(404, "Member not found")

if __name__ == '__main__':
    app.run(debug=True)
