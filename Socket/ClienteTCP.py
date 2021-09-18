from socket import *
# ao importar com *, se evita de utilizar ex: socket.gethostbyname(url)

servidor = "127.0.0.1"
porta = 43211

msg = bytes(input("Digite algo: "), "utf-8")
obj_socket =  socket(AF_INET, SOCK_STREAM) # AF_INET = IP, SOCK_STREAM = protocolo tcp
obj_socket.connect((servidor, porta)) #passa uma tupla
obj_socket.send(msg)
resposta = obj_socket.recv(1024)
print("Recebemos: ", resposta)
obj_socket.close()