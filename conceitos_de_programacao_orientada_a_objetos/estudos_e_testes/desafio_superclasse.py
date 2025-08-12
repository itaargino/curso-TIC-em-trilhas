class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    
    def acelerar(self):
        print("O veículo está acelerando.")
    
    def frear(self):
        print("O veículo está freando.")

class Carro(Veiculo):
    def __init__(self, marca, modelo, num_portas):
        super().__init__(marca, modelo)
        self.num_portas = num_portas
    
    def __str__(self):
        return f"""Marca: {self.marca}
                Modelo: {self.modelo}
                Ano: {self.ano}
                Número de portas: {self.num_portas}"""


    def abrir_porta(self, porta):
        if porta <= self.num_portas and porta > 0:
            print(f"A porta {porta} do carro está aberta.")
        else:
            print("A porta especificada não existe no carro.")
        
    def fechar_porta(self, porta):
        if porta <= self.num_portas and porta > 0:
            print(f"A porta {porta} do carro está fechada")
        else:
            print("A porta especificada não existe no carro.")
    
class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        return f"""Marca: {self.marca}
                Modelo: {self.modelo}
                Tipo: {self.tipo}"""
    
    def cortar_giro(self):
        print("A moto está cortando o giro.")

carro = Carro("Ford", "K", 4)
__spec__(carro)

moto = Moto("Honda", "Bis", "Esportiva")
__spec__(moto)

carro.acelerar()
carro.frear()
carro.abrir_porta(2)
carro.fechar_porta(2)

moto.acelerar()
moto.frear()
moto.cortar_giro()

print(carro)
print(moto)