# BIS Mitra - AI/ML Module

## Overview

BIS Mitra is an AI-powered assistant designed to help users identify relevant Indian Standards and understand BIS-related compliance information.

This folder contains the AI/ML module of the project.

## AI/ML Pipeline

User Query  
↓  
Sentence Transformer  
↓  
384-Dimensional Embedding  
↓  
FAISS Vector Search  
↓  
Semantic Similarity  
↓  
Confidence Threshold  
↓  
Relevant BIS Record  
↓  
Grounded Response  
↓  
Compliance Guidance + Official BIS Source

## Technologies

- Python
- Sentence Transformers
- all-MiniLM-L6-v2
- FAISS
- NumPy
- Pandas
- Scikit-learn

## Features

- Natural-language product understanding
- Semantic similarity search
- BIS standard recommendation
- FAISS vector retrieval
- Confidence-based rejection of unsupported queries
- Grounded BIS responses
- Compliance journey generation
- Official BIS source references
- Backend-ready AI interface
- Top-1 and Top-3 evaluation

## Knowledge Base

The current prototype contains 7 representative product records.

BIS information is stored with:

- Product name
- Aliases
- Indian Standard number
- Standard title
- Description
- Certification status
- Official source
- Source URL
- Last verification date

## Evaluation

Current prototype evaluation set:

- Total queries: 12
- Supported queries: 11
- Unsupported queries: 1
- Supported Top-1 Accuracy: 100%
- Supported Top-3 Accuracy: 100%
- Rejection Accuracy: 100%

These results apply only to the current small prototype evaluation set and should not be interpreted as universal BIS recommendation accuracy.

## Run

Install dependencies:

```bash
pip install -r requirements.txt