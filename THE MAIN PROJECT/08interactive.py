import pandas as pd
import plotly.express as px
import plotly.io as pio

pio.renderers.default = "browser"

data = pd.read_csv("data/online_learning_course_consumption_dataset.csv")

fig = px.histogram(
    data,
    x="Hours_Spent_Per_Week",
    nbins=20,
    color="Completion_Status",
    title="Interactive Histogram: Hours Spent per Week",
    opacity=0.8
)

fig.show()
