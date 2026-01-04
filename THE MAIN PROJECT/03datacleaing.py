import pandas as pd

# load dataset
data = pd.read_csv("data/online_learning_course_consumption_dataset.csv")

# -----------------------------
# DATA CLEANING (example)
# -----------------------------
data["Hours_Spent_Per_Week"] = data["Hours_Spent_Per_Week"].fillna(data["Hours_Spent_Per_Week"].mean())
data["Course_Duration_Weeks"] = data["Course_Duration_Weeks"].fillna(data["Course_Duration_Weeks"].mean())
data["Completion_Percentage"] = data["Completion_Percentage"].fillna(data["Completion_Percentage"].mean())
data["Satisfaction_Score"] = data["Satisfaction_Score"].fillna(data["Satisfaction_Score"].mean())
data["Dropout_Reason"] = data["Dropout_Reason"].fillna(data["Dropout_Reason"].mode()[0])

data = data.drop_duplicates()

# -----------------------------
# REQUIRED OUTPUT (LIKE IMAGE)
# -----------------------------
print("Missing values after cleaning and removing duplicates:")
print(data.isnull().sum())

print("\nNon-missing values after cleaning and removing duplicates:")
print(data.notnull().sum())
