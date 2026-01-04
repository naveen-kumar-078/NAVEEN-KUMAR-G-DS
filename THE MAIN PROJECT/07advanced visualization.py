import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load cleaned dataset
data = pd.read_csv("outputs/cleaned_dataset.csv")

# select numeric columns
numeric_data = data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]]

# -----------------------------
# PAIR PLOT
# -----------------------------
sns.pairplot(numeric_data)
plt.show()

# -----------------------------
# HEATMAP (CORRELATION)
# -----------------------------
correlation_matrix = numeric_data.corr()

plt.figure()
sns.heatmap(correlation_matrix, annot=True)
plt.title("Correlation Heatmap")
plt.show()

# -----------------------------
# VIOLIN PLOT
# -----------------------------
plt.figure()
sns.violinplot(y=data["Hours_Spent_Per_Week"])
plt.title("Violin Plot of Hours Spent Per Week")
plt.show()

# -----------------------------
# CORRELATION & COVARIANCE
# -----------------------------
print("Correlation Matrix:")
print(correlation_matrix)

print("\nCovariance Matrix:")
print(numeric_data.cov())



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# load cleaned dataset
data = pd.read_csv("outputs/cleaned_dataset.csv")

# select numeric columns
numeric_data = data[
    ["Hours_Spent_Per_Week",
     "Course_Duration_Weeks",
     "Completion_Percentage",
     "Satisfaction_Score"]
]

# calculate covariance
covariance_matrix = numeric_data.cov()

# visualize covariance using heatmap
plt.figure()
sns.heatmap(covariance_matrix, annot=True)
plt.title("Covariance Heatmap of Online Learning Features")
plt.show()
