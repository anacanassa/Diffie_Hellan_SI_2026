from socket import *
import random
import Utils

#Informação de rede
serverName = "10.1.70.9"
serverPort = 25000

#Criar a conexão
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

#Definindo valores diffie-helman
severInfo = str(clientSocket.recv(65000),"utf-8")
n, g, r1 = map(int,severInfo.split(",")) 
y = random.randint(2, n-2)
r2 = pow(g, y, n)

#Enviando r2
clientSocket.send(bytes(str(r2), "utf-8"))

k2 = pow(r1, y, n)
reducedK2 = k2 % 26

#Definir a mensagem
sentence = input("Input lowercase sentence: ")
criptSentence = Utils.withCesar(sentence, reducedK2, True)
print("N:",n)
print("G:",g)
print("R2:",r2)
print("K2:",k2)
print("Chave:",reducedK2)
print("Mensagem criptografada:",criptSentence)

clientSocket.send(bytes(str(criptSentence), "utf-8"))

modifiedSentence = clientSocket.recv(65000)
text = str(modifiedSentence,"utf-8")
decriptoModified = Utils.withCesar(text, reducedK2, False)

print ("Received from Make Upper Case Server: ", decriptoModified)
clientSocket.close()
