from materias import criar_materia, editar_nota, listar_materias, obter_dados_materia

def menu():
    print("\n--- Gerenciador de Notas ---")
    print("1. Criar matéria")
    print("2. Editar nota")
    print("3. Listar matérias")
    print("4. Ver avaliações")
    print("0. Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        nome = input("Nome da matéria: ")
        n = int(input("Quantas avaliações? "))
        avaliacoes = []
        for _ in range(n):
            nome_av = input("Nome da avaliação: ")
            peso = float(input("Peso: "))
            avaliacoes.append({"nome": nome_av, "peso": peso, "nota": None})
        criar_materia(nome, avaliacoes)

    elif opcao == "2":
        materia = input("Nome da matéria: ")
        avaliacao = input("Nome da avaliação: ")
        nota = float(input("Nota: "))
        editar_nota(materia, avaliacao, nota)

    elif opcao == "3":
        print("Matérias cadastradas:")
        for m in listar_materias():
            print(f"- {m}")

    elif opcao == "4":
        materia = input("Nome da matéria: ")
        dados = obter_dados_materia(materia)
        if dados:
            print(f"Avaliações de {materia}:")
            for a in dados["avaliacoes"]:
                print(f"{a['nome']} - Peso: {a['peso']} - Nota: {a['nota']}")
        else:
            print("Matéria não encontrada.")

    elif opcao == "0":
        break

    else:
        print("Opção inválida.")
