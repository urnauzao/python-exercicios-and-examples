from socket import *

servidor = "127.0.0.1" #ou localhost
porta = 43211

obj_socket = socket(AF_INET, SOCK_STREAM) #formas de conexao e comunicao com servidor
obj_socket.bind((servidor, porta)) #bind deve receber uma tupla
obj_socket.listen(2) #limite de conexoes = 2

print("Aguardando cliente conectar...")

while True:
    # na linha abaixo está sendo retornado uma TUPLA
    con, cliente = obj_socket.accept() #fica aguardando que ocorra a conexao com um cliente, e só então avança a próxima linha do código

    while True:
        msg_recebida = str(con.recv(1024)) # 1024 é o tamanho máximo de bytes na msg
        print("Recebemos: ", msg_recebida)
        msg_enviada = b'Olah Cliente' # o "b" é de msg em bytes
        con.send(msg_enviada)
        break
    con.close()