#### Aula 1 - Herança
A herança é um conceito  que permite a criação de uma nova classe a partir de uma classe
existente. 
A nova classe recebe o nome de classe derivada ou subclasse ou ainda classe filha, e a classe da qual ela é construída chamada de classe base ou superclasse ou classe mãe.

#### Aula 2 - Super Classe
![[Pasted image 20250811204729.png]]
![[Pasted image 20250811204751.png]]

#### Aula 3 - Polimorfismo
É a utilização de métodos pré-estabelecidos na classe mãe que podem ser herdados que realizam outras ações
Ou seja, mesmo que que o nome dos métodos sejam os mesmos suas funções serão dadas individualmente dependendo da sua instância

#### Aula 4 - Interface
É uma classe usada por outras classes, que possuem métodos completamente ocos e nenhum método construtor

#### Aula 5 - Métodos Abstratos
Um método abstrato é um método que é declarado na superclasse (ou interface) e que deve ser implementado nas subclasses.
Em Python, métodos abstratos são criados usando o módulo abc (Abstract Base Classes) e a função decoradora `@abstractmethod`.
Métodos abstratos são úteis porque permitem que você defina um “contrato” que todas as subclasses devem seguir.

#### Aula 6 - Métodos Estáticos
Métodos que não dependem de uma instância para serem chamados
Métodos que não podem acessar variáveis de instância diretamente
