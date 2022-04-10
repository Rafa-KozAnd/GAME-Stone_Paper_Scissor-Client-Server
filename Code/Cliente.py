#Imports
import socket
from tkinter import *

#Hosting
HOST = ' '    #IP Server /         ----------------------> Insert your IP Machine <----------------------
PORT = 15200

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ipServer = (HOST, PORT)
socketClient.connect(ipServer)

#Pop-Up
wind = Tk()
wind.title("Pedra,Papel,Tesoura,Lagarto,Spock")
txt_ortc = Label(wind, text="Versão extendida do 'Pedra, Papel, Tesoura' convencional,")
txt_ortc.grid(column=0, row=0)
txt_ortc = Label(wind, text="com o acréscimo do 'Lagarto' e do 'Spock', o que aumenta as")
txt_ortc.grid(column=0, row=1)
txt_ortc = Label(wind, text="propabilidades e diminuí as chances de um eventual empate.")
txt_ortc.grid(column=0, row=2)
txt_ortc = Label(wind, text="------------------------------------------------------------")
txt_ortc.grid(column=0, row=3)
txt_ortc = Label(wind, text="######################## Regras:  ########################")
txt_ortc.grid(column=0, row=4)
txt_ortc = Label(wind, text="* Pedra amassa tesoura")
txt_ortc.grid(column=0, row=6)
txt_ortc = Label(wind, text="* Pedra esmaga lagarto")
txt_ortc.grid(column=0, row=7)
txt_ortc = Label(wind, text="* Papel cobre pedra")
txt_ortc.grid(column=0, row=8)
txt_ortc = Label(wind, text="* Papel refuta Spock")
txt_ortc.grid(column=0, row=9)
txt_ortc = Label(wind, text="* Tesoura corta papel")
txt_ortc.grid(column=0, row=10)
txt_ortc = Label(wind, text="* Tesoura decapita lagarto")
txt_ortc.grid(column=0, row=11)
txt_ortc = Label(wind, text="* Lagarto come papel")
txt_ortc.grid(column=0, row=12)
txt_ortc = Label(wind, text="* Lagarto envenena Spock")
txt_ortc.grid(column=0, row=13)
txt_ortc = Label(wind, text="* Spock vaporiza pedra")
txt_ortc.grid(column=0, row=14)
txt_ortc = Label(wind, text="* Spock esmaga (ou derrete) tesoura")
txt_ortc.grid(column=0, row=15)
txt_ortc = Label(wind, text="------------------------------------------------------------")
txt_ortc.grid(column=0, row=17)


name = input('Digite seu nome : ').encode()

#Main
while True :

    print('\nPedra-Papel-Tesoura-Lagarto-Spock')
    print('')
    print('_______________')
    print('Vamos jogar: ')
    print('[0] - Pedra')
    print('[1] - Papel')
    print('[2] - Tesoura')
    print('[3] - Lagarto')
    print('[4] - Spock')
    print('[5] - Sair [Feche a Janela de Regras]')
    print('_______________')

    user = input('Escolha: ').encode()
    if user.decode() == "0":
        jog = "Pedra"
    elif user.decode() == "1":
        jog = "Papel"
    elif user.decode() == "2":
        jog = "Tesoura"
    elif user.decode() == "3":
        jog = "Lagarto"
    elif user.decode() == "4":
        jog = "Spock"

    socketClient.send(user)
    if user.decode() == "5":
        break

    print(f'Usuario escolheu {jog}')
    

    rcd = socketClient.recv(200)
    print(rcd.decode())
socketClient.close()


wind.mainloop()