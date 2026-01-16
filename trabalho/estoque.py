"""
--------------------------------------------------------------------------------
PROJETO: SISTEMA DE CONTROLE DE ESTOQUE E VENDAS
--------------------------------------------------------------------------------
AUTOR: GLEYDSON REBOUCAS SENA
RA:    183073
CURSO: Engenharia da Computação
REPOSITÓRIO GIT: https://github.com/gleydson-sena/logica_com_python

DESCRIÇÃO:
Sistema de gerenciamento de estoque e vendas via terminal, com persistência
em memória.

INSTRUÇÕES DE INSTALAÇÃO E EXECUÇÃO:
1. Certifique-se de estar na pasta do projeto (ou com a venv ativa).
2. Instale as dependências necessárias:
   pip install -r requirements.txt

3. Para rodar o sistema, execute o comando:
   python estoque.py (Esta dentro da pasta trabalho)
--------------------------------------------------------------------------------
"""

import os
import sys
from colorama import Fore, Back, Style

bd_produto = [] # banco de dados (apenas na memoria)
bd_vendas = []  # banco de dados (apenas na memoria)


def cancelar_venda():
    while True:
        limpar_tela()
        titulo_menu("CANCELAR VENDA", Fore.BLACK, Fore.RED, 1)
        
        if not bd_vendas:
            return Fore.YELLOW + "Nenhuma venda para cancelar." + Style.RESET_ALL

        print(f"{'ID':<4} | {'PRODUTO':<20} | {'VALOR':>10} | {'QTD':>5} | {'TOTAL':>12}")
        print("-" * 65)
        for i, v in enumerate(bd_vendas):
            print(f"{i+1:<4} | {v['produto']:<20} | {v['valor_unitario']:>10.2f} | {v['qtd']:>5} | {v['total']:>12.2f}")
        print("-" * 65)

        print(Fore.YELLOW + "Digite 0 para voltar" + Style.RESET_ALL)
        
        try:
            id_input = input("\nID da venda para ESTORNAR: ")
            if not id_input.isdigit(): continue
            
            id_venda = int(id_input)
            if id_venda == 0: return ""

            indice = id_venda - 1

            if not validar_indice(indice, bd_vendas): continue

            venda = bd_vendas[indice]
            
            # --- CONFIRMAÇÃO ---
            print(f"\n{Fore.RED}ATENÇÃO! Estornar venda de: {venda['produto']} (Qtd: {venda['qtd']}){Style.RESET_ALL}")
            confirma = input("Confirma o cancelamento? (S para Sim): ").strip().upper()

            if confirma != 'S':
                print(Fore.YELLOW + "Cancelamento abortado." + Style.RESET_ALL)
                pausar()
                continue

            # --- EXECUÇÃO ---
            # Devolve ao estoque
            for p in bd_produto:
                if p['nome'] == venda['produto']:
                    p['quantidade'] += venda['qtd']
                    break
            
            bd_vendas.pop(indice)
            print(Fore.GREEN + "Venda estornada e estoque reposto!" + Style.RESET_ALL)
            pausar()
            return ""

        except ValueError:
            continue


def relatorio_vendas():
    limpar_tela()
    titulo_menu("RELATÓRIO DE VENDAS", Fore.BLACK, Fore.MAGENTA, 1)

    if not bd_vendas:
        return Fore.YELLOW + "Nenhuma venda registrada." + Style.RESET_ALL

    print(f"{Fore.MAGENTA}{'ID':<4} | {'PRODUTO':<20} | {'VALOR':>10} | {'QTD':>5} | {'TOTAL':>12}{Style.RESET_ALL}")
    print("-" * 65)

    total_geral = 0
    for i, venda in enumerate(bd_vendas):
        total_geral += venda['total']
        print(f"{i+1:<4} | {venda['produto']:<20} | {venda['valor_unitario']:>10.2f} | {venda['qtd']:>5} | {venda['total']:>12.2f}")

    print("-" * 65)
    print(f"{Fore.GREEN}FATURAMENTO TOTAL: R$ {total_geral:.2f}{Style.RESET_ALL}")
    
    pausar()
    return ""





def validar_indice(indice, lista):      # Verifica se o índice está dentro dos limites da lista.
    if 0 <= indice < len(lista):
        return True
    else:
        print(Fore.RED + "Erro: ID não encontrado na lista. Tente novamente." + Style.RESET_ALL)
        pausar()
        return False


