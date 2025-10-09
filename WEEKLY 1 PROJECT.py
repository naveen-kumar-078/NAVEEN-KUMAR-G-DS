import pandas as vs
import matplotlib.pyplot as hi
nk = vs.read_csv('gender_submission.csv')
print(nk.head(40))
nk.rename(columns={"PassengerId":"Number"},inplace = True)
print(nk)
filter = nk[nk["Survived"]==1]
print(filter)
the_passed = nk["Survived"].value_counts()
total = len(nk)
died  = the_passed[0]
perc = (died/total)*100
print(f"percentages of survived: {perc:.2f}%")
the_passed.plot(kind='bar',color=["red","green"])
hi.xlabel("Status")
hi.ylabel("no of passengers")
hi.title("Titanic survival list")
hi.xticks(rotation=0)
hi.show()
