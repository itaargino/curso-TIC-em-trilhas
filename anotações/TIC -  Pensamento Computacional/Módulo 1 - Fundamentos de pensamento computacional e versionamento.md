Data: 04-08-2025
Horário: 12:34
#### Aula 1: Back-end, front-end e mobile
**Front-end**: ponta da frente sendo a interface, construída em CSS  (cor e forma) e HTML (limites físicos do site) e Javascript (ações importantes do site).
**Back-end**: responsável por recursos externos do ambiente do site, faz a checagem do funcionamento do front e comunica
**Mobile**: interações mais integralizadas, aproximando ainda mais o frontend e o backend

#### Aula 2: Cientista, analista e engenheiro de dados
**Engenheiro de dados**: coletar, limpar e preparar os dados, SQL ( para consultar banco de dados), Spark ( para big data) e Python ( para processos ETL (Extrair, Transformar, Carregar) é um procedimento que extrai dados de diversas fontes)
**Cientista de dados**: cria soluções usando os dados produzidos pelos engenheiros, trabalhando com estatística e machine learning. Python e R (para usar aprendizado de máquina)
**Analista de dados**: recebe as soluções e as torna digerível ao público geral ( através de gráficos, dashboards) com ferramentas como Tableau e Power BI que são duas ferramentas populares de análise e visualização de dados.

#### Aula 3: DevOps
Desenvolvimento + Operações
**O que é**:
visa melhorar processos e comunicação entre equipes, automatizando máximo de tarefas possível buscando resolver erros de maneira rápida e eficiente.

**Failfast:** é uma filosofia que incentiva a rápida identificação e correção de erros em projetos, produtos ou processos, especialmente no contexto de desenvolvimento de software e startups.

#### Aula 4: Dicionário do programador
## A

- **Algoritmo:** É uma sequência de passos que seguimos para resolver um problema.    
- **API (Interface de Programação de Aplicações):** São regras que ajudam diferentes programas a conversarem entre si.  

## B

- **Backlog:** É uma lista de tarefas que ainda precisamos fazer em nosso projeto.   
- **Banco de dados:** É onde armazenamos nossas informações de forma organizada para que possamos acessá-las e modificá-las facilmente.  

## C

- **Cache:** É como uma memória temporária que o computador usa para guardar informações que ele acessa muito frequentemente.     
- **Code Review:** É quando colegas revisam nosso código para ajudar a encontrar erros e melhorar a qualidade do que fizemos.  

## D

- **Dashboard:** É uma tela que mostra informações importantes de um jeito fácil de entender.  
- **Debug:** Fazer um debug é quando procuramos e corrigimos os erros que nosso programa tem (de modo coloquial dito como Debugar).     
- **Dependências:** É algo que o programa precisa para funcionar corretamente, como blocos de Lego que você precisa para construir algo. Sem esses blocos, o programa pode não funcionar como esperado.       
- **Diretório:** É uma forma de organizar arquivos e pastas em nosso computador.  

## F

- **Framework:** É como uma caixa de ferramentas pré-montada que os programadores usam para construir sites ou aplicativos. Ela já vem com algumas peças prontas, economizando tempo e esforço. 

## L

- **Linguagem compilada:** É quando transformamos nosso código em instruções que o computador entende antes de executá-lo.    
- **Linguagem de alto nível:** É como falar com o computador usando palavras que entendemos, facilitando a escrita e leitura do código.    
- **Linguagem de baixo nível:** É como falar com o computador usando uma linguagem que ele entende diretamente, mais próxima do jeito que o computador "pensa".     
- **Linguagem interpretada:** É quando o computador lê e executa o código linha por linha, sem transformá-lo em algo que só ele entenda antes. 

## M

- **Merge:** Fazer um merge significa juntar as mudanças que fizemos em diferentes partes do nosso projeto (de modo coloquial dito como Mergear).     
- **MVP (Minimum Viable Product****):** É a versão básica de um produto que tem só o que é mais importante para funcionar.    

## P

- **POC (Proof of** **Concept):** É uma primeira versão de um projeto que fazemos para testar se a ideia é viável.

## S

- **Sistema legado:** É um sistema antigo que ainda é usado mesmo com o surgimento de tecnologias mais novas.     
- **Sistema local:** É tudo que um computador pode fazer por conta própria, como um mundo pequeno dentro dele mesmo, sem precisar da internet ou de outros computadores.   
- **Stack:** É como um conjunto de ferramentas que usamos juntas para construir um programa ou aplicativo.

#### Aula 6: Configurando o ambiente
ola mundo

#### Aula 7: O que é Git/Github
**Controle de versão**: capaz de retornar versões anteriores para que não colapse, também consegue modularizar o trabalho para certa versão possibilitando merges futuros
**Git**: plataforma responsável por realizar esse controle de versões
**Github**: rede social de códigos para facilitar a colaboração, centralizando tudo na nuvem facilitando a organização. Permite que:
- faça atualizações
- reporte erros
- corrija erros
- sugira alterações

#### Aula 8: Fluxo de desenvolvimento
`git status` para checar a branch atual
`git switch -c nova_branch` cria nova branch
`git add` define quem irá entrar na próxima revisão do código
`git add .` adiciona todos
`git commit -m "Teste"` usado para subir para a revisão
`git push origin nova_branch` faz a publicação da atualização do código ( usando a branch)
Abre um pull & request (prs) no Github onde poderá ser revisto, comparado e sugerir mudanças

#### Aula 9: Resolvendo conflitos no github
`git fetch` pega as informações da branch, mas não substitui como no pull
...

#### Aula 10: Readme
Basicamente servindo como um banner para o projeto

#### Extras
**Git Cherry Pick**: O `git cherry-pick` é um comando que permite copiar um commit específico de uma branch para outra, sem precisar fazer merge ou rebase. Ele é útil para trazer correções sem afetar código inacabado. Para usá-lo, basta rodar `git cherry-pick <ID do commit>` na branch de destino


