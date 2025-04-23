import os
import pandas as pd
import matplotlib.pyplot as plt
# importing the .csv file works
directory_path= 'C:\\Users\\张嘉芮1\\Desktop\\IBI1\\IBI1_2024-25\\Practical10'
os.chdir(directory_path)
print ("the path is:", os.getcwd())
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# showing the third column (the year) for the first 10 rows
first_10_years = dalys_data.iloc[:10, 2] 
print(first_10_years)

# the 10th year with DALYs data recorded in Afghanistan
afg_data = dalys_data[dalys_data['Entity'] == 'Afghanistan']
if len(afg_data) >= 10:
    year= afg_data.iloc[9, 2]  
    print(f'\n The 10th year is {year}')

#used a Boolean to show DALYs for all countries in 1990
year_1990 = dalys_data[dalys_data['Year'] == 1990]
print('DALYS for all countries in 1990:')
print(year_1990[['Entity','DALYs']])

#computed the mean DALYs in the UK and France
uk_mean_dalys = dalys_data[dalys_data['Entity'] == 'United Kingdom']['DALYs'].mean()
fr_mean_dalys = dalys_data[dalys_data['Entity'] == 'France']['DALYs'].mean()

#whether the mean DALYs in the UK was greater or smaller than France
if uk_mean_dalys > fr_mean_dalys:
    print("The average DALYs in the UK are higher than those in France.")
elif uk_mean_dalys < fr_mean_dalys:
    print("The average DALYs in the UK are lower than those in France.")
else:
    print("The average DALYs in the UK and France are equal.")

# created a plot showing the DALYS over time in the UK
uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["DALYs", "Year"]]
plt.plot(uk.Year, uk.DALYs, 'b+')
plt.title('DALYs Over Time in the United Kingdom')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.grid(True)
plt.xticks(uk.Year,rotation=-90)
plt.show()
# the answer for the question 
# created a plot showing the relationship between the DALYs in China and the UK changed over time
china = dalys_data.loc[dalys_data['Entity'] == 'China', ['Year', 'DALYs']]
comparison = pd.merge(china, uk, on='Year', suffixes=('_China', '_UK'))
plt.plot(comparison['Year'], comparison['DALYs_China'], label='China', marker='o')
plt.plot(comparison['Year'], comparison['DALYs_UK'], label='United Kingdom', marker='o')
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Comparison between China and the UK')
plt.legend()
plt.grid(True)
plt.show()
correlation = comparison['DALYs_China'].corr(comparison['DALYs_UK'])
print(f"Correlation between China and UK DALYs: {correlation:.2f}")