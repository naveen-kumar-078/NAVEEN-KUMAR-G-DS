import pandas as pd
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("data/online_learning_course_consumption_dataset.csv")

scaler = StandardScaler()

data["Hours_Spent_Per_Week"] = scaler.fit_transform(data[["Hours_Spent_Per_Week"]])
data["Course_Duration_Weeks"] = scaler.fit_transform(data[["Course_Duration_Weeks"]])
data["Completion_Percentage"] = scaler.fit_transform(data[["Completion_Percentage"]])
data["Satisfaction_Score"] = scaler.fit_transform(data[["Satisfaction_Score"]])

print("Standardization completed")

print(data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]].head())
