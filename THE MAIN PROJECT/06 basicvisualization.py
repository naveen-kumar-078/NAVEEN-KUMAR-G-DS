import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("outputs/cleaned_dataset.csv")

plt.hist(data["Hours_Spent_Per_Week"], bins=10, label="Hours Spent")
plt.title("Histogram of Hours Spent Per Week")
plt.xlabel("Hours Spent Per Week")
plt.ylabel("Frequency")
plt.legend()
plt.show()


platform_counts = data["Platform"].value_counts()

plt.bar(platform_counts.index, platform_counts.values, label="Users")
plt.title("Bar Chart of Learning Platforms")
plt.xlabel("Platform")
plt.ylabel("Number of Users")
plt.legend()
plt.show()

import matplotlib.pyplot as plt

plt.figure()
plt.plot(data["Hours_Spent_Per_Week"])
plt.title("Line Plot of Hours Spent Per Week")
plt.xlabel("Index")
plt.ylabel("Hours Spent Per Week")
plt.show()

