import json
import os

CAMINHO_JSON = "notas.json"

def carregar_dados():
    if not os.path.exists(CAMINHO_JSON):
        return {"materias": {}}
    with open(CAMINHO_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(CAMINHO_JSON, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


calcular_media(materia: dict)