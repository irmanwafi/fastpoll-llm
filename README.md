# Fast Poll Malaysia LLM– GPT-Powered Public Opinion Simulation

This project simulates Malaysian public opinion using GPT (ChatGPT or OpenAI API) by generating synthetic responses grounded in real demographic data from DOSM (Department of Statistics Malaysia).

---

## 🎯 Objective

To build an AI-powered polling simulator that:
- Uses actual Malaysian demographic data
- Generates synthetic personas reflective of population distributions
- Prompts GPT to simulate how each persona would respond to an issue
- Aggregates responses to reveal public sentiment, broken down by state, ethnicity, income, etc.

Based on the academic methodology from:
> **"Simulating and Predicting Public Opinions in Surveys Using LLMs"**  
> [arXiv:2411.01582](https://arxiv.org/abs/2411.01582)

---

## 🧱 Project Structure

```
AI_Fast_Poll_Malaysia/
├── data/
│   ├── 1_population/               # DOSM population by state
│   ├── 2_income/                   # DOSM household income (optional)
│   ├── 3_education/                # DOSM education data (optional)
│   └── 4_cleaned_data/
│       └── demographic_base.csv   # Final personas
├── prompts/
│   └── generated_prompts.csv      # GPT-ready polling prompts
├── results/
│   └── ai_poll_results.csv        # GPT-simulated responses
├── scripts/
│   ├── persona_generator.py       # Python: build personas from real data
│   └── prompt_generator.py        # Python: generate prompts
├── README.md                      # This file
└── requirements.txt               # Python dependencies
```

---

## ⚙️ Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/yourusername/ai-fast-poll-malaysia.git
cd ai-fast-poll-malaysia
```

### 2. Setup virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate       # Windows: .\venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install pandas openai
```

---

## 📂 Required DOSM Datasets

Place the following files in your data folders:

- `data/1_population/population_state.csv`
- `data/2_income/hh_income_district.csv` *(optional)*
- `data/3_education/completion_school_state.csv` *(optional)*

These datasets must originate from [https://www.dosm.gov.my](https://www.dosm.gov.my).

---

## 🔁 Workflow: End-to-End

### ✅ Step 1: Generate Personas

Run the script:

```bash
python scripts/persona_generator.py
```

What it does:
- Reads real ethnicity data from DOSM
- Generates 50 synthetic personas
- Outputs `data/4_cleaned_data/demographic_base.csv`

Each persona has:

| Persona ID | State | Age Group | Gender | Ethnicity | Urban/Rural | Income Group | Education |
|------------|-------|-----------|--------|-----------|--------------|---------------|-----------|

---

### ✅ Step 2: Generate Prompts

Run:

```bash
python scripts/prompt_generator.py
```

What it does:
- Converts each persona into a GPT-ready prompt
- Example prompt:

```
You are a 25-34 year old Malay female from Selangor, living in an Urban area with M40 income and Degree education. What is your opinion on fuel subsidy removal?
```

- Output: `prompts/generated_prompts.csv`

---

### ✅ Step 3: Simulate Responses with GPT

Manual method:
- Paste each prompt into ChatGPT
- Save the response in a CSV with columns: `Persona ID`, `Prompt`, `Response`

Optional (automated):
- Use OpenAI API (you’ll need an API key)
- Future script: `gpt_response_collector.py`

---

### ✅ Step 4: Analyze Results

Use tools like:
- Excel / Google Sheets (pivot tables)
- Python (pandas, seaborn, matplotlib)
- Power BI / Tableau for dashboard visuals

Example insights:
- What % of Malay B40s from rural states support policy X?
- Which states show strongest positive sentiment?

---

## 🧠 Methodology: Why It Works

- Each persona represents a real demographic pattern (DOSM-aligned)
- GPT simulates a plausible opinion from that type of citizen
- Aggregated responses give directional insight (not statistical certainty)
- Mirrors the research approach in peer-reviewed studies

Fields used (same as the original study):
- Age
- Gender
- Education
- Income
- Ethnicity
- State (region)

---

## 🔍 Example Use Cases

- Policy testing: “Should the government remove fuel subsidies?”
- Political sentiment: “Do you support the current Prime Minister?”
- Social questions: “What do you think about vernacular schools?”

---

## 🛠️ Python Requirements (requirements.txt)

```
pandas
openai
```

---

## 📌 Future Features

- GPT response collector (automated via API)
- Sentiment scoring
- Choropleth map visualization by state
- Multi-issue simulations

---

## 📚 References

- [Simulating and Predicting Public Opinions in Surveys Using LLMs](https://arxiv.org/abs/2411.01582)
- [DOSM Official Portal](https://www.dosm.gov.my)

---