def registrar_venda():
    while True:
        limpar_tela()
        titulo_menu("REGISTRAR VENDA", Fore.BLACK, Fore.GREEN, 1)

        if visualizar_produtos(pausa=False) == False:                               # Mostra os produtos disponíveis
            return Fore.YELLOW + "Não há produtos para vender." + Style.RESET_ALL

        print(Fore.YELLOW + "Digite 0 para cancelar" + Style.RESET_ALL)

        try:
            id_input = input('\nDigite o ID do produto vendido: ')     # Escolha do Produto pelo indice da primeira coluna
        
            if not id_input.isdigit():
                print(Fore.RED + "Erro: Digite apenas números inteiros." + Style.RESET_ALL)
                pausar()
                continue # Volta para o início do while (redesenha a tela)

            id_escolhido = int(id_input)

            if id_escolhido == 0:
                return Fore.YELLOW + "Operação cancelada." + Style.RESET_ALL

            indice = id_escolhido - 1

            if not validar_indice(indice, bd_produto):          # verificar se o id existe
                continue

            produto = bd_produto[indice]

            # Mostra o produto selecionado
            print(f"\n{Fore.CYAN}Produto: {produto['nome']} | Preço: R$ {produto['preco']:.2f} | Estoque: {produto['quantidade']}{Style.RESET_ALL}")

            qtd_input = input('Quantas unidades foram vendidas? ')

            qtd_venda = int(qtd_input)

            if qtd_venda > produto['quantidade']:           # Tem estoque suficiente?
                return Fore.RED + f"Erro: Estoque insuficiente! Só temos {produto['quantidade']} unidades." + Style.RESET_ALL
            
            if qtd_venda <= 0:
                print(Fore.RED + "Erro: A quantidade deve ser maior que zero." + Style.RESET_ALL)
                pausar()
                continue

            valor_total = qtd_venda * produto['preco']      # Cálculo e Baixa no Estoque
            produto['quantidade'] -= qtd_venda              # Subtrai do estoque

            nova_venda = {
                'produto': produto['nome'],
                'valor_unitario': produto['preco'], 
                'qtd': qtd_venda,
                'total': valor_total
            }
            bd_vendas.append(nova_venda)


            # (Resumo)
            print("\n" + "="*40)
            print(f"{Fore.GREEN}VENDA REGISTRADA COM SUCESSO!{Style.RESET_ALL}")
            print(f"Produto: {produto['nome']}")
            print(f"Qtd: {qtd_venda} x R$ {produto['preco']:.2f}")
            print(f"{Fore.GREEN}TOTAL A RECEBER: R$ {valor_total:.2f}{Style.RESET_ALL}")
            print("="*40)
            
            pausar() # Pausa para ver o valor total
            return "" # Retorna vazio pois já mostramos o sucesso na tela

        except ValueError:
            print(Fore.RED + "Erro: Digite apenas números." + Style.RESET_ALL)
            pausar()


def excluir_produto():
    while True:
        limpar_tela()
        titulo_menu("EXCLUIR PRODUTO", Fore.BLACK, Fore.RED, 1)

        if visualizar_produtos(pausa=False) == False:
            return Fore.YELLOW + "Operação cancelada: Estoque vazio." + Style.RESET_ALL

        print(Fore.YELLOW + "Digite 0 para cancelar" + Style.RESET_ALL)

        try:
            id_input = input('\nDigite o ID do produto que deseja EXCLUIR: ')
            if not id_input.isdigit():
                print(Fore.RED + "Erro: Digite apenas números." + Style.RESET_ALL)
                pausar()
                continue

            id_escolhido = int(id_input)
        
            if id_escolhido == 0:
                return Fore.YELLOW + "Operação cancelada." + Style.RESET_ALL
            
            indice = id_escolhido - 1

            # Agora usa sua função de validação!
            if not validar_indice(indice, bd_produto):
                continue

            produto = bd_produto[indice]

            # Confirmação de segurança
            print(f"\n{Fore.RED}ATENÇÃO! Você vai apagar: {produto['nome']}{Style.RESET_ALL}")
            confirmacao = input("Tem certeza? (S para Sim / Enter para cancelar): ").strip().upper()

            if confirmacao == 'S':
                removido = bd_produto.pop(indice)
                print(f"{Fore.GREEN}Sucesso! O produto '{removido['nome']}' foi removido.{Style.RESET_ALL}")
                pausar()
                return ""
            else:
                print(Fore.YELLOW + "Exclusão cancelada pelo usuário." + Style.RESET_ALL)
                pausar()
                return ""

        except ValueError:
            print(Fore.RED + "Erro: Digite apenas números válidos." + Style.RESET_ALL)
            pausar()



