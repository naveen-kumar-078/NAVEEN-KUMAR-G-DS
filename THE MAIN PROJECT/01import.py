import pandas as pd

df = pd.read_csv("data/online_learning_course_consumption_dataset.csv")

print("Complete Dataset:")
print(df)

print("\nFirst 5 Rows:")
print(df.head(5))

print("\nStructure of the Dataset:")
print(df.info())

print("\nDataset Shape (Rows, Columns):")
print(df.shape)
