import socket
import _thread

HOST = '10.10.14.31'              # Endereco IP do Servidor
PORT = 8080            # Porta que o Servidor esta

def conectado(con, cliente):
    print ('Conectado por', cliente)

    while True:
        msg = con.recv(1024)
        if not msg: break
        print (cliente, msg)

    print ('Finalizando conexao do cliente', cliente)
    con.close()
    _thread.exit()

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

orig = (HOST, PORT)

tcp.bind(orig)
#while True:
tcp.listen(1)

while True:
    con, cliente = tcp.accept()
    _thread.start_new_thread(conectado, tuple([con, cliente]))

tcp.close()

