import socket

sock = socket.socket()
host = "192.168.10.14"
port = 10105
buffer_size = 2048

sock.connect((host,port))
print(f"\nConnected to IP : {host} | PORT : {port}")

server_name = str(sock.recv(200),"utf-8")

name = input("Enter your name : ")
sock.send(name.encode())


print("\nChat Started\n===============\n")
print(f"\nJoined to {server_name} Chat Room\n")


while True:
	recv_data  = (sock.recv(buffer_size)).decode("utf-8")
	if recv_data == "Bye":
		sock.close()
		print(f"{server_name}  : {recv_data}")
		print("Chat Ended\n")
		break
	print(f"{server_name} : {recv_data}\n")
	
	send_data = input("Me :")
	sock.send(send_data.encode())
	if send_data == "Bye":
		print("Chat Ended")
		sock.close()
		break
  	 
