import pandas as pd
from transformers import AutoTokenizer, AutoModel, RobertaTokenizer, RobertaModel
import numpy as np
import torch
import os

DATASET_PATH = os.path.join("data", "processed", "dataset_vulnerabilita_cleaned.csv")
EMBEDDINGS_PATH = os.path.join("data", "processed", "embeddings")

os.makedirs(EMBEDDINGS_PATH, exist_ok=True)
df = pd.read_csv(DATASET_PATH)

# Tokenizer e modelli
code_tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
code_model = AutoModel.from_pretrained("microsoft/codebert-base")

desc_tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
desc_model = RobertaModel.from_pretrained("roberta-base")

max_length = 128

# Funzioni per embeddings
def embed_code(snippet):
    tokens = code_tokenizer(snippet, return_tensors="pt", truncation=True, padding="max_length", max_length=max_length)
    with torch.no_grad():
        outputs = code_model(**tokens)
        embedding = outputs.last_hidden_state[:, 0, :]
    return embedding.squeeze(0).numpy()

def embed_desc(desc):
    tokens = desc_tokenizer(desc, return_tensors="pt", truncation=True, padding="max_length", max_length=max_length)
    with torch.no_grad():
        outputs = desc_model(**tokens)
        embedding = outputs.last_hidden_state[:, 0, :]
    return embedding.squeeze(0).numpy()

code_embeddings_list = []
desc_embeddings_list = []

for idx, (snippet, desc) in enumerate(zip(df['code'], df['CWE_desc'])):
    code_embedding = embed_code(str(snippet))
    desc_embedding = embed_desc(str(desc))
    code_embeddings_list.append(code_embedding)
    desc_embeddings_list.append(desc_embedding)
    if (idx+1) % 50 == 0:
        print(f"{idx+1} snippet elaborati")

# Salvataggio embeddings
np.save(os.path.join(EMBEDDINGS_PATH, "codebert_embeddings.npy"), np.array(code_embeddings_list))
np.save(os.path.join(EMBEDDINGS_PATH, "roberta_embeddings.npy"), np.array(desc_embeddings_list))

print(f"Tutti gli embeddings salvati in {EMBEDDINGS_PATH}")
