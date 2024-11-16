from csv import reader
from pprint import pprint
from math import inf

'''
Arquivo de código que encontra a árvore geradora mínima dado
um arquivo csv de cidades no seguinte formato:
    
    Cidade_a,Cidade_b,Peso
    Cidade_a,Cidade_c,Peso
             ...
    Cidade_y,Cidade_z,Peso

O arquivo deve estar na codificação utf-8 e salvo em formato .csv
'''

def pegar_peso(cidade_1, cidade_2):
    '''
    Retorna o peso das arestas do dicionário `pesos`.
    Verifica as duas variações.
    '''
    try:
        return pesos[cidade_1 + "_" + cidade_2]
    except:
        try:
            return pesos[cidade_2 + "_" + cidade_1]
        except:
            return inf

def prim(n, s):
    vertices_adicionados = []
    for i in range(n):
        vertices_adicionados.append(0)
    vertices_adicionados[s] = 1
    arestas = []
    while len(arestas) < (n - 1):
        menor_peso = inf
        aresta_a_adicionar = []
        vertice_a_adicionar = None
        for i in range(n):
            if vertices_adicionados[i] == 1:
                for k in range(n):
                    peso = pegar_peso(numero_para_nome[i+1], numero_para_nome[k+1])
                    if (vertices_adicionados[k] == 0 and peso < menor_peso):
                        vertice_a_adicionar = k
                        aresta_a_adicionar = [i+1, k+1]
                        menor_peso = peso
        if vertice_a_adicionar != None:
            vertices_adicionados[vertice_a_adicionar] = 1
            arestas.append([aresta_a_adicionar, menor_peso])
    return arestas

# Dicionarios de relações: nome -> número
numero_para_nome = {}
nome_para_numero = {}
# Dicionário contendo as arestas
grafo = {}
# Dicionário contendo o peso de cada aresta
pesos = {}

# Lê o arquivo
with open("../data/conexoes_sudeste.csv", mode="r", encoding="utf-8") as arquivo:
    texto = reader(arquivo, delimiter=",")
    pos = 1
    for linha in texto:
        if linha[0] not in numero_para_nome.values():
            # Dicionários para conversão de índices dos vértices
            # de strings para inteiros
            nome_para_numero[linha[0]] = pos
            numero_para_nome[pos] = linha[0]
            pos += 1
        if linha[1] not in numero_para_nome.values():
            # Dicionários para conversão de índices dos vértices
            # de strings para inteiros
            nome_para_numero[linha[1]] = pos
            numero_para_nome[pos] = linha[1]
            pos += 1
        try:
            grafo[linha[0]].append(linha[1])
        except:
            grafo[linha[0]] = [linha[1]]
        aresta = linha[0] + "_" + linha[1]
        pesos[aresta] = int(linha[2])

# Pega a aresta que possui o menor valor
min = ["", inf]
for chave, valor in pesos.items():
    if (valor < min[1]):
        min[0] = chave
        min[1] = valor

# Pega o primeiro vértice da aresta de menor valor e
# pega seu referente em número do dicionário
primeira_aresta = min[0].split("_")
vert_inicial = nome_para_numero[primeira_aresta[0]]

tamanho = len(nome_para_numero)

arvore_em_numeros = prim(len(nome_para_numero), vert_inicial)

arvore_em_nomes = []
for aresta, peso in arvore_em_numeros:
    arvore_em_nomes.append([[numero_para_nome[aresta[0]], numero_para_nome[aresta[1]]], peso])

print("\nRelação estabelecida [Número: Nome]\n")
pprint(numero_para_nome)
print("\n\nResultado da árvore com vértices em número. Formato: [[V1, V2], peso]\n")
pprint(arvore_em_numeros)
print("\n\nResultado da árvore com vértices em nomes. Formato: [[V1, V2], peso]\n")
pprint(arvore_em_nomes)