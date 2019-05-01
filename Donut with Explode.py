# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(total_litres_of_pure_alcohol, continent)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd  

fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))
explode = (0, 0, 0.15, 0, 0, 0)
ax.pie(dataset.total_litres_of_pure_alcohol,labels=dataset.continent, autopct='%1.1f%%', pctdistance=0.75, wedgeprops=dict(width=0.5), startangle=-40, explode=explode)
ax.set_title("Alcohol consumption by continent")
plt.show()
