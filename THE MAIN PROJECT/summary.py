def basic_info(data):
    print("Basic Info:")
    print(data.info())
    print(data.head())


def statistics(data):
    print("\nStatistics:")
    print(data.describe())


def missing_val(data):
    print("\nMissing Values:")
    print(data.isnull().sum())


def outlier(data):
    Q1 = data["Hours_Spent_Per_Week"].quantile(0.25)
    Q3 = data["Hours_Spent_Per_Week"].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    data = data[
        (data["Hours_Spent_Per_Week"] >= lower) &
        (data["Hours_Spent_Per_Week"] <= upper)
    ]
    return data
