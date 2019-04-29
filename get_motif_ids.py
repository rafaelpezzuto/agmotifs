import sys

arq = open(sys.argv[1])

dados = [a.strip().split('\t') for a in arq]

motifs_ids = sorted(set([int(a[1]) for a in dados]))

print(motifs_ids)
