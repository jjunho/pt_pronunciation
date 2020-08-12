#! .venv/bin/python3
# coding: utf-8

import sys
import hangul
import re
from pathlib import Path
from functools import reduce
from operator import add

infile = sys.argv[1]

clean = re.compile(r'\.\(\..*$')

PT_WORDS = [
    "pais", "país", "vela", "bela", "ele", "ele (L)", "som", "são", "sábia", "sabia", "sabiá",
    "zelo", "gelo", "cara", "cala", "meu", "mel", "sou", "sol", "bolo", "bola", "líquido", "liquido",
    "liqüido", "pato", "topa", "tapioca", "China", "sina", "cheio", "seio", "quem", "vem", "alguém",
    "um", "dois", "ficar", "picar", "venha", "vênia", "cidade", "cidade (d)", "pacato", "batata",
    "mamata", "talento", "daquilo", "naquilo", "carroça", "gamela"
]


def make_table(tsv_file):
    def words_from(tsv_file):
        words = [line.strip().split('\t')[2:]
                 for line in open(tsv_file).readlines()[2:]]
        return words

    pos_words = enumerate(words_from(tsv_file))
    name = Path(tsv_file).stem
    for pos, words in pos_words:
        for word in words:
            if " " in word:
                continue
            word = clean.sub('', word)
            yale = clean.sub('', hangul.yale(word))
            hipa = clean.sub('', hangul.ipa(word))
            yield [name, PT_WORDS[pos], word, yale, hipa]


data = "\n".join("\t".join(line)
                 for line in reduce(add, [[*make_table(infile)]]))

print(data)
