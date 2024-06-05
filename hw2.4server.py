import socket

# Địa chỉ IP và cổng của Server
HOST = '127.0.0.1'
PORT = 12345

# Tạo socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gắn socket với địa chỉ IP và cổng
server_socket.bind((HOST, PORT))

# Lắng nghe kết nối từ Client
server_socket.listen()

# Chấp nhận kết nối từ Client
client_socket, client_address = server_socket.accept()

# In địa chỉ của Client
print(f"Đã kết nối từ: {client_address}")

# Nhận dữ liệu từ Client
data = client_socket.recv(1024)

# In dữ liệu nhận được
print(f"Dữ liệu nhận được từ Client: {data.decode()}")

# Đóng kết nối
client_socket.close()
server_socket.close()
