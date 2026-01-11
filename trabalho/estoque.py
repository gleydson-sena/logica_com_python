
from colorama import Fore, Back, Style
# def sair():
#     exit

 def selecionar_opcao(opcao):
    print("ttessttee ---->")
#     if opcao == "1":
#         print("teste 01")
#         # adicionar_produto()
#     elif opcao == "2":
#         print("teste 02")
#         # listar_produto()
#     elif opcao == "3":
#         print("teste 03")
#         # atualizar_produto()
#     elif opcao == "4":
#         print("teste 04")
#         # excluir_produto()
#     elif opcao == "0":
#         print("teste sair")
#         sair()
# else:
#     print("Opção inválida. Escolha uma opção do menu")


def titulo_menu(titulo):
    print()
    texto_central = ' ' + titulo +' '   # afastar o texto do menu das laterais 1 caracter de cada lado
    largura_menu = 70                   # definir largura total em caracteres do titulo do menu

    largura_texto_central = len(texto_central)                          # determina o tamanho do texto central do menu
    largura_lados_menu = (largura_menu - largura_texto_central) // 2    # determina o tamanho dos lados do menu

    linha_menu = '#'*largura_lados_menu + texto_central + '#'*largura_lados_menu    # texto a ser exibido no titulo menu
    print(Fore.BLUE + Back.WHITE + linha_menu + Style.RESET_ALL)

def itens_menu():
    itens = ('1 - adicionar Novo Produto', '2 - Atualizar Produtos','3 - Visualizar Produtos existentes', '4 - Registrar e controlar vendas', '0 - Sair')
    for item in itens:
        print(item)

def exibir_menu(): #Menu principal
    titulo_menu('MENU')
    itens_menu()


def iniciar_sistema():
    exibir_menu()
    # opcao_escolhida = input("Escolha uma das opções: ")
    # selecionar_opcao(opcao_escolhida)
    # print(selecionar_opcao)
    # iniciar_sistema() # mudar para um while para não ficar consumindo recurso.


iniciar_sistema()
