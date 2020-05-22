#! .venv/bin/python3
# coding: utf-8

import pandas as pd
import sys

IN, OUT = sys.argv[1:3]
PT_PHON_FILE = "src/pt_phon.tsv"


def read_tsv(tsv): return pd.read_csv(tsv, sep="\t", names=[
    "Student", "Orth", "Hankul", "Yale", "KO"])


data = read_tsv(IN)

pt_phon = pd.read_csv(PT_PHON_FILE, sep="\t", names=[
                      "Orth", "PT"], index_col="Orth").to_dict()['PT']
data["PT"] = data.apply(lambda row: pt_phon[row.Orth], axis=1)
word_number = dict((y, x) for x, y in enumerate(data['PT'][:50], 1))
data["Word"] = data.apply(lambda row: word_number[row.PT], axis=1)
data = data[["Student", "Word", "Orth", "Hankul", "Yale", "PT", "KO"]]

data.to_csv(f"{OUT}/data.tsv", sep='\t')
data.to_excel(f"{OUT}/data.xlsx")
