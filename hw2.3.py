from flask import Flask, request, jsonify

app = Flask(__name__)

# Danh sách các quyển sách
books = []

# Thêm sách mới
@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    books.append(data)
    return jsonify({'Thông báo': 'Thêm sách thành công'})

# Lấy danh sách các quyển sách
@app.route('/get_books', methods=['GET'])
def get_books():
    return jsonify(books)

# Cập nhật thông tin sách
@app.route('/update_book/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    for book in books:
        if book['id'] == book_id:
            book.update(data)
            return jsonify({'Thông báo': 'Chỉnh sửa thông tin thành công'})
    return jsonify({'Thông báo': 'Không tìm thấy sách'})

# Xoá sách
@app.route('/delete_book/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book['id'] == book_id:
            del books[index]
            return jsonify({'Thông báo': 'Xóa sách thành công'})
    return jsonify({'Thông báo': 'Không tìm thấy sách'})

if __name__ == '__main__':
    app.run()
