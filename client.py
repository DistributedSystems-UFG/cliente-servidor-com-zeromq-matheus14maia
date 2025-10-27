import multiprocessing #-
import zmq
from time import sleep #-
from const import *

def client():
  context = zmq.Context()
  socket  = context.socket(zmq.REQ)       # create request socket
  socket.connect("tcp://"+ HOST + ":" + PORT) # block until connected

  # 1. Testar operação ADD
  print("Enviando: ADD|40|2")
  socket.send(b"ADD|40|2")                 # send message
  message = socket.recv()                 # block until response
  print(f"Resposta (ADD): {message.decode()}")
  
  # 2. Testar operação UPPER
  print("Enviando: UPPER|olá, mundo")
  socket.send("UPPER|olá, mundo".encode())         # send message (now handled as utf-8 properly)
  message = socket.recv()                 # block until response
  print(f"Resposta (UPPER): {message.decode()}")
  
  # 3. Enviar comando STOP
  print("Enviando: STOP")
  socket.send(b"STOP")                    # tell server to stop
#-
if __name__ == "__main__": #-
  s = multiprocessing.Process(target=server) #-
  c = multiprocessing.Process(target=client) #-
#-
  s.start() #-
  sleep(2) # Espera o servidor iniciar completamente #-
  c.start() #-
  c.join() #-
  s.join() #-