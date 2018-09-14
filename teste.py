from socket import *
import threading
import sys
from random import randint


s = socket ()

meusbytes = "0"
def msg():
    global meusbytes
    meusbytes = str.encode (str(randint(1, 3)), "UTF-8")
    #print (meusbytes)
def rec():
    while True:
        data = s.recv (1024)
        print (data.decode("utf-8"))

s.connect(("10.10.14.30", 8080)) #conexão com a maquina do mjoao
t = threading.Thread(target=rec,args=())
t.start()
#while True:
msg()

s.send (meusbytes)

s.close ()