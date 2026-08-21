# Diffie Hellman SI 2026

# TCP Client/Server com Diffie-Hellman e Cifra de César

# Demonstração de uso - vídeo

https://youtu.be/Xvy-lLhzV00

## Descrição

Este projeto implementa uma comunicação cliente-servidor utilizando sockets TCP em Python. O objetivo é demonstrar conceitos básicos de criptografia, incluindo:

- Troca de chaves utilizando o algoritmo Diffie-Hellman.
- Criptografia e descriptografia usando a Cifra de César.
- Comunicação TCP entre cliente e servidor.

## Estrutura do Projeto

### Simple_tcpServer.py

Responsável por iniciar o servidor TCP e aguardar conexões de clientes.

Funcionalidades:

- Gera um número primo de 256 bits.
- Define os parâmetros do protocolo Diffie-Hellman.
- Recebe a chave pública do cliente.
- Calcula a chave secreta compartilhada.
- Recebe uma mensagem criptografada.
- Descriptografa a mensagem utilizando a chave derivada.
- Converte o texto para letras maiúsculas.
- Criptografa novamente a resposta e a envia ao cliente.

### Simple_tcpClient.py

Responsável por conectar ao servidor e enviar mensagens.

Funcionalidades:

- Conecta ao servidor TCP.
- Recebe os parâmetros Diffie-Hellman enviados pelo servidor.
- Gera sua chave pública.
- Calcula a chave secreta compartilhada.
- Solicita uma mensagem do usuário.
- Criptografa a mensagem usando Cifra de César.
- Envia a mensagem ao servidor.
- Recebe a resposta processada.
- Descriptografa e exibe o resultado final.

### Utils.py

Arquivo auxiliar contendo funções criptográficas.

Funcionalidades:

#### Cifra de César

Função `withCesar()`:

- Realiza criptografia ou descriptografia por deslocamento de caracteres.
- Utilizada para proteger as mensagens trocadas entre cliente e servidor.

#### Teste de Primalidade

Função `miller_rabin()`:

- Implementa o algoritmo probabilístico Miller-Rabin.
- Verifica se um número possui alta probabilidade de ser primo.

#### Geração de Números Primos

Função `gerar_primo()`:

- Gera números primos aleatórios com quantidade de bits definida.
- Utilizada para criar o parâmetro primo do Diffie-Hellman.

## Fluxo de Comunicação

1. O servidor gera os parâmetros Diffie-Hellman.
2. O cliente recebe os parâmetros e gera sua chave pública.
3. Cliente e servidor calculam a mesma chave secreta.
4. A chave é reduzida para um valor entre 0 e 25.
5. O cliente cifra a mensagem usando Cifra de César.
6. O servidor decifra a mensagem, processa o texto e responde.
7. O cliente decifra a resposta recebida.

## Objetivo Educacional

O projeto foi desenvolvido com foco em aprendizado, demonstrando conceitos de:

- Programação de redes com sockets TCP.
- Troca segura de chaves utilizando Diffie-Hellman.
- Criptografia simétrica simples com Cifra de César.
- Manipulação de mensagens entre cliente e servidor.

## Mensagem do cliente

<img width="1313" height="919" alt="ClientVision" src="https://github.com/user-attachments/assets/d0a39341-c2a0-45d0-8f29-4b3612f8e4e4" />

## Mensagem server

<img width="1349" height="916" alt="ServerVision (1)" src="https://github.com/user-attachments/assets/b9f337cb-872e-4c58-a5c6-d3e9e6ee5ea2" />


## Capturas Wireshark 

#### N, G, R1:

<img width="1519" height="801" alt="N_G_R1" src="https://github.com/user-attachments/assets/a37e8b33-77bb-4e88-9bb6-67906813b838" />


#### R2:

<img width="1495" height="699" alt="R2" src="https://github.com/user-attachments/assets/dd2759ee-dd95-4101-8075-f830d5c6a214" />


#### Mensagem criptografada Client:

<img width="1494" height="644" alt="ClientMsg" src="https://github.com/user-attachments/assets/34d474b7-1043-43eb-82bd-1dc55363383f" />



#### Mensagem criptografada Server:

<img width="1491" height="674" alt="ServerMsg" src="https://github.com/user-attachments/assets/6a231553-1222-4c7e-960d-04b8365f5031" />
