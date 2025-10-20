import pandas as pd
import re
import csv
import os
from collections import Counter
import spacy
import nltk


SOURCE_FILE = os.path.join("../data", "code_w_descriptions.csv")
DEST_FILE   = os.path.join("../data", "processed", "dataset_vulnerabilita_cleaned.csv")
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

nltk.download('stopwords', download_dir='./nltk_data', quiet=False)
nltk.data.path.append('./nltk_data')

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

# Funzione per rimuovere commenti da codice (sia // che /* */)
def remove_comments(code):
    if not isinstance(code, str):
        return ''
    
    code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)
    code = re.sub(r'//.*', '', code)
    return code.strip()

# Funzione per normalizzare spazi e tabulazioni
def normalize_whitespace(code):
    if not isinstance(code, str):
        return ''
    #Serve a mantenere le tabulazioni e gli spazi di inizio riga e a normalizzare quelle in mezzo al codice
    def replacer(match):
        init_line = match.group(1)
        line = match.group(2)
        line = re.sub(r'\t{2,}', '\t', line)
        line = re.sub(r'(?<=\S) {2,}', ' ', line)
        return init_line + line.rstrip()

    pattern = re.compile(r'^(\t*)(.*)$', re.MULTILINE)
    normalized_code = re.sub(pattern, replacer, code)
    return normalized_code

# Funzione di pulizia testo
def clean_text(text):
    if not isinstance(text, str):
        return ''
    t = text.strip().lower()
    # mantiene lettere, numeri, spazi, trattini, underscore e apostrofi
    t = re.sub(r"[^0-9a-zàèéìòùÀÈÉÌÒÙüÜ\s\-\_']", " ", t)
    # sostituisci sequenze di spazi multipli con uno solo
    t = re.sub(r"\s+", " ", t)
    return t.strip()


# Funzione di lemming 
def lemming_text(text):
    doc = nlp(text)
    return ' '.join([token.lemma_ for token in doc])

def remove_stopwords(text):
    tokens = text.split()
    tokens = [t for t in tokens if t not in stop_words]
    return ' '.join(tokens)

# Funzione di processing
def process_code(code):
    if pd.isna(code):
        return ''
    code = remove_comments(code)
    code = normalize_whitespace(code)
    return code

# Caricamento dataset 
df = pd.read_csv(
    SOURCE_FILE,
    quotechar='"',
    doublequote=True,      
    quoting=csv.QUOTE_ALL,
    dtype=str,
    skip_blank_lines=True,
    on_bad_lines='skip',
    keep_default_na=False
)

# Applica processamento sulla colonna  'code' per gli snippet di codice
# su CWE_desc per le descrizioni delle vulnerabilità
df['code'] = df['code'].apply(process_code)
df['CWE_desc'] = df['CWE_desc'].apply(clean_text)
df['CWE_desc'] = df['CWE_desc'].apply(remove_stopwords)
df['CWE_desc'] = df['CWE_desc'].apply(lemming_text)

df.to_csv(DEST_FILE, index=False)

print("Numero righe:", len(df))
print("CWE unique:", df['CWE_ID'].nunique())
print("Top 10 CWE e counts:", Counter(df['CWE_ID']).most_common(10))


