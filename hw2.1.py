from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/get_file', methods=['GET'])
def get_file_content():
    try:
        with open('file.txt', 'r') as file:
            content = file.read()
            return jsonify({'file_content': content})
    except Exception as e:
        return jsonify({'Thông báo ': 'Đọc file lỗi'})

if __name__ == '__main__':
    app.run(debug=True)
