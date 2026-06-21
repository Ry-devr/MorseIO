from function import TradutorMorse, limpar_terminal, reproduzir_morse
from gerenciador_arquivo import GerenciadorArquivo

limpar_terminal()
tradutor = TradutorMorse()
gereArquivo = GerenciadorArquivo("historico.csv")

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
        limpar_terminal()
    else:
        jarodou = 1

    print('''
========================================
                OPÇOES
========================================
  [1] Traduzir texto → morse
  [2] Traduzir morse → texto
  [3] Histórico
  [0] Sair
========================================
Escolha uma opção:
''')
    while True:
        try:
            opcao = int(input("=> "))
            break
        except ValueError:
            print("ERRO: Valor invalido ou nao exite")
        except EOFError:
            print()
            opcao = -1
            break

    ### Traduzir texto ###
    if opcao == 1:
        while True:
            try:
                frase = input("Digite:\n=> ")
                resultado = tradutor.texto_para_morse(frase)
                print("Resultado:", resultado)
                reproduzir_morse(resultado)

                historico = gereArquivo.recuperaDados()
                historico.append([frase, resultado, "texto -> morse"])
                gereArquivo.salvarDados(historico)

                tentar = input("Quer tentar novamente (s,n)? ").lower().strip()
                if tentar in ["s","sim", ""]:
                    pass
                elif tentar in ["n","nao","não"]:
                    break
            except KeyError as e:
                print(f"CARACTER INVALIDO:{e}, tente novamente ")
            except EOFError:
                break

    ### Traduzir morce ###
    elif opcao == 2:
        while True:
            try:
                morse = input("Digite:\n=> ")
                resultado = tradutor.morse_para_texto(morse)
                print("Resultado", resultado)

                historicoM = gereArquivo.recuperaDados()
                historicoM.append([morse, resultado, "Morse -> texto"])
                gereArquivo.salvarDados(historicoM)
                break
            except KeyError as a:
                print(f"CARACTER IVALIDO: {a}, tente novamente")
            except EOFError:
                break

    elif opcao == 3:
        historico = gereArquivo.recuperaDados()
        for h in historico:
            print(f"[{h[2]}] {h[0]} -> {h[1]}")
 
    ### Sair ###
    elif opcao == 0:
        print("saindo...")
        limpar_terminal()
        break


