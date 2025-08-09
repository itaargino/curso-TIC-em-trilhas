from utils import carregar_dados, salvar_dados

def criar_materia(nome, avaliacoes):
    dados = carregar_dados()
    if nome in dados["materias"]:
        print("Matéria já existe.")
        return
    dados["materias"][nome] = {"avaliacoes": avaliacoes}
    salvar_dados(dados)
    print(f"Matéria '{nome}' criada com sucesso.")

def editar_nota(materia, nome_avaliacao, nova_nota):
    dados = carregar_dados()
    avaliacoes = dados["materias"].get(materia, {}).get("avaliacoes", [])
    for a in avaliacoes:
        if a["nome"] == nome_avaliacao:
            a["nota"] = nova_nota
            salvar_dados(dados)
            print(f"Nota atualizada em '{materia}' → {nome_avaliacao}: {nova_nota}")
            return
    print("Avaliação não encontrada.")

def listar_materias():
    dados = carregar_dados()
    return list(dados["materias"].keys())

def obter_dados_materia(nome):
    dados = carregar_dados()
    return dados["materias"].get(nome)
