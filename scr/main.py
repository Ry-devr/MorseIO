from typing_extensions import runtime
import function
import time
from os import system, name

input("Presione ENTER para continuar...") # Uma pausa antes de limpar a tela 
system("cls" if name == "nt" else "clear") # limpar o terminal quando iniciar o programa

tradutor = function.TradutorMorse()

print('''
 ██████   ██████                                     █████         
░░██████ ██████                                     ░░███          
 ░███░█████░███   ██████  ████████   █████   ██████  ░███   ██████ 
 ░███░░███ ░███  ███░░███░░███░░███ ███░░   ███░░███ ░███  ███░░███
 ░███ ░░░  ░███ ░███ ░███ ░███ ░░░ ░░█████ ░███████  ░███ ░███ ░███
 ░███      ░███ ░███ ░███ ░███      ░░░░███░███░░░   ░███ ░███ ░███
 █████     █████░░██████  █████     ██████ ░░██████  █████░░██████ 
░░░░░     ░░░░░  ░░░░░░  ░░░░░     ░░░░░░   ░░░░░░  ░░░░░  ░░░░░░  

-----.-.-.-....---
''')

while True:
    print('''
========================================
                OPÇOES
========================================
  [1] Traduzir texto → morse
  [2] Traduzir morse → texto
  [4] Histórico
  [5] Configurações
  [6] Limpar terminal
  [0] Sair
========================================
Escolha uma opção:
''')
    while True:
        try:
            opcao = int(input("=> "))
            break
        except:
            print("ERRO: Valor invalido ou nao exite")
    
    if opcao == 1:
        frase = input("Digite:\n=> ")
        time.sleep(2)
        print("Resultado:", tradutor.texto_para_morse(frase))
    elif opcao == 2:
        while True:
            try:
                frase = input("Digite:\n=> ")
                print(tradutor.morse_para_texto(frase))
                break
            except:
                print("ERRO: Valor invalido")

    elif opcao == 6:
        system("cls" if name == "nt" else "clear")
    elif opcao == 0:
        break


