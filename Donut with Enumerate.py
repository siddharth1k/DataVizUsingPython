# Prolog - Auto Generated #
import os, matplotlib.pyplot, uuid, pandas
os.chdir(u'C:/Users/SIDSINGH/PythonEditorWrapper_6449d26e-7817-4d78-ad43-136990c5232a')
dataset = pandas.read_csv('input_df_83027735-f011-4c8a-9fee-c29a05a574ed.csv')

matplotlib.pyplot.figure(figsize=(5.55555555555556,4.16666666666667))
matplotlib.pyplot.show = lambda args=None,kw=None: matplotlib.pyplot.savefig(str(uuid.uuid1()))
# Original Script. Please update your script content here and once completed copy below section back to the original editing window #
# The following code to create a dataframe and remove duplicated rows is always executed and acts as a preamble for your script: 

# dataset = pandas.DataFrame(total_litres_of_pure_alcohol, continent)
# dataset = dataset.drop_duplicates()

# Paste or type your script code here:
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd  

fig, ax = plt.subplots(figsize=(6, 4), subplot_kw=dict(aspect="equal"))
#ax.pie(dataset.total_litres_of_pure_alcohol,labels=dataset.continent, autopct='%1.1f%%', pctdistance=0.75, wedgeprops=dict(width=0.5), startangle=-40, explode=explode)
wedges, texts = ax.pie(dataset.total_litres_of_pure_alcohol, wedgeprops=dict(width=0.5), startangle=-40)

bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
kw = dict(xycoords='data', textcoords='data', arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

for i, p in enumerate(wedges):
    ang = (p.theta2 - p.theta1)/2. + p.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    connectionstyle = "angle,angleA=0,angleB={}".format(ang)
    kw["arrowprops"].update({"connectionstyle": connectionstyle})
    ax.annotate(dataset.continent[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                 horizontalalignment=horizontalalignment, **kw)

ax.set_title("Alcohol consumption by continent")

plt.show()

# Epilog - Auto Generated #
os.chdir(u'C:/Users/SIDSINGH/PythonEditorWrapper_6449d26e-7817-4d78-ad43-136990c5232a')
