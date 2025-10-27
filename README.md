[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/k52jMr_H)
# Client-Server-ZeroMQ
Simple example of the client-server pattern using ZeroMQ
(from distributed-systems.net)

### First, install ZeroMQ (on each machine):

    sudo apt update

    sudo apt install python3-zmq

### Or, with virtual environments (also on each machine -- only install pip3 and venv if not yet installed):

    sudo apt update
    sudo apt install python3-pip
    sudo apt install python3-venv
    python3 -m venv myvenv
    source myvenv/bin/activate
    pip3 install pyzmq

### Next, configure the IP address and port number of the server's machine in the const.py file

Note: Make sure that this repo is cloned in all the machines used for this experiment. (Se estiver testando localmente, pode usar `HOST = "127.0.0.1"` no `const.py`).

### Then, run the client and server:

On the machine for which the IP address was configured:

    python3 server.py

On another machine (or in another terminal, if testing locally):

    python3 client.py

### Now, add other services (operations) in the server and call them from the client.

---

### Novas Funcionalidades Implementadas

O servidor foi modificado para ir além de um simples "eco". Ele agora funciona como um servidor de operações, capaz de processar diferentes tipos de requisições com base em um protocolo simples.

**Protocolo:**

As mensagens do cliente para o servidor devem seguir o formato:
`OPERACAO|ARGUMENTO1|ARGUMENTO2|...`

O servidor processa a `OPERACAO` e retorna o resultado como uma string.

**Operações Adicionadas:**

1.  **ADD (Adição)**
    * **Formato:** `ADD|num1|num2`
    * **Descrição:** Soma dois números (`num1` e `num2`).
    * **Exemplo de Resposta:** `42`

2.  **UPPER (Maiúsculas)**
    * **Formato:** `UPPER|texto`
    * **Descrição:** Converte a string `texto` para letras maiúsculas.
    * **Exemplo de Resposta:** `OLÁ, MUNDO`

3.  **STOP (Parar)**
    * **Formato:** `STOP`
    * **Descrição:** Instrui o servidor a encerrar sua execução.

O `client.py` foi atualizado para demonstrar a chamada dessas duas novas operações (`ADD` e `UPPER`) antes de enviar o comando `STOP`.