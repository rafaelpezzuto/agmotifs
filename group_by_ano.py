import sys
import os

sys.path.append('../aglattes/')
from models.lattes import Lattes, Relacao


def obtain_interval_edges(min_year: int):
    interval_edges = []
    for i in range(min_year, min_year + INTERVALO):
        for e in ARESTAS_POR_ANO.get(str(i), []):
            interval_edges.append(e)
    return interval_edges


def sort_edges(edges: list):
    return sorted(sorted(edges, key=lambda x:int(x.split(' ')[1])), key=lambda x:int(x.split(' ')[0]))


def write_subgraph(subgraph: list, min_year: int, path: str):
    file_path = path + str(min_year) + '.txt'
    out = open(file_path, 'w')
    for i in subgraph:
        out.write(i + '\n')
    out.close()


ARQUIVO_GRAFO = '/home/rafael/aglattes-testing/grafo.gdf'
PASTA_RESULTADOS = '/home/rafael/aglattes-testing/subgrafos/anos/'
INTERVALO = 5
os.mkdir(PASTA_RESULTADOS)

print('Lendo dados do passo anterior')
temp_vertices = []
temp_arestas = []
arq_grafo = open(ARQUIVO_GRAFO)

for line in arq_grafo:
    elementos = line.strip().split(',')
    if len(elementos) == 30:
        temp_vertices.append(line.strip())
    elif len(elementos) == 13:
        temp_arestas.append(line.strip())
    else:
        print('linha invalida: %s' % line.strip())

VERTICES = []
header_vertices = [i.split(' ')[0] for i in temp_vertices.pop(0).strip().split(',')]
header_vertices[0] = 'id_lattes'
header_vertices[1] = 'nome'
for n in temp_vertices:
    attributes = n.split(',')
    dargs = {}
    for i, na in enumerate(attributes):
        dargs[header_vertices[i]] = attributes[i]
    v = Lattes(**dargs)
    VERTICES.append(v)

ARESTAS = []
header_arestas = [i.split(' ')[0] for i in temp_arestas.pop(0).strip().split(',')]
header_arestas[0] = 'origem_id_lattes'
for n in temp_arestas:
    attributes = n.split(',')
    dargs = {}
    for i, na in enumerate(attributes):
        dargs[header_arestas[i]] = attributes[i]
    a = Relacao(**dargs)
    ARESTAS.append(a)
arq_grafo.close()

ARESTAS_POR_ANO = {}
for a in ARESTAS:
    if a.ano_conclusao not in ARESTAS_POR_ANO:
        ARESTAS_POR_ANO[a.ano_conclusao] = [a]
    else:
        ARESTAS_POR_ANO[a.ano_conclusao].append(a)

max_year = int(max(ARESTAS_POR_ANO.keys()))
min_year = int(min(ARESTAS_POR_ANO.keys()))

for i in range(min_year, max_year, INTERVALO):
    subgraph_edges = obtain_interval_edges(i)

    subgraph_nodes = set()
    for e in subgraph_edges:
        subgraph_nodes.add(e.origem_id_lattes)
        subgraph_nodes.add(e.destino_id_lattes)

    counter = 1
    d_nodes = {}
    for n in subgraph_nodes:
        d_nodes[n] = counter
        counter += 1

    new_edges = []

    for e in subgraph_edges:
        new_edge = ' '.join([str(d_nodes[e.origem_id_lattes]), str(d_nodes[e.destino_id_lattes]), '1'])
        new_edges.append(new_edge)

    write_subgraph(sort_edges(new_edges), i, PASTA_RESULTADOS)
