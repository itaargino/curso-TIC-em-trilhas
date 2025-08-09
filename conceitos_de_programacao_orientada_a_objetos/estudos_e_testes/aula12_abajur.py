#Nosso abajur tem apenas uma lâmpada e um único botão que é multifuncional. 
#Quando tocado uma vez, acende a lâmpada com intensidade fraca. 
#Quando tocado pela segunda vez, acende a lâmpada com intensidade média. 
#Quando tocado pela terceira vez, acende a lâmpada com intensidade forte. 
#Quando tocado pela quarta vez, apaga a lâmpada. Sempre nesta sequência de toques.

class Abajur:
    def __init__(self):

        self.__intensidade = 0
        self.__lampada = False

    def __liga_desliga_lampada(self):
        if self.__intensidade > 0:
            self.__lampada = True
        else:
            self.__lampada = False

            
    
    def __controla_intensidade(self):
        if self.__intensidade == 3:
            self.__intensidade = 0
        else:
            self.__intensidade += 1

    def tocar_botao(self):
        if input("Tocar Botão [Enter]") == "":
            return True
        else:
            return False


    def mostrar_status(self):
        print("Intensidade: ", self.__intensidade)
        print("Lâmpada: ", self.__lampada)

    def acionamento(self):
        self.__controla_intensidade()
        self.__liga_desliga_lampada()
    
abajur = Abajur()
while True:
    abajur.mostrar_status()
    if abajur.tocar_botao():
        abajur.acionamento()
    else:
        break
    