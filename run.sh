#! /bin/bash

source ~/env/jupyter/bin/activate
unzip -d data data/xlsx.zip
python src/process_xlsx.py
rm -rf data/xlsx
python src/process_tsv.py
rm -rf data/tsv
