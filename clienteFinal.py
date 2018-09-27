from socket import * 
import threading
import sys
s = socket()
meusbytes = ""
def msg():
	global meusbytes
	meusbytes = str.encode(input(),"utf-8")
def rec():
	while True:
		print ("Resposta do servidor:" + s.recv(4096).decode("utf-8"))

s.connect(("10.0.2.15",8000))
t = threading.Thread(target=rec, args=())
t.start()
while True:
	msg()
	s.send(meusbytes)
s.close