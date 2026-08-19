from socket import *
import Utils
import random

#Definindo valores diffie-helman
n = Utils.gerar_primo(256)
g = 5
x = random.randint(2, n-2)
r1 = pow(g, x, n)

print("Primo gerado:", n)
print("Gerador:", g)
print("R1:", r1)

#Definindo informação do servidor
serverPort = 25000
serverSocket = socket(AF_INET,SOCK_STREAM)

#Abrindo a porta
serverSocket.bind(("",serverPort))
serverSocket.listen(5) # o argumento “listen” diz à biblioteca de soquetes que queremos enfileirar no máximo 5 requisições de conexão (normalmente o máximo) antes de recusar começar a recusar conexões externas. Caso o resto do código esteja escrito corretamente, isso deverá ser o suficiente.
print ("TCP Server\n")
connectionSocket, addr = serverSocket.accept()

# wait = connectionSocket.recv(65000)
# print("clientConnected")

serverInfo = f"{n},{g},{r1}"
connectionSocket.send(bytes(serverInfo, "UTF-8"))

#Recebendo a mensagem
clientr2 = connectionSocket.recv(65000)
clientinfo = str(clientr2,"utf-8")

r2 = int(clientinfo)
k1 = pow(r2, x, n)
chave = k1 % 26

print("R2:", r2)
print("K1:", k1)
print("Cahve", chave)

sentence = connectionSocket.recv(65000)
clientSentence = str(sentence,"utf-8").replace("[","").replace("]","").replace("'", "").replace(", ","")
print(clientSentence)

decripReceived = Utils.withCesar(clientSentence, chave, False)

print ("Received From Client: ", decripReceived)

capitalizedSentence = decripReceived.upper() # processamento

criptCapitalized = Utils.withCesar(capitalizedSentence, chave, True)

connectionSocket.send(bytes(criptCapitalized, "UTF-8"))

sent = capitalizedSentence
print ("Sent back to Client: ", sent)
connectionSocket.close()