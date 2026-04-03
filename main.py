import pandas as pd
from funnel import generate_data
from analysis import run_analysis

# Step 1: Generate dataset
generate_data()

# Step 2: Load dataset
df = pd.read_csv("funnel_dataset.csv")

# Step 3: Run analysis
run_analysis(df)