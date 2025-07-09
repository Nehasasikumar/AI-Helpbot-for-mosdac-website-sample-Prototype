# AI Helpbot for MOSDAC Website – Sample Prototype

This project demonstrates a smart prototype that:

- Scrapes satellite mission and FAQ data from the MOSDAC website  
- Extracts and preprocesses key information using NLP techniques  
- Generates structured knowledge triples  
- Visualizes a clean and interpretable Knowledge Graph  
- Provides a prototype AI chatbot frontend rendered via FastAPI and Jinja2 templates

---

## Project Structure

```
AI Helpbot for mosdac website sample Prototype/
│
├── data/
│   ├── mosdac_missions.xlsx     # Raw scraped data (Excel)
│   ├── output.json              # Original scraped content
│   ├── triples.csv              # Initial extracted triples
│   └── triples_clean.csv        # Refined triples for KG
│
├── kg/
│   ├── graph.gexf               # Knowledge Graph (for Gephi/Neo4j)
│   └── clean_kg_graph.png       # Neatly visualized KG image
│
├── scraper/
│   └── faq_scraper.py           # Web scraper using Selenium & BeautifulSoup
│
├── utils/
│   ├── preprocess_triples.py    # Triple cleaner/preprocessor
│   └── kg_preprocessor.py       # KG builder & visualizer
│
├── templates/
│   └── index.html               # Chatbot frontend rendered by FastAPI
│
├── app.py                       # FastAPI backend server
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

- Windows:
  ```bash
  .\venv\Scripts\Activate.ps1
  ```
- macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## Workflow

### Step 1: Scrape Data 

```bash
python scraper/faq_scraper.py
```

### Step 2: Preprocess Extracted Triples

```bash
python utils/preprocess_triples.py
```

### Step 3: Generate Knowledge Graph

```bash
python utils/kg_preprocessor.py
```

### Step 4: Run the Web UI (Chatbot)

Ensure your HTML file is named correctly as templates/index.html.

```bash
uvicorn app:app --reload
```

Then open in browser:

```
http://127.0.0.1:8000
```

---

## Example Output

### Sample Triple

```
insat-3d → provides_service → meteorological observation
```

### Knowledge Graph

- Image output: kg/clean_kg_graph.png  
- GEXF output (for Gephi): kg/graph.gexf

---

## Tech Stack

| Area           | Tools Used                                      |
|----------------|--------------------------------------------------|
| Web Scraping   | Selenium, BeautifulSoup, requests, lxml         |
| NLP            | nltk, spaCy                                     |
| Data Handling  | pandas, openpyxl                                |
| Graphs         | networkx, matplotlib                            |
| Web Framework  | FastAPI, Jinja2                                 |
| Frontend UI    | Custom HTML/CSS with animated satellite theme   |

---

## Use Cases

- AI-powered satellite helpbot assistant  
- Scientific document knowledge modeling  
- Foundation for Q&A systems over scraped content  
- Interactive chatbot UI for demonstration and deployment  

---
