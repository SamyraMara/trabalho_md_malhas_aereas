import csv
from collections import defaultdict
import heapq
import os

def ler_csv_para_grafo(nome_arquivo):
    grafo = {}
    with open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"md", nome_arquivo), mode='r') as arquivo_csv:
        leitor = csv.reader(arquivo_csv)
        for linha in leitor:
            origem, destino, peso = linha
            peso = int(peso)
            if origem not in grafo:
                grafo[origem] = {}
            if destino not in grafo:
                grafo[destino] = {}
            grafo[origem][destino] = peso
            grafo[destino][origem] = peso  
    return grafo

def dijkstra(grafo, inicio, fim):
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[inicio] = 0
    pq = [(0, inicio)]
    caminho = {inicio: None}
    
    while pq:
        (dist_atual, vertice_atual) = heapq.heappop(pq)
        
        if dist_atual > distancias[vertice_atual]:
            continue
        
        for vizinho, peso in grafo[vertice_atual].items():
            distancia = dist_atual + peso
            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                caminho[vizinho] = vertice_atual
                heapq.heappush(pq, (distancia, vizinho))
                
    caminho_final = []
    passo = fim
    while passo is not None:
        caminho_final.insert(0, passo)
        passo = caminho[passo]
        
    return distancias[fim], caminho_final


# Usando as funções
filepath = 'conexoes_sudeste.csv'
grafo = ler_csv_para_grafo(filepath)
inicio, fim = 'AREALVA', 'CABO FRIO'
print('\n')
custo, caminho = dijkstra(grafo, inicio, fim)
print(f"O menor caminho de {inicio} para {fim} é: {caminho} com um custo de {custo}")
print('\n')
inicio, fim = 'RIO DE JANEIRO', 'CABO FRIO'
custo, caminho = dijkstra(grafo, inicio, fim)
print(f"O menor caminho de {inicio} para {fim} é: {caminho} com um custo de {custo}")
print('\n')
inicio, fim = 'VARGINHA', 'RIBEIRÃO PRETO'
custo, caminho = dijkstra(grafo, inicio, fim)
print(f"O menor caminho de {inicio} para {fim} é: {caminho} com um custo de {custo}")
print('\n')
inicio, fim = 'ARAÇATUBA', 'VITÓRIA'
custo, caminho = dijkstra(grafo, inicio, fim)
print(f"O menor caminho de {inicio} para {fim} é: {caminho} com um custo de {custo}")
print('\n')