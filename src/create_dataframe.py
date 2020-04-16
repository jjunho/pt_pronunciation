import pandas as pd

ORIG_DIR = "./data/00_original"
PROC_DIR = "./data/01_process"

PT_PHON_FILE = f"{ORIG_DIR}/pt_words_phon.tsv"
DATA_FILE = f"{PROC_DIR}/data_table.tsv"
DATAFRAME = f"{PROC_DIR}/dataframe.tsv"
EXCEL_FILE = f"{PROC_DIR}/table_pt_ko.xlsx"

# %% [markdown]
# ## Load files and build dataframe

# %%
data = pd.read_csv(DATA_FILE, sep="\t", names=[
                   "Student", "Orth", "Hankul", "Yale", "KO"])

pt_phon = pd.read_csv(PT_PHON_FILE, sep="\t", names=[
                      "Orth", "PT"], index_col="Orth").to_dict()['PT']
data["PT"] = data.apply(lambda row: pt_phon[row.Orth], axis=1)

word_number = dict((y, x) for x, y in enumerate(data['PT'][:50]))
data["Word"] = data.apply(lambda row: word_number[row.PT], axis=1)

data = data[["Student", "Word", "Orth", "Hankul", "Yale", "PT", "KO"]]

# %% [markdown]
# ## Save dataframe

# %%
data.to_csv(DATAFRAME, sep='\t')

# %% [markdown]
# ## Pivot table and save excel file

# %%
table_pt_ko = data.pivot_table(index="PT", columns="Student", values=[
                               "KO"], aggfunc=lambda x: ", ".join(x))
table_pt_ko.to_excel(EXCEL_FILE)
