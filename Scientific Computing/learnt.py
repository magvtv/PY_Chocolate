
# #import matplotlib as mtp
# #import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#import seaborn.objects as so
# #sns.set_theme()


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 16:56:52 2023

@author: pharoh
"""

# mplt.figure(figsize=(60, 10))
# data = pds.read_csv("gapminder.csv", )
# title = ["Country", "Continent", "Yr", "LifeExp", "Population", "GDP"]
# data_2007 = data[data["Yr" == 2007]]

# sns.set_theme(palette=None, style="darkgrid")
# sns.violinplot(data=data_2007, x="Country", y = "Population")


#data_2007 = data[data["Yr"] == 2007]
plt.figure(figsize=(30, 10))
titles = ["Yr", "Continent", "Population", "LifeExp", "Country", "GDP"]
stats = pd.read_csv('gapminder.csv', usecols = titles)
sns.set_theme()
#so.Plot(
#    x = "Year",
#    y = "Life Expectancy"
#    color = "Country"
#).add(so.Line())

sns.relplot(
    data = stats,
    x = "LifeExp",
    y = "Continent",   
)







#fig, noma = plt.subplots()
#noma.violinplot(data_2007, showextrema=False)


"""
    Plotting code
"""
#plt.xlabel('Countries')
#plt.ylabel('Population')
#plt.xticks(rotation = -90)
#plt.title("Sample Report For 2007", fontsize=20)
#plt.plot(data_2007.Country, data_2007.Population)




#plt.show()

#vdata = []
#vdata.append(data["LifeExp"])
#vdata.append(data["Population"])
#vdata.append(data["GDP"])


# # Create a random dataset across several variables
# #rs = np.random.default_rng(0)
# #n, p = 40, 8
# #d = rs.normal(0, 2, (n, p))
# #d += np.log(np.arange(1, p + 1)) * -5 + 10

# # Show each distribution with both violins and points
# #sns.violinplot(data=violin_data, palette="light:g", inner="points", orient="h")