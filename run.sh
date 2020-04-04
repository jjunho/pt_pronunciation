#! /bin/bash

source venv/bin/activate
unzip -d data/00_original data/00_original/xlsx.zip
python src/process_xlsx.py
rm -rf data/00_original/xlsx
python src/process_tsv.py
