import json
from pathlib import Path

def __checar_estado(estado):
    """
    Método privado que verifica se a sigla do estado fornecida é válida, comparando com as siglas de estado do arquivo JSON.

    Args:
        estado (str): A sigla do estado a ser verificada. A sigla deve ter exatamente 2 caracteres.

    Returns:
        str: A sigla do estado, se for válida.

    Exemplo:
        >>> __checar_estado("AC")
        "AC"
    """
    caminho = Path('config/estados-cidades.json')
    lista_estados = []

    with open(caminho, 'r', encoding='utf-8') as arquivo:
        conteudo = json.load(arquivo)
    
        for estado_json in conteudo["estados"]:
            lista_estados.append(estado_json['sigla'])
    
    while True:
        try:
            if estado in lista_estados:
                print(f"{estado} é um estado válido!")
                return estado
            else:
                estado = input(f"{estado} não é um estado valido! Tente novamente: ").strip().upper()
                continue
        except ValueError as e:
            print(e)  
        except Exception as e:
            print("Erro inesperado: ", e)

def inputs_do_usuario():
    """
    Recebe e trata os inputs do usuário para pesquisa no site.
    
    Utiliza a função 'input()' para receber estado e cidade pela entrada do usuário.

    Retorna:
        str: estado, cidade
    """
    estado = input("Digite a sigla do Estado: ").strip().upper()
    estado = __checar_estado(estado)
    return estado