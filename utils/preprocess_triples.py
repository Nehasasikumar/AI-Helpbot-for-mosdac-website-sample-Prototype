import pandas as pd
from pathlib import Path

# Input/Output paths
INPUT_CSV = "data/triples.csv"
OUTPUT_CSV = "data/triples_clean.csv"

# Ensure output directory exists
Path("data").mkdir(parents=True, exist_ok=True)

# Load triples
df = pd.read_csv(INPUT_CSV)

# Drop rows with missing or very short text
df.dropna(inplace=True)
df["Object"] = df["Object"].astype(str)
df = df[df["Object"].str.len() > 20]

# Standardize predicates
df["Predicate"] = df["Predicate"].str.lower().str.strip()
df["Predicate"] = df["Predicate"].replace({
    "was_launched_on": "launched_on",
    "has_payload": "has_payload",
    "provides_service": "provides_service",
    # Add other mappings if needed
})

# Remove duplicates
df.drop_duplicates(inplace=True)

# Truncate overly long objects for visualization
def truncate(text, length=100):
    return text if len(text) <= length else text[:length].strip() + "..."

df["Object"] = df["Object"].apply(lambda x: truncate(x))

# Save cleaned triples
df.to_csv(OUTPUT_CSV, index=False)
print(f"Cleaned triples saved to {OUTPUT_CSV}")
