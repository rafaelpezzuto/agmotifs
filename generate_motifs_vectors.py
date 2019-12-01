import os
import sys


DIR_SOURCES = sys.argv[1]
IN_FILES = ['/'.join([DIR_SOURCES, f]) for f in os.listdir(DIR_SOURCES) if f.endswith('.tsv')]

files = {}
for f in sorted(IN_FILES):
    table_motifs = [i.strip().split('\t') for i in open(f)]
    fields = {}
    motifs_ids = set()
    for g in table_motifs:
        field = g[0]
        m_id = g[1]
        motifs_ids.add(m_id)
        real_appearences = g[2]
        random_mean = g[3]
        real_zscore = g[4]
        real_pval = g[5]
        uniqueness = g[6]
        concentration = g[7]
        if field not in fields:
            fields[field] = [(m_id, real_zscore)]
        else:
            fields[field].append((m_id, real_zscore))

    motifs_ids = sorted(motifs_ids, key=lambda x:int(x))
    for fi in fields:
        fii = fields.get(fi)
        for m in motifs_ids:
            if m not in [x[0] for x in fii]:
                fii.append((m, 0.0))
        fii = sorted(fii, key=lambda x:int(x[0]))
    files[f] = fields

for kfile in files:
    file_fields = files.get(kfile)
    file_folder = '/'.join(kfile.split('/')[:-2] + ['vectors'])
    file_name = '/'.join(kfile.split('/')[:-2] + ['vectors'] + kfile.split('/')[-1:])
    os.makedirs(file_folder, exist_ok=True)
    w = open(file_name, 'w')
    for kfield in sorted(file_fields):
        motifs_ids = [i[0] for i in sorted(file_fields.get(kfield), key=lambda x:int(x[0]))]
        break
    w.write(','.join(['GROUP'] + motifs_ids))
    w.write('\n')
    for kfield in sorted(file_fields):
        vfield = file_fields.get(kfield)
        w.write(kfield + ',')
        w.write(','.join([str(vi[1]) for vi in sorted(vfield, key=lambda x:int(x[0]))]))
        w.write('\n')
    w.close()
