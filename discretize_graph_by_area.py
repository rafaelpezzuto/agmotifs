import unicodedata


def remove_accents(text: str):
    result = []
    for c in text:
        result.append(unicodedata.normalize('NFKD', str(c))[0])
    return ''.join(result)


arestas = [o.strip().split(',') for o in open('/mnt/dados/massive/dataset-2017-08-doutores/arestas.csv')]
vertices = [o.strip().split(',') for o in open('/mnt/dados/massive/dataset-2017-08-doutores/vertices.csv')]

grandes_areas = {}
areas = {}

for v in vertices[1:]:
    a = remove_accents(v[4]).title().replace(' ', '').replace(';', '')
    if a not in areas.keys():
        areas[a] = [v[0]]
    else:
        areas[a].append(v[0])

    ga = remove_accents(v[3]).title().replace(' ', '')
    if ga not in grandes_areas.keys():
        grandes_areas[ga] = [v[0]]
    else:
        grandes_areas[ga].append(v[0])
         
del areas['']
for a in areas:
    areas[a] = set(areas[a])

del grandes_areas['']
for ga in grandes_areas:
    grandes_areas[ga] = set(grandes_areas[ga])

import os
os.mkdir('areas_flex')           
os.mkdir('areas_rigor')         
os.mkdir('grandes_areas_rigor')
os.mkdir('grandes_areas_flex')  
                       
for a in areas:
    counter = 1
    d_nodes = {}
    nodes = areas.get(a)
    out = open('areas_flex/' + a + '.txt', 'w')
    nodes_area = set()
    arestas_area = []
    for e in arestas[1:]:
        if e[0] in nodes or e[1] in nodes:
            arestas_area.append(e)
            nodes_area.add(e[0])
            nodes_area.add(e[1])
    d_nodes = {}
    counter = 1
    for n in nodes_area:
        d_nodes[n] = counter
        counter += 1
    sorted_arestas = sorted(sorted(arestas_area, key=lambda x:int(d_nodes[x[1]])), key=lambda x:int(d_nodes[x[0]]))
    for e in sorted_arestas:
        if e[0] in nodes_area or e[1] in nodes_area:
            out.write(' '.join([str(d_nodes[e[0]]), str(d_nodes[e[1]]), '1']))
            out.write('\n')
            
for a in areas:
    counter = 1
    d_nodes = {}
    nodes = areas.get(a)
    out = open('areas_rigor/' + a + '.txt', 'w')
    nodes_area = set()
    arestas_area = []
    for e in arestas[1:]:
        if e[0] in nodes and e[1] in nodes:
            arestas_area.append(e)
            nodes_area.add(e[0])
            nodes_area.add(e[1])
    d_nodes = {}
    counter = 1
    for n in nodes_area:
        d_nodes[n] = counter
        counter += 1
    sorted_arestas = sorted(sorted(arestas_area, key=lambda x:int(d_nodes[x[1]])), key=lambda x:int(d_nodes[x[0]]))
    for e in sorted_arestas:
        if e[0] in nodes_area or e[1] in nodes_area:
            out.write(' '.join([str(d_nodes[e[0]]), str(d_nodes[e[1]]), '1']))
            out.write('\n')
            
for a in grandes_areas:
    counter = 1
    d_nodes = {}
    nodes = grandes_areas.get(a)
    out = open('grandes_areas_rigor/' + a + '.txt', 'w')
    nodes_area = set()
    arestas_area = []
    for e in arestas[1:]:
        if e[0] in nodes and e[1] in nodes:
            arestas_area.append(e)
            nodes_area.add(e[0])
            nodes_area.add(e[1])
    d_nodes = {}
    counter = 1
    for n in nodes_area:
        d_nodes[n] = counter
        counter += 1
    sorted_arestas = sorted(sorted(arestas_area, key=lambda x:int(d_nodes[x[1]])), key=lambda x:int(d_nodes[x[0]]))
    for e in sorted_arestas:
        if e[0] in nodes_area or e[1] in nodes_area:
            out.write(' '.join([str(d_nodes[e[0]]), str(d_nodes[e[1]]), '1']))
            out.write('\n')
            
for a in grandes_areas:
    counter = 1
    d_nodes = {}
    nodes = grandes_areas.get(a)
    out = open('grandes_areas_flex/' + a + '.txt', 'w')
    nodes_area = set()
    arestas_area = []
    for e in arestas[1:]:
        if e[0] in nodes or e[1] in nodes:
            arestas_area.append(e)
            nodes_area.add(e[0])
            nodes_area.add(e[1])
    d_nodes = {}
    counter = 1
    for n in nodes_area:
        d_nodes[n] = counter
        counter += 1
    sorted_arestas = sorted(sorted(arestas_area, key=lambda x:int(d_nodes[x[1]])), key=lambda x:int(d_nodes[x[0]]))
    for e in sorted_arestas:
        if e[0] in nodes_area or e[1] in nodes_area:
            out.write(' '.join([str(d_nodes[e[0]]), str(d_nodes[e[1]]), '1']))
            out.write('\n')