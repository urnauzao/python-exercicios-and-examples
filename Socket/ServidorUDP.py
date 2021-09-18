from socket import *
# um servidor UDP é ótimo para envio de broadcast
# UDP é mais rápido pois não tem hand shake, ou seja, nao aguarda confirmação de recebimento

servidor = "127.0.0.1"
porta = 43210

obj_socket = socket(AF_INET, SOCK_DGRAM) # SOCK_DGRAM é que define como UDP
obj_socket.bind((servidor, porta))
print("Servidor pronto...")

while True:
    dados, origem = obj_socket.recvfrom(65535) # range máximo de portas para receber informações
    print("Origem...........: ", origem)
    print("Dados recebidos..: ", dados.decode()) # transforma em string
    resposta = input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem) # encode codifica em bytes

obj_socket.close()