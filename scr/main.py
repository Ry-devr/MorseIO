import function
from os import system, name

def limpar_terminal():
    try: 
        input("Presione ENTER para continuar...")
        system("cls" if name == "nt" else "clear")
    except:
        pass

limpar_terminal()
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

-- --- .-. ... . .. ---
''')
cnt = 0
while True:
    if cnt > 0:
        limpar_terminal()
    else:
        cnt = 1

    print('''
========================================
                OPÇOES
========================================
  [1] Traduzir texto → morse
  [2] Traduzir morse → texto
  [4] Histórico
  [5] Configurações
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

    ### Traduzir texto ###
    if opcao == 1:
        frase = input("Digite:\n=> ")
        print("Resultado:", tradutor.texto_para_morse(frase))

    ### Traduzir morce ###
    elif opcao == 2:
        while True:
            try:
                frase = input("Digite:\n=> ")
                print(tradutor.morse_para_texto(frase))
                break
            except:
                print("ERRO: Valor invalido")
    
    ### Sair ###
    elif opcao == 0:
        break


