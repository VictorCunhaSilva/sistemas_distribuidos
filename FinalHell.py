from socket import *

s = socket ()

host = "10.10.13.24"
porta = 8000
s.bind ((host, porta))
s.listen (10)


def trataConexao:
        print ("Recebi a conexao de "+str(cliente))
	data = conn.recv (4096)
	#cria arquivo str(data).txt
        while True:
		cat data >> data.txt
                data = str(conn.recv(4096))
                #append data to arquivo
                #recstr = str(cliente)+" "+data.decode("utf-8")
                #print (recstr)
                #conn.send (str.encode ("Recebi sua mensagem","UTF-8"))
        print ("Fim da conexao com "+str(cliente))


while True:#vira thread
        (conn, cliente) = s.accept ()
	t = threading.Thread(target=trataConexao,args=())
	t.start()
conn.close