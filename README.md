# Elasticsearch Search Labs Projects

![Elasticsearch Logo](https://www.elastic.co/static-res/images/elastic-logo-200.png)

## Overview
This repository contains three Elasticsearch implementations demonstrating different search approaches, built following the official [Elasticsearch Search Labs Tutorial](https://www.elastic.co/search-labs/tutorials/search-tutorial).

## 🔍 Projects

### 1. Full-Text Search
Traditional keyword-based search implementation

#### Features:
- ✅ Basic search queries with relevance scoring
- 📄 Pagination (`from/size`)
- 🔍 Filtering with boolean queries
- 📊 Faceted search with aggregations
- ⚡ Performance optimized settings

#### Directory: `full-text-search/`

---

### 2. Vector Search (k-NN)
Vector similarity search implementation

#### Features:
- 🤖 Dense vector embeddings (sentence-transformers)
- 🔢 k-NN search 
- 🔄 Hybrid vector+keyword search
- 🏎️ Optimized for production workloads

#### Directory: `vector-search-knn/`

---

### 3. Semantic Search (ELSER)
Context-aware search using ELSER v2

#### Features:
- 🧠 ELSER v2 model deployment
- 💡 Semantic query expansion
- 🔄 Hybrid semantic+keyword search


#### Directory: `semantic-search-elser/`

## 🛠️ Technical Implementation

### Requirements
| Component       | Requirement           |
|-----------------|-----------------------|
| Elasticsearch   | 8.x+ recommended      |
| Python          | 3.8+                  |
| Dependencies    | See `requirements.txt`|

![image](https://github.com/user-attachments/assets/ec106a8f-c868-4007-a423-81ce974c73ec)


### set up guide
- follow the project setup in  [Elasticsearch Search Labs Tutorial](https://www.elastic.co/search-labs/tutorials/search-tutorial).
- replace the files by the files in this repo and u re free to go 



   
