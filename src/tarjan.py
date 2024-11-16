from collections import defaultdict
import os
import csv

# Esta classe representa um grafo nao-direcionado
# usando representacao de lista de adjacencia
class Graph:

    def __init__(self):
        self.graph = defaultdict(list) # dicionario padrao para armazenar o grafo
        self.Time = 0

    # funcao para adicionar uma aresta ao grafo
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    '''Uma funcao recursiva que encontra pontos de articulacao
    usando a travessia em profundidade (DFS)
    u --> O vertice a ser visitado em seguida
    visited[] --> mantem o controle dos vertices visitados
    disc[] --> Armazena os tempos de descoberta dos vertices visitados
    parent[] --> Armazena vertices pais na arvore DFS 
    ap[] --> Armazena pontos de articulacao'''
    def APUtil(self, u, visited, ap, parent, low, disc):

        # Contagem de filhos no vertice atual
        children = 0

        # Marca o vertice atual como visitado
        visited[u] = True

        # Inicializa o tempo de descoberta e o valor de menor alcance
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        # Recorre para todos os vertices adjacentes a este vertice
        for v in self.graph[u]:
            # Se v ainda nao foi visitado, se torna filho de u
            # na arvore DFS e chama a recursao para ele
            if not visited[v]:
                parent[v] = u
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc)

                # Verifica se a subarvore enraizada em v tem uma conexao com
                # um dos ancestrais de u
                low[u] = min(low[u], low[v])

                # u e um ponto de articulacao nos seguintes casos
                # (1) u e a raiz da arvore DFS e possui dois ou mais filhos.
                if parent[u] is None and children > 1:
                    ap[u] = True

                # (2) Se u nao e a raiz e o valor de menor alcance de um de seus filhos
                # e maior que o valor de descoberta de u.
                if parent[u] is not None and low[v] >= disc[u]:
                    ap[u] = True

            # Atualiza o valor de menor alcance de u para chamadas de funcao pai
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    # A funcao para fazer a travessia DFS. Usa a funcao recursiva APUtil()
    def AP(self):

        # Marca todos os vertices como nao visitados
        # e inicializa as listas parent e visited,
        # e a lista ap (ponto de articulacao)
        visited = {v: False for v in self.graph}
        disc = {v: float("Inf") for v in self.graph}
        low = {v: float("Inf") for v in self.graph}
        parent = {v: None for v in self.graph}
        ap = {v: False for v in self.graph}

        # Chama a funcao auxiliar recursiva
        # para encontrar pontos de articulacao
        # na arvore DFS enraizada no vertice 'i'
        for v in self.graph:
            if not visited[v]:
                self.APUtil(v, visited, ap, parent, low, disc)

        # Imprime os pontos de articulacao
        for v, is_ap in ap.items():
            if is_ap:
                print(v, end=" ")

    def ler_csv_para_grafo(self, nome_arquivo):
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            leitor = csv.reader(arquivo_csv)
            for linha in leitor:
                origem, destino, _ = linha
                self.addEdge(origem, destino)

print('\n\n')
g = Graph()
nome_arquivo = 'conexoes_sudeste.csv'
g.ler_csv_para_grafo(nome_arquivo)
g.AP()
print('\n\n')