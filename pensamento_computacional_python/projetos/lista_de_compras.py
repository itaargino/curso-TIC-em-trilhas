lista_compras = []

def verificar_repeticao(lista_compras, nome):
    for produto in lista_compras:
        if nome.lower() == produto['nome'].lower():
            return True
    return False

def adicionar_produto(produto, nome, quantidade, descricao, unidade):
    if verificar_repeticao(lista_compras, nome):
        print("Produto já existe na lista de compras.")
        return menu()

    id_do_produto = len(lista_compras) + 1
    produto = {
        'nome': nome,
        'quantidade': quantidade,
        'descricao': descricao,
        'unidade': unidade,
        'id': id_do_produto
    }
    lista_compras.append(produto)
    print("Produto adicionado com sucesso!")
    return menu()

def remover_produto(id_do_produto):
    for produto in lista_compras:
        if produto['id'] == id_do_produto:
            lista_compras.remove(produto)
            print("Produto removido com sucesso!")
            return menu()
    print("Produto não encontrado.")
    return menu()

def pesquisar_produto(nome):
    for produto in lista_compras:
        if nome.lower() in produto['nome'].lower():
            print("Produto encontrado:", produto)
            print("Quantidade:", produto['quantidade'], produto['unidade'])
            return menu()
    print("Produto não encontrado.")
    return menu()


def listar_produtos():
    if not lista_compras:
        print("Lista de produtos está vazia.")
    else:
        print("Lista de produtos:")
        for produto in lista_compras:
            print("Nome:", produto['nome'], "||", "ID:", produto['id'], "||", "Quantidade:", produto['quantidade'], produto['unidade'])

def iniciar():
    print(" Bem-vindo à lista de compras simples ")
    menu()

def menu():
    listar_produtos()
    print("\nLista de compras simples")
    print("1. Adicionar Produto")
    print("2. Remover Produto")
    print("3. Pesquisar produto")
    print("4. Sair")

    escolha = input("Digite o número da opção desejada: ")

    if escolha == '1':
        nome = input("Digite o nome do produto: ")
        quantidade = input("Digite a quantidade do produto: ")
        descricao = input("Digite a descrição do produto: ")
        print("Escolha a unidade do produto:")
        print("1. Quilograma")
        print("2. Grama")
        print("3. Litro")
        print("4. Mililitro")
        print("5. Unidade")
        print("6. Metro")
        print("7. Centímetro")
        vetor_unidades = ['Quilograma', 'Grama', 'Litro', 'Mililitro', 'Unidade', 'Metro', 'Centímetro']
        while True:
            escolha_unidade = input("Digite o número correspondente: ")
            if escolha_unidade not in ['1', '2', '3', '4', '5', '6', '7']:
                print("Opção inválida, por favor tente novamente.")
                continue
            else:
                break
        unidade = vetor_unidades[int(escolha_unidade) - 1]
        adicionar_produto(lista_compras, nome, quantidade, descricao, unidade)

    elif escolha == '2':
        try:
            id_do_produto = int(input("Digite o ID do produto que deseja remover: "))
            remover_produto(id_do_produto)
        except ValueError:
            print("Entrada inválida. Digite um número.")
            return menu()

    elif escolha == '3':
        nome = input("Digite o nome do produto que deseja pesquisar: ")
        pesquisar_produto(nome)

    elif escolha == '4':
        print("Obrigado por usar a lista de compras simples.")
        return

    else:
        print("Opção inválida.")
        return menu()

iniciar()
