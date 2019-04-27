import os
import sys


DIR_SOURCES =  sys.argv[1]
IN_FILES = ['/'.join([DIR_SOURCES, f]) for f in os.listdir(DIR_SOURCES)]

for f in sorted(IN_FILES):
    fi = open(f)
    while True:
        line = fi.readline()
        if line == '':
            break
        if 'Full list includes' in line:
            number_of_motifs = int(line.strip().split(' ')[3])
            group = f.split('/')[-1].split('.')[0]
            readed = 0
            while True:
                motif_line = fi.readline().strip()
                if 'Full list of subgraphs size' in motif_line:
                    break
                motif_line = motif_line.split('\t')
                if len(motif_line) > 1:
                    if motif_line[0].isdigit():
                        readed += 1
                        print('\t'.join([group] + motif_line))
                if readed == number_of_motifs:
                    break
    fi.close()
