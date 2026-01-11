def selecionar_opcao(opcao):
    print(opcao)
    if opcao == "1":
        adicionar_produto()
    elif opcao == "2":
        listar_produto()
    elif opcao == "3":
        atualizar_produto()
    elif opcao == "4":
        excluir_produto()
    elif opcao == "0":
        sair()

else:

    print("Opção inválida. Escolha uma opção do menu")

    iniciar_sistema()



def exibir_menu(): #Menu principal
    print("="*50)
    print("7 - Cadastro Geral")
    print("0 - Sair")
    # print("-"*70)
    


def iniciar_sistema():
    exibir_menu()
    opcao_escolhida = input("Escolha uma das opções: ")
    selecionar_opcao(opcao_escolhida)
    inicia_sistema() # mudar para um while para não ficar consumindo recurso.


iniciar_sistema()
