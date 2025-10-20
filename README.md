# Multimodal Source Code – Vulnerability Description Classification

---
The goal of this project is to develop a multimodal transformer-based model that aligns source code snippets and their corresponding vulnerability descriptions to improve CWE category classification
---

## Objectives

- Align source code and vulnerability descriptions in a shared latent space  
- Exploit this alignment to classify vulnerabilities into CWE categories
- Evaluate the effectiveness of multimodal alignment in improving classification accuracy

---

## Methodology

### 1. Dataset preparation
- Dataset derived from **real CVE records (NVD)**, including
  - `code_snippet`
  - `vulnerability_description`
  - `CWE_label`
- Text preprocessing
  - lowercasing, tokenization (RoBERTa tokenizer)
- Code preprocessing
  - normalization, comment removal, tokenization (CodeBERT tokenizer)

---

### 2. Model Architecture

The architecture uses **two transformer encoders**:
- **Code Encoder:** `CodeBERT`  
- **Text Encoder:** `RoBERTa`  
