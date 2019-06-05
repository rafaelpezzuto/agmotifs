#!/bin/bash
PASTA_MOTIFS=/mnt/backup/cloud/FeeRa-eOS-Desktop/Dropbox/thesis/motifs
PASTA_TABELAS=/mnt/backup/cloud/FeeRa-eOS-Desktop/Dropbox/thesis/motifs/tables
mkdir -p $PASTA_TABELAS

python3 generate_motifs_table.py "$PASTA_MOTIFS"/grandes-areas/rigor/3 > "$PASTA_TABELAS"/grandes-areas-rigor-3.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/grandes-areas/rigor/4 > "$PASTA_TABELAS"/grandes-areas-rigor-4.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/grandes-areas/rigor/5 > "$PASTA_TABELAS"/grandes-areas-rigor-5.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/grandes-areas/flex/3 > "$PASTA_TABELAS"/grandes-areas-flex-3.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/grandes-areas/flex/4 > "$PASTA_TABELAS"/grandes-areas-flex-4.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/grandes-areas/flex/5 > "$PASTA_TABELAS"/grandes-areas-flex-5.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/areas/rigor/3 > "$PASTA_TABELAS"/areas-rigor-3.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/areas/rigor/4 > "$PASTA_TABELAS"/areas-rigor-4.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/areas/rigor/5 > "$PASTA_TABELAS"/areas-rigor-5.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/areas/flex/3 > "$PASTA_TABELAS"/areas-flex-3.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/areas/flex/4 > "$PASTA_TABELAS"/areas-flex-4.tsv 
python3 generate_motifs_table.py "$PASTA_MOTIFS"/areas/flex/5 > "$PASTA_TABELAS"/areas-flex-5.tsv 
