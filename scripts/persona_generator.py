import pandas as pd
import random
import os

# === Paths ===
POP_PATH = "data/1_population/population_state.csv"
OUTPUT_PATH = "data/4_cleaned_data/demographic_base.csv"
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

# === Load population data ===
pop = pd.read_csv(POP_PATH)
pop.columns = [c.strip().lower().replace(" ", "_") for c in pop.columns]

# === Filter for relevant rows ===
filtered = pop[
    (pop["age"] == "overall") &
    (pop["sex"] == "both") &
    (pop["ethnicity"] != "overall")
]

# === Build ethnicity distribution by state ===
ethnic_dist = (
    filtered.groupby(["state", "ethnicity"])["population"]
    .sum()
    .groupby(level=0)
    .apply(lambda x: x / x.sum())
)

# === Convert to lookup dictionary ===
ethnic_lookup = {
    state: group.droplevel(0).to_dict()
    for state, group in ethnic_dist.groupby(level=0)
}

# === Sampling functions ===
def sample_from_distribution(dist_dict):
    values, weights = zip(*dist_dict.items())
    return random.choices(values, weights=weights, k=1)[0]

def sample_ethnicity(state):
    dist = ethnic_lookup.get(state)
    if dist:
        return sample_from_distribution(dist)
    return 'Malay'  # fallback

# === Fixed values ===
age_groups = ['18-24', '25-34', '35-44', '45-54', '55+']  # Clean hyphens
genders = ['Male', 'Female']
income_groups = ['B40', 'M40', 'T20']
education_levels = ['SPM', 'Diploma', 'Degree']
urban_states = ['Selangor', 'Penang', 'Kuala Lumpur', 'Johor', 'Putrajaya']

def infer_urban_rural(state):
    return 'Urban' if state in urban_states else 'Rural'

# === Generate personas ===
valid_states = list(ethnic_lookup.keys())
personas = []

for i in range(50):
    state = random.choice(valid_states)
    persona = {
        'Persona ID': f'P{i+1:03}',
        'State': state,
        'Age Group': random.choice(age_groups),
        'Gender': random.choice(genders),
        'Ethnicity': sample_ethnicity(state),
        'Urban/Rural': infer_urban_rural(state),
        'Income Group': random.choice(income_groups),
        'Education': random.choice(education_levels)
    }
    personas.append(persona)

# === Save to CSV ===
df = pd.DataFrame(personas)
df.to_csv(OUTPUT_PATH, index=False)
print(f"✅ Saved {len(df)} personas to {OUTPUT_PATH}")
