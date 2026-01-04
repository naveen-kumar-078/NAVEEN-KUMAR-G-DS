import pandas as pd
import plotly.express as px

# Load CSV
df = pd.read_csv("uae_real_estate_2024.csv")

# Select numeric columns safely
numeric_cols = df.select_dtypes(include="number").columns

# Create an interactive scatter plot (guaranteed to work)
fig = px.scatter(
    df,
    x=numeric_cols[0],
    y=numeric_cols[1] if len(numeric_cols) > 1 else numeric_cols[0],
    title="Interactive Visualization – UAE Real Estate 2024",
    hover_data=df.columns
)

fig.show()
