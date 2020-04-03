#!/usr/bin/env python3
# coding: utf-8

from pathlib import Path
from glob import glob
import os
import pandas as pd

IN_DIR = "data/xlsx"
OUT_DIR = "data/tsv"

if not os.path.exists(OUT_DIR):
    os.makedirs(OUT_DIR)


def xlsx2tsv(infile_path, outfile_path):
    xlsx = pd.read_excel(infile_path)
    xlsx.to_csv(outfile_path, sep="\t")


def change_filename(infilename, outdir):
    name, *_ = infilename.strip().split('_')
    clean_name = Path(name).stem
    return f"{outdir}/{clean_name}.tsv"


def get_all_files(dir):
    return [x for x in glob(f"{dir}/*") if '.xlsx' in x]


def make_tsvs(indir, outdir):
    all_files = get_all_files(indir)
    for infile in all_files:
        xlsx2tsv(infile, change_filename(infile, outdir))


make_tsvs(IN_DIR, OUT_DIR)
