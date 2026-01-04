import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# load dataset
data = pd.read_csv("outputs/cleaned_dataset.csv")

# numeric input features
X = data[
    ["Hours_Spent_Per_Week",
     "Course_Duration_Weeks",
     "Completion_Percentage",
     "Satisfaction_Score"]
]

# target variable (class)
y = data["Completion_Status"]

# split data into train and test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# create k-NN model
knn = KNeighborsClassifier(n_neighbors=5)

# train model
knn.fit(X_train, y_train)

# predict
y_pred = knn.predict(X_test)

print("KNN ACCURACY")
print("k-NN Accuracy:", accuracy_score(y_test, y_pred))


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv("outputs/cleaned_dataset.csv")

X = data[[
    "Hours_Spent_Per_Week",
    "Course_Duration_Weeks",
    "Completion_Percentage",
    "Satisfaction_Score"
]]

y = data["Completion_Status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(" \n model accuracy")
print("Accuracy:", accuracy_score(y_test, predictions))
