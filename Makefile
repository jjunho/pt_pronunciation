PY		= .venv/bin/python
PIP		= .venv/bin/pip

PX2T	= src/xlsx2tsv.py
PT2D	= src/tsv2data.py
PD2D	= src/data2dataframe.py

DDATA	= data
DORIG	= $(DDATA)/0_original

FXZIP   = $(DORIG)/xlsx.zip
FALLT	= $(DDATA)/all.tsv
FDATX	= $(DDATA)/data.xlsx
FDATT	= $(DDATA)/data.tsv

SXLS	= $(wildcard $(DORIG)/xlsx/*.xlsx)
STSV	= $(patsubst $(DORIG)/xlsx/%.xlsx,$(DDATA)/%.tsv,$(SXLS))
PTSV	= $(patsubst $(DORIG)/xlsx/%.xlsx,$(DDATA)/%.ptsv,$(SXLS))

data: $(FDATX)

init: .venv
	cd $(DORIG); unzip xlsx; cd -

$(FDATX): $(FALLT) $(PD2D)
	$(PY) $(PD2D) $(FALLT) $(DDATA)

$(FALLT): $(PTSV)
	cat $(PTSV) > $(FALLT) 

$(DDATA)/%.ptsv: $(STSV) $(PT2D)
	$(PY) $(PT2D) $< > $@

$(DDATA)/%.tsv: $(PX2T)
	$(PY) $(PX2T) $(DORIG)/xlsx/$*.xlsx $@

.venv:
	python -m venv .venv
	$(PIP) install -U pip
	$(PIP) install -U -r requirements.txt

clean:
	rm -rf $(FDATT)
	rm -rf $(FDATX)
	rm -rf $(PTSV)
	rm -rf $(FALLT)

clean-all: clean
	rm -rf $(DORIG)/xlsx
	rm -rf .venv