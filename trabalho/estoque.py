import os
import sys
from colorama import Fore, Back, Style

def adicionar_produto():
    tarefa = input('digite um produto')

def sair():
    limpar_tela()
    titulo_menu('Confirmação de Saída')

    confirmacao=input('Deseja realmente sair do sistema? (S/N)  ').strip().upper()
    if confirmacao == 'S':
        print(Fore.RED + '\nEncerrando o sistema\n\n' + Style.RESET_ALL)
        sys.exit()                          #fecha o programa
    else:
        return


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  # usar cls para Windows / clear para linux

def pausar():
    input('Digite ENTER para continuar ...')

def selecionar_opcao(opcao):
    if opcao == "1":            # adicionar_produto()
        adicionar_produto()
        pausar()

    elif opcao == "2":
        print("teste 02")
        pausar()
#         # listar_produto()
    elif opcao == "3":
        print("teste 03")
        pausar()
#         # atualizar_produto()
    elif opcao == "4":
        print("teste 04")
        pausar()
#         # excluir_produto()
    elif opcao == "0":
       sair()
    else:
        print("Opção inválida. Escolha uma opção do menu")
        pausar()


def titulo_menu(titulo):
    print()
    texto_central = ' ' + titulo +' '   # afastar o texto do menu das laterais 1 caracter de cada lado
    largura_menu = 70                   # definir largura total em caracteres do titulo do menu

    largura_texto_central = len(texto_central)                          # determina o tamanho do texto central do menu
    largura_lados_menu = (largura_menu - largura_texto_central) // 2    # determina o tamanho dos lados do menu

    linha_menu = '#'*largura_lados_menu + texto_central + '#'*largura_lados_menu    # texto a ser exibido no titulo menu
    print(Fore.BLUE + Back.WHITE + linha_menu + Style.RESET_ALL)

def itens_menu():
    itens = ('1 - Adicionar novo produto', '2 - Atualizar produtos', '3 - Excluir produto','4 - Visualizar produtos existentes', '5 - Registrar e controlar vendas', '0 - Sair')
    for item in itens:
        print(item)

def exibir_menu():
    limpar_tela()
    titulo_menu('MENU')     #chama def exibir titulo do menu
    itens_menu()            #chama def exibir itens do menu


def iniciar_sistema():
    opcao_escolhida = ""
    while True:
        exibir_menu()
        opcao_escolhida = input("Escolha uma das opções: ")
        selecionar_opcao(opcao_escolhida)


iniciar_sistema()
