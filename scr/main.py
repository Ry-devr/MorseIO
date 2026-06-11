import function
tradutor = function.Traduzir()
while True:
    print("Opçoes: ")

    while True:
        try:
            opcao = int(input("=> "))
            break
        except:
            print("ERRO: Valor invalido ou nao exite")
    
    if opcao == 1:
        frase = input("Digite:\n=> ")

        print(tradutor.texto_para_morse(frase))
    elif opcao == 2:
        while True:
            try:
                frase = input("Digite:\n=> ")
                print(tradutor.morse_para_texto(frase))
                break
            except:
                print("ERRO: Valor invalido")
    elif opcao == 0:
        break


