import stats as st

import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter

SBA_Region = pd.read_csv('Sidi-Bel_Abbes_Region.csv')
B_Region = pd.read_csv('Bejaia_Region.csv')

B_DF = pd.DataFrame(B_Region)
SBA_DF = pd.DataFrame(SBA_Region)

# Task 1 - Calculate and draw bar graphs for means of "Temperature", "RH", "Ws","Rain"

B_Temp_Fire = st.mean((B_Region['Temperature'][B_Region['Classes'] == 'fire']).to_numpy())
B_Temp_NotFire = st.mean((B_Region['Temperature'][B_Region['Classes'] == 'not fire']).to_numpy())
B_RH_Fire = st.mean((B_Region['RH'][B_Region['Classes'] == 'fire']).to_numpy())
B_RH_NotFire = st.mean((B_Region['RH'][B_Region['Classes'] == 'not fire']).to_numpy())
B_Ws_Fire = st.mean((B_Region['Ws'][B_Region['Classes'] == 'fire']).to_numpy())
B_Ws_NotFire = st.mean((B_Region['Ws'][B_Region['Classes'] == 'not fire']).to_numpy())
B_Rain_Fire = st.mean((B_Region['Rain'][B_Region['Classes'] == 'fire']).to_numpy())
B_Rain_NotFire = st.mean((B_Region['Rain'][B_Region['Classes'] == 'not fire']).to_numpy())

'''
B_RH = B_DF.groupby('Classes')['RH'].mean()
B_Ws = B_DF.groupby('Classes')['Ws'].mean()
B_Rain = B_DF.groupby('Classes')['Rain'].mean()
'''

fig, ax = plt.subplots(2, 2)

# Temperature
ax[0, 0].bar(['fire', 'not fire'], [B_Temp_Fire, B_Temp_NotFire], edgecolor = 'black', color = ['orange', 'lightgreen'])
ax[0, 0].set_ylabel('Temperature (C)')
ax[0, 0].set_ylim(25, 35)

# RH
ax[0, 1].bar(['fire', 'not fire'], [B_RH_Fire, B_RH_NotFire], edgecolor = 'black', color = ['orange', 'lightgreen'])
ax[0, 1].set_ylabel('Relative Humidity')
ax[0, 1].set_ylim(60, 75)

# Ws
ax[1, 0].bar(['fire', 'not fire'], [B_Ws_Fire, B_Ws_NotFire], edgecolor = 'black', color = ['orange', 'lightgreen'])
ax[1, 0].set_ylabel('Wind Speed')
ax[1, 0].set_ylim(15, 17)

# Rain
ax[1, 1].bar(['fire', 'not fire'], [B_Rain_Fire, B_Rain_NotFire], edgecolor = 'black', color = ['orange', 'lightgreen'])
ax[1, 1].set_ylabel('Rain (inches)')
fig.subplots_adjust(wspace = 0.5, hspace = 0.5)
fig.suptitle('Bejaia Region Statistics')
plt.show()


# Task 2 - Show median values for "FFMC", "DMC", "DC", and "ISI"

print('\nSidi-Bel Region Medians :',
      '\nFFMC =', st.median(SBA_DF['FFMC']),
      '\nDMC =', st.median(SBA_DF['DMC']),
      '\nDC =', st.median(SBA_DF['DC']),
      '\nISI =', st.median(SBA_DF['ISI']))


# Task 3 - Show 25, 60, and 75 percent quartiles for "Temperature", "RH", "Ws", and "Rain"

# Temperature
print('\nBejaia Region Quartiles for Temperature :',
      '\n25 % Quartile -', st.quantile(B_DF['Temperature'], 0.25),
      '\n60 % Quartile -', st.quantile(B_DF['Temperature'], 0.60),
      '\n75 % Quartile -', st.quantile(B_DF['Temperature'], 0.75))

# RH
print('\nBejaia Region Quartiles for Relative Humidity :',
      '\n25 % Quartile -', st.quantile(B_DF['RH'], 0.25),
      '\n60 % Quartile -', st.quantile(B_DF['RH'], 0.60),
      '\n75 % Quartile -', st.quantile(B_DF['RH'], 0.75))

# Ws
print('\nBejaia Region Quartiles for Wind Speed :',
      '\n25 % Quartile -', st.quantile(B_DF['Ws'], 0.25),
      '\n60 % Quartile -', st.quantile(B_DF['Ws'], 0.60),
      '\n75 % Quartile -', st.quantile(B_DF['Ws'], 0.75))

# Rain
print('\nBejaia Region Quartiles for Rain :',
      '\n25 % Quartile -', st.quantile(B_DF['Rain'], 0.25),
      '\n60 % Quartile -', st.quantile(B_DF['Rain'], 0.60),
      '\n75 % Quartile -', st.quantile(B_DF['Rain'], 0.75))


# Task 4 - Find the standard deviation of "Temperature", "Rain", "BUI", and "FWI"

print('\nSidi-Bel Region Standard Deviations :',
      '\nTemperature =', st.std(SBA_DF['Temperature']),
      '\nRain =', st.std(SBA_DF['Rain']),
      '\nBUI =', st.std(SBA_DF['BUI']),
      '\nFWI =', st.std(SBA_DF['FWI']),)


# Task 5 - Show correlation between "RH" and all other statistical data"

print('\nBejaia Region Dataset Correlatoin Coefficient between RH and other statistics :',
      '\nTemperature = ', st.correlation(B_DF['RH'], B_DF['Temperature']),
      '\nWs = ', st.correlation(B_DF['RH'], B_DF['Ws']),
      '\nRain = ', st.correlation(B_DF['RH'], B_DF['Rain']),
      '\nFFMC = ', st.correlation(B_DF['RH'], B_DF['FFMC']),
      '\nDMC = ', st.correlation(B_DF['RH'], B_DF['DMC']),
      '\nDC = ', st.correlation(B_DF['RH'], B_DF['DC']),
      '\nISI = ', st.correlation(B_DF['RH'], B_DF['ISI']),
      '\nBUI = ', st.correlation(B_DF['RH'], B_DF['BUI']),
      '\nFWI = ', st.correlation(B_DF['RH'], B_DF['FWI']))

print('\nStrongest positive correlation of RH is with Rain:\n',
      st.correlation(B_DF['RH'], B_DF['Rain']),
      '\nStrongest negative correlation of RH is with Temperature:\n',
      st.correlation(B_DF['RH'], B_DF['Temperature']))

fire = B_DF.groupby(['month', 'Classes'])['Temperature'].mean()
fire.plot(x = 'month', y = 'Temperature', kind = 'bar',\
          color = ['orange','lightgreen'], edgecolor = 'black', ylim=(25,35),\
          xlabel = 'Months by Fire', ylabel = 'Temperature', title = 'Average Temperature By Month Based on Fires')
