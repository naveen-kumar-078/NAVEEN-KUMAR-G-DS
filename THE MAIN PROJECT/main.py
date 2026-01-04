import pandas as pd
from summary import basic_info, statistics, missing_val, outlier
from transformation import transform
from mapping import plot_histogram

# load data
df = pd.read_csv("data/online_learning_course_consumption_dataset.csv")

# summary
basic_info(df)
statistics(df)
missing_val(df)

# outlier handling
df = outlier(df)

# transformation
df = transform(df)

# visualization
plot_histogram(df)

print("\nProgram executed successfully")
