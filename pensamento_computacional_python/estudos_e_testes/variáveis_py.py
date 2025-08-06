# --- Tipos Primitivos ---
print("--- Tipos Primitivos ---")

# int: para números inteiros
idade = 30
print(f"Variável 'idade' | Valor: {idade} | Tipo: {type(idade)}")

# float: para números com ponto flutuante (decimais)
altura = 1.75
print(f"Variável 'altura' | Valor: {altura} | Tipo: {type(altura)}")

# bool: para valores lógicos (Verdadeiro ou Falso)
tem_permissao = True
print(f"Variável 'tem_permissao' | Valor: {tem_permissao} | Tipo: {type(tem_permissao)}")

print("\n" + "="*40 + "\n")

# --- Tipos Compostos ---
print("--- Tipos Compostos ---")

# str (string): para sequências de caracteres (texto)
nome_completo = "Carlos Silva"
primeira_letra = "C" # Em Python, um caractere é uma string de tamanho 1
print(f"Variável 'nome_completo' | Valor: '{nome_completo}' | Tipo: {type(nome_completo)}")

# list: coleção ordenada e mutável de itens. Pode conter tipos diferentes.
lista_de_compras = ["maçã", "banana", "leite", 500]
print(f"Variável 'lista_de_compras' | Valor: {lista_de_compras} | Tipo: {type(lista_de_compras)}")

# tuple: coleção ordenada e IMUTÁVEL de itens.
coordenadas_gps = (-23.5505, -46.6333)
print(f"Variável 'coordenadas_gps' | Valor: {coordenadas_gps} | Tipo: {type(coordenadas_gps)}")

# dict (dicionário): coleção não ordenada de pares chave-valor.
dados_usuario = {"id": 101, "nome": "Ana", "ativo": True}
print(f"Variável 'dados_usuario' | Valor: {dados_usuario} | Tipo: {type(dados_usuario)}")

# set: coleção não ordenada de itens ÚNICOS.
numeros_da_sorte = {7, 13, 22, 7, 42, 13}
print(f"Variável 'numeros_da_sorte' | Valor: {numeros_da_sorte} | Tipo: {type(numeros_da_sorte)}")
