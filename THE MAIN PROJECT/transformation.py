from sklearn.preprocessing import StandardScaler

def transform(data):
    scaler = StandardScaler()

    data["Hours_Spent_Per_Week"] = scaler.fit_transform(
        data[["Hours_Spent_Per_Week"]]
    )
    data["Course_Duration_Weeks"] = scaler.fit_transform(
        data[["Course_Duration_Weeks"]]
    )
    data["Completion_Percentage"] = scaler.fit_transform(
        data[["Completion_Percentage"]]
    )
    data["Satisfaction_Score"] = scaler.fit_transform(
        data[["Satisfaction_Score"]]
    )

    return data
    