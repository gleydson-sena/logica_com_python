import os
import sys
from colorama import Fore, Back, Style

bd_produto = [] # banco de dados (apenas na memoria)


def visualizar_produtos():
    limpar_tela()
    titulo_menu("LISTA DE PRODUTOS", Fore.BLACK, Fore.CYAN, 1)

    # verificar se o banco de dados não esta vazio
    if not bd_produto:
        return Fore.YELLOW + "O estoque está vazio. Cadastre algo primeiro." + Style.RESET_ALL
    
    limpar_tela()
    titulo_menu("LISTA DE PRODUTOS", Fore.BLACK, Fore.CYAN, 1)

    # cria o cabecalho definido o numero de caracteres e alinamento <esquerda, >direita
    print(f"{Fore.CYAN}{'ID':<4}|{'NOME DO PRODUTO':<30}|{'PREÇO (R$)':>12}|{'QTD':>5}{Style.RESET_ALL}")
    print("-" * 60)


    # cria os itens do relatorio
    for indice, produto in enumerate(bd_produto):
        id_visual = indice + 1
        nome = produto['nome']
        preco = produto['preco']
        qtd = produto['quantidade']

        print(f'{id_visual:<4}|{nome:<30}|{preco:>12.2f}|{qtd:>5}')
    print("-" * 60)
    pausar()

def adicionar_produto():
    limpar_tela()
    titulo_menu("Incluir produto", Fore.BLACK,Fore.LIGHTGREEN_EX,1)
    nome = input('digite o nome do produto:  ') # primeiro pega o nome para verificacao e posterior inclusao
    
    if not nome:                                # se estiver vazio, cancela
        print(Fore.YELLOW + "\nOperação cancelada: Nome vazio." + Style.RESET_ALL)
        pausar()
        return

    for produto in bd_produto:
        if produto['nome'].lower() == nome.lower():
            print(Fore.YELLOW + f'O produto {Fore.RED}{nome}{Fore.YELLOW} já existe!' + Style.RESET_ALL)
            pausar()
    

    try:
        limpar_tela()
        titulo_menu("Incluir produto", Fore.BLACK ,Fore.LIGHTGREEN_EX,1)

        preco = float(input(f'Informe do {Fore.YELLOW}{nome}{Style.RESET_ALL} \n  Preço (R$):'))
        quantidade = int(input('  Quantidade em estoque:  '))

        novo_produto = {
        'nome': nome,
        'preco':preco,
        'quantidade':quantidade
        }
        bd_produto.append(novo_produto)
        print()
        return f'{Fore.YELLOW}{nome}{Fore.GREEN} incluido com {Fore.YELLOW}{quantidade}{Fore.GREEN} unidades em estoque, preço de R$ {Fore.YELLOW}{preco:.2f}{Fore.GREEN} - com sucesso!' + Style.RESET_ALL
        # pausar()
    except ValueError:
        return f'{Fore.YELLOW}{nome}{Fore.RED} não foi incluido!' + Style.RESET_ALL
    
    

def sair():
    limpar_tela()
    titulo_menu('Confirmação de Saída')

    confirmacao=input('Deseja realmente sair do sistema? (S - para sair / outras retorna)  ').strip().upper()
    if confirmacao == 'S':
        limpar_tela()
        print(Fore.RED + '\n\n    Sistema Encerrando!\n\n' + Style.RESET_ALL)
        sys.exit()                          #fecha o programa
    else:
        return


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')  # usar cls para Windows / clear para linux

def pausar():
    input('Digite ENTER para continuar ...')

def selecionar_opcao(opcao):
    if opcao == "1":            # adicionar_produto()
        return adicionar_produto()
    elif opcao == "2":
        print("teste 02")
        pausar()
#         # listar_produto()

    elif opcao == "3":
        print("teste 03")
        pausar()
#         # atualizar_produto()

    elif opcao == "4":
        return visualizar_produtos()


    elif opcao == "0":
       sair()
    else:
        print(Fore.RED+"Opção inválida. Escolha uma opção do menu"+Style.RESET_ALL)
        pausar()


def titulo_menu(titulo, cor_texto=Fore.BLUE, cor_laterais=Fore.BLUE, espacamento=0):
    print()
    texto_central = ' ' + titulo +' '   # afastar o texto do menu das laterais 1 caracter de cada lado
    largura_menu = 70                   # definir largura total em caracteres do titulo do menu

    largura_texto_central = len(texto_central)                          # determina o tamanho do texto central do menu
    largura_lados_menu = (largura_menu - largura_texto_central) // 2    # determina o tamanho dos lados do menu
    lados = '#'*largura_lados_menu                                      # ja cria os os lados facilitando jogar no print com cores

    # texto a ser exibido no titulo menu
    print(Back.WHITE + cor_laterais + lados + cor_texto + texto_central + cor_laterais + lados + Style.RESET_ALL)

    if espacamento>0:
        print('\n' * espacamento)

def itens_menu():
    itens = ('1 - Adicionar novo produto', '2 - Atualizar produtos', '3 - Excluir produto','4 - Visualizar produtos existentes', '5 - Registrar e controlar vendas', '0 - Sair')
    for item in itens:
        print(item)     

def exibir_menu(mensagem=""):
    limpar_tela()
    titulo_menu('MENU')     #chama def exibir titulo do menu
    itens_menu()            #chama def exibir itens do menu

    if mensagem:
        print(f'\n{mensagem}')

def iniciar_sistema():
    opcao_escolhida = ""
    mensagem_status=""
    while True:
        exibir_menu(mensagem_status)
        mensagem_status=""
        opcao_escolhida = input("Escolha uma das opções: ")
        resultado  = selecionar_opcao(opcao_escolhida)

        if resultado:
            mensagem_status = resultado


iniciar_sistema()
