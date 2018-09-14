from socket import *
import threading
import sys

s = socket ()
meusbytes = "0"
def msg():
    global meusbytes
    minhastr = input() #para escrever, tipo scanf
    #print (minhastr)
    meusbytes=str.encode (minhastr, "UTF-8")
    #print (meusbytes)
def rec():
    while True:
        data = s.recv (1024)
        print (data.decode("utf-8"))

s.connect(("10.10.14.1", 8753)) #conexão com a maquina do mjoao
t = threading.Thread(target=rec,args=())
t.start()
while True:
    x = msg()
    #data = s.recv (1024)
    #print (data.decode("utf-8"))
    s.send (meusbytes)


s.close ()