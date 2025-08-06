def inserir_numeros():
    while True:
        try:
            numero1 = float(input("Digite o primeiro número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

    while True:
        try:
            numero2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
    return numero1, numero2

def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    if numero2 == 0:
        return 'invalido'
    return numero1 / numero2


def menu():
    while True:
        print("Calculadora Simples")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("s. Sair")

        escolha = input("Digite o número da operação desejada ou 's' para sair: ")

        if escolha == 's' or escolha == 'S':
            break

        if escolha not in ['1', '2', '3', '4']:
            print("Opção inválida, por favor tente novamente.")
            continue

        numero1, numero2 = inserir_numeros()

        if escolha == "1":
            resultado = soma(numero1, numero2)
        elif escolha == "2":
            resultado = subtracao(numero1, numero2)
        elif escolha == "3":
            resultado = multiplicacao(numero1, numero2)
        elif escolha == "4":
            resultado = divisao(numero1, numero2)
            if resultado == 'invalido':
                print("Divisão por zero não é permitida.")
                continue


        print(f"Resultado: {resultado}")

    print("\nDesligando calculadora... Agradecemos por usar!")

menu()