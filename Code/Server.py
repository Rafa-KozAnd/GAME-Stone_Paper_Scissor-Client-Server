#Imports
import socket
import sys
import threading

#Hosting
HOST = ''           #IP Machine
PORT = 15200
socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipServer = (HOST,PORT)
socketServer.bind(ipServer)
socketServer.listen(1)

from random import randint

opc = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')

#Main
while True:
    
    socketClient, ipClient = socketServer.accept()
    while True:
        user = socketClient.recv(100)
        print(user.decode())
        comp = randint(0, 5)
        resp = ''

        if user.decode() == "0":                #Usuario escolheu Pedra
        
            if comp == 0:                               #Maquina escolheu Pedra
                resp = "Máquina escolheu Pedra \n Empate"
            elif comp == 1:                             #Maquina escolheu Papel
                resp = "Máquina escolheu Papel \n Máquina venceu"
            elif comp == 2:                             #Maquina escolheu Tesoura
                resp = "Máquina escolheu Tesoura \n Usuário venceu"
            elif comp == 3:                             #Maquina escolheu Lagarto
                resp = "Máquina escolheu Lagarto \n Usuário venceu"
            elif comp == 4:                             #Maquina escolheu Spock
                resp = "Máquina escolheu Spock \n Máquina venceu"

        elif user.decode() == "1":              #Usuario escolheu Papel

            if comp == 0:                               #Maquina escolheu Pedra
                resp = "Máquina escolheu Pedra \n Usuário venceu"
            elif comp == 1:                             #Maquina escolheu Papel
                resp = "Máquina escolheu Papel \n Empate"
            elif comp == 2:                             #Maquina escolheu Tesoura
                resp = "Máquina escolheu Tesoura \n Máquina venceu"
            elif comp == 3:                             #Maquina escolheu Lagarto
                resp = "Máquina escolheu Lagarto \n Máquina venceu"
            elif comp == 4:                             #Maquina escolheu Spock
                resp = "Máquina escolheu Spock \n Usuário venceu"

            
        elif user.decode() == "2":              #Usuario escolheu Tesoura
            
            if comp == 0:                               #Maquina escolheu Pedra
                resp = "Máquina escolheu Pedra \n Máquina venceu"
            elif comp == 1:                             #Maquina escolheu Papel
                resp = "Máquina escolheu Papel \n Usuário venceu"
            elif comp == 2:                             #Maquina escolheu Tesoura
                resp = "Máquina escolheu Tesoura \n Empate"
            elif comp == 3:                             #Maquina escolheu Lagarto
                resp = "Máquina escolheu Lagarto \n Usuário venceu"
            elif comp == 4:                             #Maquina escolheu Spock
                resp = "Máquina escolheu Spock \n Máquina venceu"


        elif user.decode() == "3":              #Usuario escolheu Lagarto
            
            if comp == 0:                               #Maquina escolheu Pedra
                resp = "Máquina escolheu Pedra \n Máquina venceu"
            elif comp == 1:                             #Maquina escolheu Papel
                resp = "Máquina escolheu Papel \n Usuário venceu"
            elif comp == 2:                             #Maquina escolheu Tesoura
                resp = "Máquina escolheu Tesoura \n Máquina venceu"
            elif comp == 3:                             #Maquina escolheu Lagarto
                resp = "Máquina escolheu Lagarto \n Empate"
            elif comp == 4:                             #Maquina escolheu Spock
                resp = "Máquina escolheu Spock \n Usuário venceu"

        elif user.decode() == "4":              #Usuario escolheu Spock

            if comp == 0:                               #Maquina escolheu Pedra
                resp = "Máquina escolheu Pedra \n Usuário venceu"
            elif comp == 1:                             #Maquina escolheu Papel
                resp = "Máquina escolheu Papel \n Máquina venceu"
            elif comp == 2:                             #Maquina escolheu Tesoura
                resp = "Máquina escolheu Tesoura \n Usuário venceu"
            elif comp == 3:                             #Maquina escolheu Lagarto
                resp = "Máquina escolheu Lagarto \n Máquina venceu"
            elif comp == 4:                             #Maquina escolheu Spock
                resp = "Máquina escolheu Spock \n Empate"

        elif user.decode() == "5":
            sys.exit()
            break

        file = open("log.txt", "a")
        file.write(resp + "\n")
        file.close()
        socketClient.send(resp.encode())