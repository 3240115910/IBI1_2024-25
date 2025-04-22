import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
directory_path= 'C:\\Users\\张嘉芮1\\Desktop\\IBI1\\IBI1_2024-25\\Practical10'
os.chdir(directory_path)
print ("the path is:", os.getcwd())
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.head(5))
print(dalys_data.info())
dalys= dalys_data['DALYs'].describe()
max_dalys = dalys['max']
min_dalys = dalys['min']
first_year = dalys_data['Year'].min()
last_year = dalys_data['Year'].max()
print(f"Max dalys: {max_dalys}")
print(f"Min dalys: {min_dalys}")
print(f"First year with dalys data: {first_year}")
print(f"Last year with dalys data: {last_year}")
print(dalys_data.iloc[0,3])
first_10_years = dalys_data.iloc[:10, 3] 
print(first_10_years)
afg_data = dalys_data[dalys_data['Entity'] == 'Afghanistan']
if len(afg_data) >= 10:
    year= afg_data.iloc[9, 3]  
    print(f"\n The 10th year is {year}")
year_1990 = dalys_data[dalys_data["Year"] == 1990]
print(year_1990["DALYs"])
uk = dalys_data.loc[dalys_data["Entity"] == "United Kingdom", ["DALYs", "Year"]]
plt.plot(uk["Year"], uk["DALYs"], 'b+')
plt.title('DALYs Over Time in the United Kingdom')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.grid(True)
plt.show()
