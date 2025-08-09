class Televisao:
    def __init__(self):
            self.marca = "LG"
            self.volume = 0

    def aumentar_volume(self):
        if self.volume < 10:
            self.volume += 1

    def diminuir_volume(self):
        if self.volume > 0:
            self.volume -= 1

    
def controle():
    tv = Televisao()
    print("Controle de TV")
    while True:
        print(f"\nVolume atual: {tv.volume}")
        print("1. Aumentar volume")
        print("2. Diminuir volume")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            tv.aumentar_volume()
        elif opcao == "2":
            tv.diminuir_volume()
        elif opcao == "3":
            print("Saindo do controle.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    controle()