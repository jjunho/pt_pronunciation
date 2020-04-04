#!/usr/bin/env python3
# coding: utf-8

from functools import reduce
from operator import add
from glob import glob
from pathlib import Path
from libs import hangul

IN_DIR = "data/01_process/tsv"
OUT_DIR = "data/01_process"

DATA_FILES = sorted(f for f in glob(f"{IN_DIR}/*") if '.tsv' in f)

PT_WORDS = ["pais", "país", "vela", "bela", "ele", "ele (L)", "som", "são", "sábia", "sabia", "sabiá", "zelo", "gelo", "cara", "cala", "meu", "mel", "sou", "sol", "bolo", "bola", "líquido", "liquido", "liqüido", "pato", "topa",
            "tapioca", "China", "sina", "cheio", "seio", "quem", "vem", "alguém", "um", "dois", "ficar", "picar", "venha", "vênia", "cidade", "cidade (d)", "pacato", "batata", "mamata", "talento", "daquilo", "naquilo", "carroça", "gamela"]


def words_from(tsv_file):
    words = [line.strip().split('\t')[2:]
             for line in open(tsv_file).readlines()[2:]]
    return words


def make_table(tsv_file):
    pos_words = enumerate(words_from(tsv_file))
    name = Path(tsv_file).stem
    for pos, words in pos_words:
        for word in words:
            yield [name, PT_WORDS[pos], word, hangul.yale(word), hangul.ipa(word)]


data = "\n".join("\t".join(line) for line in reduce(
    add, [[*make_table(data_file)] for data_file in DATA_FILES]))

open(f"{OUT_DIR}/data_table.tsv", "w").write(data)
