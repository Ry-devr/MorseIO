import function

function.limpar_terminal()
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
jarodou = 0
while True:
    if jarodou > 0:
        function.limpar_terminal()
    else:
        jarodou = 1

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
        while True:
            try:
                frase = input("Digite:\n=> ")
                print("Resultado:", tradutor.texto_para_morse(frase))
                break
            except KeyError as e:
                print(f"CARACTER INVALIDO:{e}, tente novamente ")

    ### Traduzir morce ###
    elif opcao == 2:
        while True:
            try:
                frase = input("Digite:\n=> ")
                print(tradutor.morse_para_texto(frase))
                break
            except KeyError as a:
                print(f"CARACTER IVALIDO: {a}, tente novamente")
 
    ### Sair ###
    elif opcao == 0:
        print("saindo...")
        function.limpar_terminal()
        break


