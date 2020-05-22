#! .venv/bin/python3
# coding: utf-8

import pandas as pd
import sys

IN, OUT = sys.argv[1:3]

xlsx = pd.read_excel(IN)
xlsx.to_csv(OUT, sep="\t")
