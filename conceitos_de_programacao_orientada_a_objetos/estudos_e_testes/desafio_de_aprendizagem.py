class Copo:
    def __init__(self, capacidade):
        self.capacidade = capacidade

    def encher(self, volume):
        if volume > self.capacidade:
            print("Este volume excede a capacidade do copo.")
        else:
            self.capacidade -= volume
            print("o volume foi adicionado ao copo")
    
class Copo_com_canudo(Copo):
    def __init__(self, capacidade, cor_do_canudo):
        super().__init__(capacidade)
        self.cor_do_canudo = cor_do_canudo

copo1 = Copo(250)
copo1.encher(100)
copo2 = Copo_com_canudo(200, "vermelho")
copo2.encher(250)

# aqui deve aparecer a mensagem “Este volume excede a capacidade do copo.”


        