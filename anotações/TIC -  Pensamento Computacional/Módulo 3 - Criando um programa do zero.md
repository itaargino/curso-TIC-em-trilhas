#### Aula 1: Código Limpo
Legibilidade, manutenibilidade, escalabilidade, colaboração, reusabilidade, eficiência e corrigível para bugs
1. Dê nomes significativos às coisas!
2. Faça comentários de código de uma forma inteligente!
3. Faça uma formatação amigável!
4. Evite magia!
5. Cada função deve ter somente uma responsabilidade!
6. Mantenha as bibliotecas e dependências do seu projeto atualizadas!
7. Evite código duplicado!
Clean Code: Habilidades Práticas do Agile Software

#### Questão desafio: A Lista de Compras  

Imagine que um cliente contrata você para criar uma aplicação de lista de compras simples. Essa lista deverá ter uma série de funcionalidades que precisam ser implementadas e que, ao final, deverá permitir que o usuário manipule os produtos na lista. Portanto, você precisará elencar o que será necessário para que a lista seja implementada, de acordo com as necessidades do cliente, utilizando seus conhecimentos em programação e implementá-las utilizando Python.

**Para realizar este desafio você precisar ter noção dos seguintes conceitos:** 

- Laços de repetição; 
- Condicionais; 
- Entrada e saída de dados; 
- Manipulação de listas, dicionários e strings; 

**Objetivo do desafio:**Desenvolver um aplicativo que gerencie uma lista de compras que permita adicionar, remover e listar os produtos adicionados nela. 
**Para isso, o seu aplicativo precisa ter as seguintes funcionalidades:** 

1. **Menu de Opções:** O sistema deve fornecer um menu de opções para o usuário interagir. As opções devem ser as seguintes:    
    1. Adicionar produto
    2. Remover produto
    3. Pesquisar produtos
    4. Sair do programa  
2. **Adicionar Produto:** O usuário deve poder adicionar um novo produto à lista de compras. O sistema deve solicitar informações sobre o nome, unidade de medida, quantidade e descrição do produto. As opções de unidade devem ser:  
    1. Quilograma
    2. Grama
    3. Litro
    4. Mililitro
    5. Unidade
    6. Metro
    7. Centímetro     
    **Essas opções devem aparecer quando o sistema perguntar a unidade de medida.**  
        
3. **Controle de ID Automático:** O sistema deve atribuir automaticamente um ID único para cada produto adicionado à lista.
4. **Remover Produto:** O usuário deve poder remover um produto da lista com base ID do produto. O sistema deve solicitar o ID do produto que o usuário deseja remover.
5. **Pesquisar Produtos por Nome:** O usuário deve poder pesquisar produtos na lista com base no nome ou parte do nome. O sistema deve exibir os resultados correspondentes e fornecer a contagem total de produtos encontrados.
6. **Listar Todos os Produtos:** O sistema deve ser capaz de exibir todos os produtos presentes na lista de compras, se houver. Contudo, o menu não deve mostrar uma opção de “Listar produtos”. A exibição deverá ocorrer toda vez que o menu principal for executado, acima dele.
7. **Cabeçalho do Aplicativo:** Deve ser exibido um cabeçalho ao iniciar o aplicativo para fornecer uma saudação e indicar que é uma Lista de Compras Simples.
8. **Feedback de Ação:** Após a execução de uma ação (como adicionar ou remover um produto), o sistema deve fornecer feedback indicando o resultado da ação.
9. **Tratamento de Entradas Inválidas:** O sistema deve ser capaz de lidar com entradas inválidas do usuário e fornecer mensagens de erro apropriadas para orientar o usuário.
10. **Encerramento do Programa:** O usuário deve poder encerrar o programa de forma adequada, escolhendo a opção de saída no menu.