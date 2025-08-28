#### Aula 1 - O que é programação orientada a objetos
**POO** é um paradigma da programação, tem o objetivo de se relacionar à outro objeto.
Para cada objeto teremos métodos diferentes, sendo uma forma de resolver um problema
**Definição**: Um objeto em programação pode ser categorizado, definido por suas características. Ele pode simples ou complexo, 
**Analogia com carro:** Carro é o objeto mas ele pode ser relacionado com objeto pessoa por exemplo
**Por que?** 
- Facilita o raciocínio na hora de pensar no que pode ser feito com o código
- Facilita a manutenção
- Aproximar o código para o mundo real
- Gerencia melhor a memória
	**O que um objeto é na programação:** deriva de um classe (um molde que descreve as propriedades de um objeto)

#### Aula 2 - Classes, métodos e objetos
Uma **classe** é uma estrutura ou um "molde" que define um conjunto de atributos (dados ou características) e métodos (ações ou comportamentos) que podem ser utilizados para criar objetos
**Objetos** são instâncias das classes, ou seja, são as variáveis que você cria a partir do "molde" definido pela classe. Eles possuem as características (atributos) e comportamentos (métodos) definidos pela classe que os originou
**Método** é uma função dentro de uma classe


#### Aula 3 - Variáveis
**Atributos** são as características ou dados que um objeto possui, dois tipos serão explorados:
- **Atributos de classe:** São compartilhados por todos os objetos da classe. São definidos dentro da classe, mas fora de qualquer método. Por exemplo, `especie = "Canino"` na classe `Cachorro` seria um atributo de classe
- **Atributos de instância**: São específicos de cada objeto. São definidos dentro do método especial `__init__()` e seus conteúdos são próprios de cada objeto. Por exemplo, `nome`, `raca` e `tamanho` são atributos de instância

#### Aula 4 - Métodos
**Funções**: composta por palavra reservada (`def`), parâmetros e declaração de retorno (declarado ou não).
Observe que um parâmetro passado numa chamada é nomeado de **argumento**

#### Aula 5 - Métodos e funções em detalhes
Atente-se ao retorno, pois a utilização do função depende desse. Imagine uma mensagem:
```
def mensagem(parametro)
...
return ("exemplo")
```
chamada: `print(mensagem(parametro))`
```
def mensagem(parametro)
...
return print("exemplo")
```
chamada: `mensagem(parametro)`

#### Aula 6 -  Método inicial e palavra self
O **construtor** (`__init__`) é um método especial que é executado quando um objeto é criado, sendo usado para inicializar os atributos do objeto. Temos também class, dir, str...
`self` parâmetro para definir o objeto específico
Atributos de classe usa atributo cls

#### Aula 7 - Exercitando esses conceitos
![[Pasted image 20250808130118.png]]
(código no github)

#### Aula 8 - Encapsulamento
**Encapsular** está ligado com a ideia de proteger os atributos e métodos do objeto. Para termos uma outra camada de proteção (evitarmos que os dados sejam alterados erroneamente) temos um termo chamado **visibilidade**

#### Aula 9 - Visibilidade
A visibilidade é uma forma de informar a acessibilidade de um atributo da classe:
- Pública: pode ser acessado
- Privada: não pode ser acessado
- Restrita: atributo sobre aviso (Python não liga muito pra restrita)

#### Aula 10 - Visibilidade (com exemplos)
Quando um atributo é definido como privado, ele não pode ser acessado ou modificado diretamente de fora da classe. No entanto, muitas vezes é necessário permitir que o dado seja lido ou alterado de forma controlada. É aqui que entram os métodos "getter" (obtém) e "setter" (define/altera)

**Métodos Setter (Ex:** **set_nome****)**:
- Um método setter é usado para **modificar o conteúdo de um atributo privado**

**Métodos Getter (Ex:** **get_nome****)**:
- Um método getter é usado para **obter (visualizar/acessar) o valor de um atributo privado**
Métodos como esses podem ser complexos com outros métodos inseridos formando uma cadeia de execução

#### Aula 11 - Decoradores
![[Pasted image 20250808181312.png]]

#### Aula 12 - Exercício
Nosso abajur tem apenas uma lâmpada e um único botão que é multifuncional. Quando tocado uma vez, acende a lâmpada com intensidade fraca. Quando tocado pela segunda vez, acende a lâmpada com intensidade média. Quando tocado pela terceira vez, acende a lâmpada com intensidade forte. Quando tocado pela quarta vez, apaga a lâmpada. Sempre nesta sequência de toques.

**Sites Recomendados:**

Documentação oficial sobre Python

[https://docs.python.org/pt-br/3/reference/index.html](https://docs.python.org/pt-br/3/reference/index.html)

[Links para um site externo.](https://docs.python.org/pt-br/3/reference/index.html)

Classes

[https://docs.python.org/pt-br/3/tutorial/classes.html](https://docs.python.org/pt-br/3/tutorial/classes.html)

[Links para um site externo.](https://docs.python.org/pt-br/3/tutorial/classes.html)

[https://www.w3schools.com/python/python_classes.asp](https://www.w3schools.com/python/python_classes.asp)

[Links para um site externo.](https://www.w3schools.com/python/python_classes.asp)

Herança

[https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance](https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance)

[Links para um site externo.](https://docs.python.org/pt-br/3/tutorial/classes.html#inheritance)

Método

[https://docs.python.org/pt-br/3/tutorial/classes.html#method-objects](https://docs.python.org/pt-br/3/tutorial/classes.html#method-objects)

[Links para um site externo.](https://docs.python.org/pt-br/3/tutorial/classes.html#method-objects)

Polimorfismo

[https://www.w3schools.com/python/python_polymorphism.asp](https://www.w3schools.com/python/python_polymorphism.asp)

[Links para um site externo.](https://www.w3schools.com/python/python_polymorphism.asp)

Documentação  
[https://wiki.python.org.br/DocumentacaoPython?action=AttachFile&do=view&target=modulo_b.pdf](https://wiki.python.org.br/DocumentacaoPython?action=AttachFile&do=view&target=modulo_b.pdf)

[Links para um site externo.](https://wiki.python.org.br/DocumentacaoPython?action=AttachFile&do=view&target=modulo_b.pdf)