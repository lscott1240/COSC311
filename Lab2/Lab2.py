import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

SBA_Region = pd.read_csv('Sidi-Bel_Abbes_Region.csv')
B_Region = pd.read_csv('Bejaia_Region.csv')

# Task 1 : Show Info(), Describe(), 'Ws', count() of both data sets

SBA_Region.info()
B_Region.info()

B_DF = pd.DataFrame(B_Region)
SBA_DF = pd.DataFrame(SBA_Region)

print(SBA_Region.describe(), '\n')
print(B_Region.describe(), '\n')

print(SBA_Region[' Ws'], '\n')
print(B_Region[' Ws'], '\n')

print(SBA_Region.count(), '\n')
print(B_Region.count(), '\n')

# Gathers the mean of all temperatures based on month
temperature_mean = B_Region.groupby('month')[['Temperature']].mean().sort_values('month')

# Creates a list of integers referencing months from the data set
months = Counter(B_Region['month'])

# Task 2 = Show line graph of average temperature change by month
plt.plot(months.keys(), temperature_mean, color='green', marker='o', linestyle='solid')
plt.title('Temperature Change by Month in Bejaia Region')
plt.ylabel('Temperature (Celcius)')
plt.xlabel('Months June - September')
plt.xticks([6, 7, 8, 9])
plt.show()

# Task 3 = Create scatter plot for temperature based on Fire Weather Index
SBA_Region.plot.scatter(x = 'Temperature', y = 'FWI')
plt.show()

# Task 4 = Draw a historgram of average Relative Humidity by month
B_DF[' RH'].plot(kind = 'hist', bins = 4, color = 'orange', edgecolor = 'black')
plt.grid(visible = True)
plt.title('Relative Humidity for each month')
plt.xlabel('Months June - September')
plt.ylabel('Relative Humidity')
plt.ylim(20, 40)
plt.show()

'''
b_rh = B_DF.groupby('month')[' RH'].mean()
plt.bar(b_rh.keys(), b_rh, color = 'orange', edgecolor = 'black')
plt.title('Relative Humidity for each month')
plt.xlabel('Months June - September')
plt.ylabel('Relative Humidity')
plt.xticks([6,7,8,9])
plt.ylim(50, 75)
plt.show()
'''

# Task 5 = Draw a bar graph to show maximum rain amount for each month
b_max_rain = B_DF.groupby('month')['Rain '].max()
plt.bar(b_max_rain.keys(), b_max_rain, color = 'darkblue', edgecolor = 'black')
plt.title('Maximum Rain Amount per Month')
plt.xlabel('Months June - September')
plt.ylabel('Amount of Rain')
plt.xticks([6, 7, 8, 9])
plt.show()

# Task 6 = Draw a histogram of Windspeed in the month of June
(SBA_DF[' Ws'][SBA_DF['month'] == 6]).hist(bins = 5, color = 'lightblue', edgecolor = 'black')
plt.show()

# Task 7 = Draw a line figure that shows correlation between Temperature and Relative Humidity
SBA_Temp = (SBA_DF[' RH'][SBA_DF['month'] == 7])
SBA_RH = (SBA_DF['Temperature'][SBA_DF['month'] == 7])
xs = [i for i, _ in enumerate(SBA_Temp)]

plt.plot(xs, SBA_Temp,  'g-',   label = 'Temperature')
plt.plot(xs, SBA_RH,    'r-.',  label = 'Rain Humidity')

plt.xticks([])
plt.title('Rain Hmidity and Temperature Correlation')
plt.show()

# Task 8 = Draw a bar graph to show the distribution of Relative Humidity
values = Counter(min(humid // 10 * 10, 90) for humid in B_DF[' RH'])

plt.bar([x + 5 for x in values.keys()], values.values(), 10, edgecolor = 'black', color = 'red')
plt.axis([35, 95, 0, 45])
plt.xticks([10 * i for i in range(4, 10)])
plt.xlabel('Decile')
plt.ylabel('Number of Days')
plt.title('Distribution of Relative Humidity')
plt.show()

# Task 9 = Draw a figure to show average temperature for each month with fires and no fires
fire = B_DF.groupby(['month', 'Classes  '])['Temperature'].mean()
fire.plot(x = 'month', y = 'Temperature', kind = 'bar',\
          color = ['orange','lightgreen'], edgecolor = 'black', ylim=(25,35),\
          xlabel = 'Months by Fire', ylabel = 'Temperature', title = 'Average Temperature By Month Based on Fires')
