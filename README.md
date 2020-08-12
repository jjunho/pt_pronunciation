Data about Korean learners' acquisition of Portuguese pronunciation

Copyright © 2020 Juliano Paiva Junho

The data in this repository is available under the terms written in the file `LICENSE`.

## Basic requirements

You need `python3` in order to build the data file used in this research.

## Build script help

```bash
python3 makepy -h
```

```
usage: makepy [-h] [--all] [--init] [--data] [--clean] [--clean-all]

makepy: A script to build the research data

optional arguments:
  -h, --help   show this help message and exit
  --all        initializes python environment and builds all data
  --init       initializes python environment
  --data       builds all data
  --clean      cleans only built data
  --clean-all  cleans all data and python environment
```

## Make the data file

```bash
python3 makepy --all
```

The data file will be in `data/all.tsv` and `data/all.xlsx`.