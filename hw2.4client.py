import socket

HOST = '127.0.0.1'
PORT = 12345

# Tên tập tin cần gửi
file_name = './file.txt'

# Tạo socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Kết nối tới Server
client_socket.connect((HOST, PORT))

# Gửi tên tập tin tới Server
client_socket.sendall(file_name.encode())

# Gửi dữ liệu tập tin tới Server
with open(file_name, 'rb') as file:
    client_socket.sendfile(file)

# Đóng kết nối
client_socket.close()
