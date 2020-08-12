# pt_pronunciation

Data about Korean learners' acquisition of Portuguese pronunciation

Copyright © 2020 Juliano Paiva Junho

The data in this repository is available under the terms written in the file `LICENSE`.

## Basic requirements

You need `python3` and `make` in order to build the data file used in this research.

## Initialize the virtual environment

```bash
make init
```

## Unzip the xlsx data and make the data file

```bash
make xlsx
make
```

After `make`ing the data, you can clean the directory.

```bash
make clean
```

The data file will be in `data/data.tsv` and `data/data.xlsx`.