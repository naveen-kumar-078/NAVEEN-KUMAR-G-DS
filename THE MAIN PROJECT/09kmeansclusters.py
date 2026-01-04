import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# load dataset
data = pd.read_csv("outputs/cleaned_dataset.csv")

# select numeric columns
numeric_data = data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]]

# standardize numeric data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_data)

# apply k-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
data["Cluster"] = kmeans.fit_predict(scaled_data)

# -----------------------------
# OUTPUT 1: CLUSTER COUNTS
# -----------------------------
print("Number of data points in each cluster:")
print(data["Cluster"].value_counts())

# -----------------------------
# OUTPUT 2: CLUSTER INTERPRETATION
# -----------------------------
print("\nCluster-wise Interpretation (Mean Values):")
cluster_summary = data.groupby("Cluster")[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]].mean()

print(cluster_summary)

# -----------------------------
# OUTPUT 3: SCATTER PLOT
# -----------------------------
plt.figure()
sns.scatterplot(
    data=data,
    x="Hours_Spent_Per_Week",
    y="Completion_Percentage",
    hue="Cluster"
)
plt.title("Scatter Plot: Clusters based on Study Hours & Completion")
plt.xlabel("Hours Spent Per Week")
plt.ylabel("Completion Percentage")
plt.show()

# -----------------------------
# OUTPUT 4: PAIR PLOT
# -----------------------------
sns.pairplot(
    data,
    vars=[
        "Hours_Spent_Per_Week",
        "Course_Duration_Weeks",
        "Completion_Percentage",
        "Satisfaction_Score"
    ],
    hue="Cluster"
)
plt.show()

