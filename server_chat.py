import socket


sock = socket.socket()
host = ''
port = 10105
buffer_size = 2048

send_bool = True

sock.bind((host,port))

sock.listen(5)

print("Server Started Waiting for client...\n\n")
conn,addr = sock.accept()
print(f"Connection Established to  IP : {addr[0]} | PORT : {addr[1]}")

name = input("Enter your name : ")
conn.send(name.encode())

client_name = str(conn.recv(200),"utf-8")
print("\nChat Started\n===============\n")
print(f"{client_name} has joined the chat\n")

while True:
			
	send_data = input("Me :")
	conn.send(send_data.encode())
	if send_data == "Bye":
		print("Chat Ended")
		conn.close()
		sock.close()
		break
		
	recv_data = str(conn.recv(buffer_size),"utf-8")
	if recv_data == "Bye":
		conn.close()
		sock.close()
		print(f"{client_name} : {recv_data}")
		print("Chat Ended")
		break
	print(f"{client_name} : {recv_data}\n")

	
