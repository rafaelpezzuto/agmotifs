#!/bin/bash
pasta_grafos=$1
motif_tamanho=$2
pasta_saida=$3
mkdir -p $pasta_saida/$motif_tamanho
for f in $(ls $pasta_grafos)
do
  ./mfinder "$pasta_grafos/$f" -s $motif_tamanho -f "$pasta_saida/$motif_tamanho/$f"
  mv "$pasta_saida/$motif_tamanho/$f""_OUT.txt" "$pasta_saida/$motif_tamanho/$f"
done