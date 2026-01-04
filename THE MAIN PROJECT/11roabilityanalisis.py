import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("outputs/cleaned_dataset.csv")

# Probability distribution: Hours Spent Per Week
sns.histplot(
    data["Hours_Spent_Per_Week"],
    kde=True,
    stat="density"
)
plt.title("Probability Distribution of Hours Spent Per Week")
plt.xlabel("Hours Spent Per Week")
plt.ylabel("Probability Density")
plt.show()

# Probability distribution: Completion Percentage
sns.histplot(
    data["Completion_Percentage"],
    kde=True,
    stat="density"
)
plt.title("Probability Distribution of Completion Percentage")
plt.xlabel("Completion Percentage")
plt.ylabel("Probability Density")
plt.show()
