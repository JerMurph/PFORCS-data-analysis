import seaborn
import pandas
import matplotlib.pyplot as plt
seaborn.set_style("whitegrid")
csv = pandas.read_csv("yearly_csv.csv")
res = seaborn.pointplot(x=csv['Country'], y=csv['Value'])
plt.show()