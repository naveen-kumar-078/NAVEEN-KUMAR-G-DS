import matplotlib.pyplot as plt

def plot_histogram(data):
    plt.hist(data["Hours_Spent_Per_Week"], bins=10)
    plt.title("Histogram of Hours Spent Per Week")
    plt.xlabel("Hours Spent Per Week")
    plt.ylabel("Frequency")
    plt.show()
