import sys
import unicodedata


INVALID_STRINGS = ['programa de', 'posgraduacao em', 'mestrado em', 'mestrado academico em', 'programa de posgraduacao em', 'programa de pos graduacao em', 'doutorado em', 'pos graduacao em']
FILE_GRAFO = sys.argv[1]


def remove_invalid_strings(string):
    for i in INVALID_STRINGS:
        if i in string:
            string = string.replace(i, '')
    return string


def remove_accents(string):
    new_string = ''
    for c in string:
        new_string += unicodedata.normalize('NFKD', c)[0]
    return new_string


def special_fixer(string):
    if string == 'ciencias e tecnologia de materiais':
        return 'ciencia e tecnologia de materiais'
    if string == 'fisica aplicada':
        return 'fisica'
    if string == 'ciencias da computacao' or string == 'computacao aplicada':
        return 'ciencia da computacao'
    if string == 'relazioni internazionali':
        return 'relacoes internacionais'
    return string


vertices = []
arestas = []
for g in [g.strip().split(',') for g in open(FILE_GRAFO)]:
    if len(g) == 30:
        vertices.append(g)
    elif len(g) == 13:
        arestas.append(g)
    else:
        print('LINHA INVALIDA:', g)
        sys.exit(1)

print('VERTICES: %s' % len(vertices))
print('ARESTAS: %s\n' % len(arestas))

cursos = {}
for a in arestas[1:]:
    cs = []
    curso = special_fixer(remove_invalid_strings(remove_accents(a[8]).lower()).strip())
    if curso != '':
        cs.append(curso)

    extras = a[-2].split('#')
    for e in extras:
        if e != '':
            els = e.split(':')
            curso_extra = special_fixer(remove_invalid_strings(remove_accents(els[2]).lower()).strip())
            if curso_extra != '':
                cs.append(curso_extra)

    for c in cs:
        if c not in cursos:
            cursos[c] = set([','.join(a)])
        else:
            cursos[c].add(','.join(a))

for k in sorted(cursos.keys()):
    print(k, len(cursos.get(k)), sep=": ")
