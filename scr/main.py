import function

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
        print(function.t_para_m(frase))

    elif opcao == 2:
        while True:
            try:
                frase = input("Digite:\n=> ")
                print(function.m_para_t(frase))
                break
            except:
                print("ERRO: Valor invalido")
    elif opcao == 0:
        break


