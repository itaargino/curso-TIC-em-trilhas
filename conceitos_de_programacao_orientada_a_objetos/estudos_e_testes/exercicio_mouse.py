#Chegou o momento de você colocar em prática os seus conhecimentos. 
# Crie uma classe Mouse com os seguintes atributos privados:
#- cor
#- qtd_botoes.
#
#O construtor desta classe deverá receber como parâmetros os respectivos valores para instanciá-los.
#Escreva também os métodos getters e setters para esses atributos utilizando o decorador property.

class Mouse:
    def __init__(self, cor, qtd_botoes):
        self.__cor = cor
        self.__qtd_botoes = qtd_botoes
    
    @property
    def cor(self):
        return self.__cor

    @property
    def qtd_botoes(self):
        return self.__qtd_botoes
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor
    
    @qtd_botoes.setter
    def qtd_botoes(self, qtd_botoes):
        self.__qtd_botoes = qtd_botoes

    