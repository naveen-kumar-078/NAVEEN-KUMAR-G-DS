import pandas as pd

data = pd.read_csv("outputs/cleaned_dataset.csv")

print("MEAN:")
print(data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]].mean())

print("\nMEDIAN:")
print(data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]].median())

print("\nMODE:")
print(data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]].mode().iloc[0])

print("\nSTANDARD DEVIATION:")
print(data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]].std())

print("\nMINIMUM:")
print(data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]].min())

print("\nMAXIMUM:")
print(data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]].max())

print("\nSUMMARY STATISTICS:")
print(data.describe())
