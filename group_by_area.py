import os
import sys
import unicodedata

sys.path.append('../aglattes/')
from models.lattes import Lattes, Relacao


def remove_accents(text: str):
    result = []
    for c in text:
        result.append(unicodedata.normalize('NFKD', str(c))[0])
    return ''.join(result)


def obtain_subgraph_edges(scope: str, field: str, mode: str):
    subgraph_edges = []
    nodes = []

    if scope == 'areas':
        nodes = AREAS.get(field)
    elif scope == 'grandes-areas':
        nodes = GRANDES_AREAS.get(field)

    field_nodes = set()
    field_edges = []
    for e in ARESTAS:
        if mode == 'flex':
            if e.origem_id_lattes in nodes or e.destino_id_lattes in nodes:
                field_edges.append(e)
                field_nodes.add(e.origem_id_lattes)
                field_nodes.add(e.destino_id_lattes)
        elif mode == 'rigor':
            if e.origem_id_lattes in nodes and e.destino_id_lattes in nodes:
                field_edges.append(e)
                field_nodes.add(e.origem_id_lattes)
                field_nodes.add(e.destino_id_lattes)

    counter = 1
    d_nodes = {}
    for n in field_nodes:
        d_nodes[n] = counter
        counter += 1

    for e in field_edges:
        if mode == 'flex':
            if e.origem_id_lattes in field_nodes or e.destino_id_lattes in field_nodes:
                new_edge = ' '.join([str(d_nodes[e.origem_id_lattes]), str(d_nodes[e.destino_id_lattes]), '1'])
                subgraph_edges.append(new_edge)
        elif mode == 'rigor':
            if e.origem_id_lattes in field_nodes and e.destino_id_lattes in field_nodes:
                new_edge = ' '.join([str(d_nodes[e.origem_id_lattes]), str(d_nodes[e.destino_id_lattes]), '1'])
                subgraph_edges.append(new_edge)
    return subgraph_edges


def sort_edges(edges: list):
    return sorted(sorted(edges, key=lambda x:int(x.split(' ')[1])), key=lambda x:int(x.split(' ')[0]))


def write_subgraph(subgraph: list, scope: str, mode: str, name: str, path: str):
    file_path = '/'.join([path, scope, mode, name]) + '.txt'
    out = open(file_path, 'w')
    for i in subgraph:
        out.write(i + '\n')
    out.close()


ARQUIVO_GRAFO = '/home/rafael/aglattes-testing/grafo.gdf'
PASTA_RESULTADOS = '/home/rafael/aglattes-testing/subgrafos/'

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

vertices = []
header_vertices = [i.split(' ')[0] for i in temp_vertices.pop(0).strip().split(',')]
header_vertices[0] = 'id_lattes'
header_vertices[1] = 'nome'
for n in temp_vertices:
    attributes = n.split(',')
    dargs = {}
    for i, na in enumerate(attributes):
        dargs[header_vertices[i]] = attributes[i]
    v = Lattes(**dargs)
    vertices.append(v)

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


GRANDES_AREAS = {}
AREAS = {}

for v in vertices:
    area = remove_accents(v.primeira_area).title().replace(' ', '').replace(';', '')
    if area != '':
        if area not in AREAS.keys() and area != '':
            AREAS[area] = set([v.id_lattes])
        else:
            AREAS[area].add(v.id_lattes)

    grande_area = remove_accents(v.primeira_grande_area).title().replace(' ', '')
    if grande_area != '':
        if grande_area not in GRANDES_AREAS.keys():
            GRANDES_AREAS[grande_area] = set([v.id_lattes])
        else:
            GRANDES_AREAS[grande_area].add(v.id_lattes)
         

os.mkdir(PASTA_RESULTADOS)
os.mkdir(PASTA_RESULTADOS + 'areas/')
os.mkdir(PASTA_RESULTADOS + 'areas/' + '/flex')
os.mkdir(PASTA_RESULTADOS + 'areas/' + '/rigor')

os.mkdir(PASTA_RESULTADOS + 'grandes-areas/')
os.mkdir(PASTA_RESULTADOS + 'grandes-areas/' + '/flex')
os.mkdir(PASTA_RESULTADOS + 'grandes-areas/' + '/rigor')
                       
for a in AREAS:
    subgraph_edges_area_flex = obtain_subgraph_edges('areas', a, 'flex')
    write_subgraph(sort_edges(subgraph_edges_area_flex), 'areas', 'flex', a, PASTA_RESULTADOS)

    subgraph_edges_area_rigor = obtain_subgraph_edges('areas', a, 'rigor')
    write_subgraph(sort_edges(subgraph_edges_area_rigor), 'areas', 'rigor', a, PASTA_RESULTADOS)

for ga in GRANDES_AREAS:
    subgraph_edges_grande_area_flex = obtain_subgraph_edges('grandes-areas', ga, 'flex')
    write_subgraph(sort_edges(subgraph_edges_grande_area_flex), 'grandes-areas', 'flex', ga, PASTA_RESULTADOS)

    subgraph_edges_grande_area_rigor = obtain_subgraph_edges('grandes-areas', ga, 'rigor')
    write_subgraph(sort_edges(subgraph_edges_grande_area_rigor), 'grandes-areas', 'rigor', ga, PASTA_RESULTADOS)    
