import multiprocessing #-
import zmq
from time import sleep #-
from const import *

def server():
  context = zmq.Context()
  socket  = context.socket(zmq.REP)       # create reply socket
  socket.bind("tcp://*:"+ PORT)            # bind socket to address
  print(f"Servidor iniciado e escutando na porta {PORT}...")

  while True:
    message = socket.recv()               # wait for incoming message
    message_str = message.decode()
    print(f"Recebido: {message_str}")

    if not "STOP" in message_str:
      
      # --- Lógica das Novas Funções ---
      try:
        parts = message_str.split('|')
        operation = parts[0].upper()
        args = parts[1:]

        if operation == "ADD":
          if len(args) != 2:
            reply = "Erro: A operação ADD requer 2 argumentos."
          else:
            num1 = float(args[0])
            num2 = float(args[1])
            result = num1 + num2
            reply = str(result)
        
        elif operation == "UPPER":
          if len(args) != 1:
            reply = "Erro: A operação UPPER requer 1 argumento."
          else:
            reply = args[0].upper()
            
        else:
          reply = "Erro: Operação desconhecida."
          
      except Exception as e:
        reply = f"Erro no servidor: {str(e)}"
      # --- Fim da Lógica ---

      socket.send(reply.encode())         # send it away (encoded)
    else:                         
      print("Recebido comando STOP. Encerrando.")
      break                               # break out of loop and end