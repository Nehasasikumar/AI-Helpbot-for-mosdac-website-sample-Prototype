# AI-Helpbot-for-mosdac-website-sample-Prototype

**This project demonstrates a smart prototype that:**
->Scrapes satellite mission and FAQ data from the MOSDAC website
->Extracts and preprocesses key information using NLP techniques
->Generates structured knowledge triples
->Visualizes a clean and interpretable Knowledge Graph
->Lays the groundwork for an intelligent assistant for ISRO/MOSDAC portals

**Features:**
->Web scraping using Selenium + BeautifulSoup
->NLP preprocessing using NLTK + spaCy
->Knowledge triple extraction (Subject-Predicate-Object)
->Clean triple refinement
->Interactive and visually intuitive KG generation using NetworkX & matplotlib

**Project Structure**
AI Helpbot for mosdac website sample Prototype/
│
├── data/
│   ├── mosdac_missions.xlsx     ← Raw scraped data (Excel)
│   ├── output.json              ← Original JSON scrape
│   ├── triples.csv              ← Initial extracted triples
│   └── triples_clean.csv        ← Refined triples for KG
│
├── kg/
│   ├── graph.gexf               ← Knowledge Graph (GEXF format for tools like Gephi)
│   └── clean_kg_graph.png       ← Neatly visualized KG image
│
├── scraper/
│   └── faq_scraper.py           ← Web scraper using Selenium & BeautifulSoup
│
├── utils/
│   ├── preprocess_triples.py    ← Triple cleaner/preprocessor
│   └── kg_preprocessor.py       ← Knowledge Graph builder & visualizer
│
├── requirements.txt             ← Python dependencies
└── README.md                    ← This file

**How to Run:**
**1️)Create a virtual environment (if not already)**
python -m venv venv
.\venv\Scripts\Activate.ps1   # For Windows PowerShell

**2️)Install dependencies:**
pip install -r requirements.txt
python -m spacy download en_core_web_sm

**3️)Scrape the data (optional if already present):**
python scraper/faq_scraper.py

**4)Preprocess the extracted triples:**
python utils/preprocess_triples.py

**5️)Generate and visualize the Knowledge Graph:**
python utils/kg_preprocessor.py

**Example Output**
Triple Example:
insat-3d → provides_service → meteorological observation

**KG Visualization:**
Generated as a clean image in kg/clean_kg_graph.png
Also saved as kg/graph.gexf for use in Gephi or other tools

**Tech Stack:**
->Python 3.10+
->Selenium & BeautifulSoup (scraping)
->pandas, openpyxl (data handling)
->nltk, spaCy (NLP preprocessing)
->networkx, matplotlib (graph generation)

**Use Cases**
->Interactive satellite helpbot assistant
->Scientific document knowledge modeling
->Foundation for Q&A systems over scraped content
