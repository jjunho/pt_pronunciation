#! /bin/bash

source venv/bin/activate
unzip -d data/00_original data/00_original/xlsx_01.zip
python src/process_xlsx.py data/00_original/xlsx data/00_original/tsv
rm -rf data/00_original/xlsx
python src/process_tsv.py data/00_original/tsv data/01_process
rm -rf data/00_original/tsv
python src/create_dataframe.py data/00_original data/01_process