def atualizar_produto():
    while True:
        limpar_tela()
        titulo_menu("Incluir produto", Fore.BLACK,Fore.LIGHTGREEN_EX,1)

        if visualizar_produtos(pausa=False) == False:
            return Fore.YELLOW + "Operação cancelada: Estoque vazio." + Style.RESET_ALL

        print(Fore.YELLOW + "Digite 0 para cancelar" + Style.RESET_ALL)
        try:
            id_input = input('\nDigite o ID do produto que deseja alterar: ')
            if not id_input.isdigit():
                print(Fore.RED + "Erro: Digite apenas números." + Style.RESET_ALL)
                pausar()
                continue

            id_escolhido = int(id_input)
            
            if id_escolhido == 0:
                return Fore.YELLOW + "Operação cancelada." + Style.RESET_ALL
            
            indice = id_escolhido - 1

            if not validar_indice(indice, bd_produto):
                continue

            produto = bd_produto[indice]

            print(f"\n{Fore.CYAN}Alterando: {produto['nome']}{Style.RESET_ALL}")

            # Pequena melhoria: aceita Enter para não mudar o valor
            novo_preco_str = input('Novo Preço (R$) [Enter mantem]: ')
            if novo_preco_str:
                novo_preco = float(novo_preco_str.replace(',', '.'))
                produto['preco'] = novo_preco

            nova_qtd_str = input('Nova Quantidade [Enter mantem]: ')
            if nova_qtd_str:
                produto['quantidade'] = int(nova_qtd_str)

            print(f"{Fore.GREEN}Sucesso! {produto['nome']} atualizado.{Style.RESET_ALL}")
            pausar()
            return ""
            
        except ValueError:
            print(Fore.RED + "Erro: Digite apenas números válidos." + Style.RESET_ALL)
            pausar()


def visualizar_produtos(pausa=True):
    limpar_tela()
    titulo_menu("LISTA DE PRODUTOS", Fore.BLACK, Fore.CYAN, 1)

    # verificar se o banco de dados não esta vazio
    if not bd_produto:

        if pausa:
            return Fore.YELLOW + "O estoque está vazio. Cadastre algo primeiro." + Style.RESET_ALL
        else:
            print(Fore.YELLOW + "O estoque está vazio." + Style.RESET_ALL)
            return False
    
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
    
    if pausa:
        pausar() # Só pausa se for chamado pelo menu principal (Opção 4)
        return ''
    else:
        return True



def adicionar_produto():
    while True:
        limpar_tela()
        titulo_menu("Incluir produto", Fore.BLACK,Fore.LIGHTGREEN_EX,1)
        
        print(Fore.YELLOW + "Digite 0 para cancelar" + Style.RESET_ALL)
        nome = input('digite o nome do produto:  ') 
        
        if nome == '0': return "" # Opção de sair
        
        if not nome:
            print(Fore.YELLOW + "\nOperação cancelada: Nome vazio." + Style.RESET_ALL)
            pausar()
            continue # Volta para o inicio

        # Verifica duplicidade
        existe = False
        for produto in bd_produto:
            if produto['nome'].lower() == nome.lower():
                print(Fore.YELLOW + f'O produto {Fore.RED}{nome}{Fore.YELLOW} já existe!' + Style.RESET_ALL)
                pausar()
                existe = True
                break
        if existe: continue

        try:
            limpar_tela()
            titulo_menu("Incluir produto", Fore.BLACK ,Fore.LIGHTGREEN_EX,1)

            preco_input = input(f'Informe do {Fore.YELLOW}{nome}{Style.RESET_ALL} \n  Preço (R$):')
            preco = float(preco_input.replace(',', '.')) # Aceita virgula ou ponto

            qtd_input = input('  Quantidade em estoque:  ')
            if not qtd_input.isdigit():
                print(Fore.RED + "Erro: Quantidade deve ser numero inteiro." + Style.RESET_ALL)
                pausar()
                continue
            
            quantidade = int(qtd_input)

            novo_produto = {
            'nome': nome,
            'preco':preco,
            'quantidade':quantidade
            }
            bd_produto.append(novo_produto)
            print()
            print(f'{Fore.YELLOW}{nome}{Fore.GREEN} incluido com {Fore.YELLOW}{quantidade}{Fore.GREEN} unidades em estoque, preço de R$ {Fore.YELLOW}{preco:.2f}{Fore.GREEN} - com sucesso!' + Style.RESET_ALL)
            pausar()
            return ""
            
        except ValueError:
            print(Fore.RED + "Erro: Valor inválido inserido." + Style.RESET_ALL)
            pausar()
 
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
    if opcao == "1":
        return adicionar_produto()
    elif opcao == "2":
        return atualizar_produto()
    elif opcao == "3":
        return excluir_produto()
    elif opcao == "4":
        return visualizar_produtos()
    elif opcao == "5":
        return registrar_venda()
    elif opcao =="6":
        return cancelar_venda()
    elif opcao =="7":
        return relatorio_vendas()

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
    itens = ('1 - Adicionar novo produto', '2 - Atualizar produtos', '3 - Excluir produto','4 - Visualizar produtos existentes', '5 - Registrar vendas', '6 - Cancelamento de vendas', '7 - Visualizana movimentação vendas', '0 - Sair')
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
