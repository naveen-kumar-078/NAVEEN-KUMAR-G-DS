import pandas as pd

data = pd.read_csv("online_learning_course_consumption_dataset.csv")

data.to_csv("online_learning_course_consumption_dataset.csv", index=False)


data.to_excel("online_learning_course_consumption_dataset.xlsx", index=False)

print("Dataset exported successfully")
