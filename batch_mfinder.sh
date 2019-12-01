#!/usr/bin/env bash
DIR_SUBGRAPHS=$1
MOTIF_SIZE=$2
DIR_OUTPUT=$3
mkdir -p $DIR_OUTPUT/$MOTIF_SIZE
cd $DIR_SUBGRAPHS;
for f in *-edges-minimal.csv;
do
  echo 'SUBGRAPH='$DIR_SUBGRAPHS/$f 'MOTIF_SIZE='$MOTIF_SIZE;
  /home/rafael/Working/phd/agmotifs/mfinder "$DIR_SUBGRAPHS/$f" -s $MOTIF_SIZE -f "$DIR_OUTPUT/$MOTIF_SIZE/$f"
  mv "$DIR_OUTPUT/$MOTIF_SIZE/$f""_OUT.txt" "$DIR_OUTPUT/$MOTIF_SIZE/$f"
done
