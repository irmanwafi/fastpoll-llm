import pandas as pd
import os

# === Paths ===
INPUT_PATH = "data/4_cleaned_data/demographic_base.csv"
OUTPUT_PATH = "prompts/generated_prompts.csv"
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# === Load personas ===
df = pd.read_csv(INPUT_PATH)

# === Define polling questions ===
polling_questions = {
    "fuel_subsidy": "What is your opinion on the government's decision to remove fuel subsidies?",
    "vernacular_schools": "Do you support the continuation of vernacular schools in Malaysia?",
    "pm_support": "Do you support the current Prime Minister's leadership?",
    "cost_of_living": "How concerned are you about the rising cost of living in Malaysia?",
    "ethnic_relations": "What is your view on the state of ethnic relations in Malaysia today?"
}

# === Generate prompts ===
prompt_rows = []

for _, row in df.iterrows():
    persona_id = row["Persona ID"]
    context = (
        f"You are a {row['Age Group']} year old {row['Ethnicity']} {row['Gender'].lower()} "
        f"from {row['State']}, living in a {row['Urban/Rural']} area, with {row['Income Group']} income "
        f"and {row['Education']} education."
    )

    for key, question in polling_questions.items():
        prompt = f"{context} {question}"
        prompt_rows.append({
            "Persona ID": persona_id,
            "Question": key,
            "Prompt": prompt
        })

# === Save to CSV ===
out_df = pd.DataFrame(prompt_rows)
out_df.to_csv(OUTPUT_PATH, index=False)
print(f"✅ Generated {len(out_df)} prompts for {len(df)} personas in {OUTPUT_PATH}")
