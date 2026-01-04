import pandas as pd

# load dataset
data = pd.read_csv("data/online_learning_course_consumption_dataset.csv")

# show first rows BEFORE handling
print("Dataset sample BEFORE outlier handling:")
print(data.head())

# shape before
print("\nDataset shape before outlier handling:")
print(data.shape)

# -----------------------------
# OUTLIER HANDLING (IQR METHOD)
# -----------------------------
Q1 = data["Hours_Spent_Per_Week"].quantile(0.25)
Q3 = data["Hours_Spent_Per_Week"].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

data = data[
    (data["Hours_Spent_Per_Week"] >= lower) &
    (data["Hours_Spent_Per_Week"] <= upper)
]

# shape after
print("\nDataset shape AFTER outlier handling:")
print(data.shape)

# show first rows AFTER handling
print("\nDataset sample AFTER outlier handling:")
print(data.head())
