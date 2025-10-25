#  importing necessary packages

import pandas as pd 
import requests
import numpy as np
from IPython.display import display
from io import StringIO

from dstapi import DstApi # The helper class
# Define the query parameters 
query = {
    "table": "PRIS113",
    "format": "JSON"
}

url = "https://api.statbank.dk/v1/data"

response = requests.post(url, json=query)
data = response.json()
pris113_api=DstApi('PRIS113')
params=pris113_api._define_base_params(language='en')
pris113_dat=pris113_api.get_data(params=params)
print(pris113_dat.head())
metadata = pris113_dat.rename(columns={"TID": "date", "INDHOLD": "CPI", "TYPE": "type"})

#structuriing the date variable and converting to datetime
metadata['date'] = pd.to_datetime(metadata['date'], format='%YM%m')
metadata = metadata.sort_values('date')

# Ensure CPI column is numeric
metadata['CPI'] = pd.to_numeric(metadata['CPI'], errors='coerce')

#Set the CPI index to 100 in 2020
metadata['year'] = metadata['date'].dt.year
cpi_2020_mean = metadata.loc[metadata['year'] == 2020, 'CPI'].mean()
metadata['CPI_indexed'] = metadata['CPI'] / cpi_2020_mean * 100
metadata.head()
print(metadata.to_string(index=False))
#Calculate Month-to-Month Inflation Rate
metadata['MoM_inflation'] = metadata['CPI_indexed'].pct_change() * 100
print(metadata[['date', 'CPI_indexed', 'MoM_inflation']].head(15))
print(metadata.to_string(index=False))
#Calculate 12-Month Inflation Rate
metadata['YoY_inflation'] = metadata['CPI_indexed'].pct_change(periods=12) * 100
print(metadata[['date', 'CPI_indexed', 'YoY_inflation']].head(15))
print(metadata.to_string(index=False))

#plot the inflation rates

import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))
plt.plot(metadata['date'], metadata['CPI_indexed'], label='CPI (2020=100)')
plt.title('Consumer Price Index in Denmark, Indexed to 2020')
plt.xlabel('Year')
plt.xlim(pd.to_datetime('2000-01-01'), pd.to_datetime('2025-12-31'))
plt.ylabel('CPI (2020=100)')
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
plt.plot(metadata['date'], metadata['MoM_inflation'], label='Month-to-Month Inflation Rate')
plt.title('Month-to-Month Inflation Rate')
plt.xlabel('Year')
plt.xlim(pd.to_datetime('2000-01-01'), pd.to_datetime('2025-12-31'))
plt.ylabel('Inflation Rate')
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
plt.plot(metadata['date'], metadata['YoY_inflation'], label='Year-over-Year Inflation Rate')
plt.title('12-Month Inflation Rate')
plt.xlabel('Year')
plt.xlim(pd.to_datetime('2000-01-01'), pd.to_datetime('2025-12-31'))
plt.ylabel('Inflation Rate')
plt.legend()
plt.show()

# Find when the 12-month rate drops below a threshold of 3 % after 2020
metadata_post2020 = metadata[metadata['date'] >= pd.to_datetime('2020-01-01')]
peak_date = metadata_post2020.loc[metadata_post2020['YoY_inflation'].idxmax(), 'date']
metadata_after_peak = metadata_post2020[metadata_post2020['date'] > peak_date]
end_surge_date = metadata_after_peak.loc[metadata_after_peak['YoY_inflation'] < 3, 'date'].min()
print(f"Post-pandemic inflation surge ended around: {end_surge_date}")

# Instantaneous Inflation Calculation
T = 12  # 12 months 

import matplotlib.pyplot as plt
import numpy as np

def compute_kappa(T=12, alpha=0):
    ks = np.arange(0, T)
    numer = (T - ks) ** alpha
    denom = numer.sum() 
    kappa = T * numer / denom
    return kappa

def plot_kappas(T=12, alphas=(0, 1, 2, 3), figsize=(8, 4)):
    ks = np.arange(0, T)
    plt.figure(figsize=figsize)
    for alpha in alphas:
        kappa = compute_kappa(T=T, alpha=alpha)
        plt.plot(ks, kappa, marker='o', label=f'alpha={alpha}')
    plt.gca().invert_xaxis()  # show k=0 (most recent) on the left (optional)
    plt.xticks(ks)
    plt.xlabel('k (0 = current month, 11 = 11 months ago)')
    plt.ylabel('κ(k, α)')
    plt.title(f'κ(k, α) for T={T}')
    plt.legend()
    plt.grid(True)
    plt.show()
    plot_kappas(T=12, alphas=(0, 1, 2, 3))  