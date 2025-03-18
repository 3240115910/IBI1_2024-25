#The data of the population in two countries.
UK_countries_population=[57.11,3.13,1.91,5.45] 
China_provinces_population = [65.77, 41.88, 45.28, 61.27, 85.15]
#The area and the provinces in these two countries
UK_countries=['England', 'Wales', 'Northern	Ireland', 'Scotland']
China_provinces=['Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu']
#print the sorted result
print("Sorted populations of UK countries (in millions):", sorted (UK_countries_population))
print("Sorted populations of Zhejiang-neighbouring provinces (in millions):", sorted (China_provinces_population))
#start to draw two pie
import matplotlib.pyplot as plt
#set up the labels, sizes, explode for the first pie
labels = 'England','Wales','Northern Ireland','Scotland'
sizes = [57.11, 3.13, 1.91, 5.45]
explode = (0,0,0,0)
plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%',shadow=True,startangle=100)
plt.axis('equal')
plt.title('Population Sizes in UK')
plt.show()
#set up these information for the second pie
labels = 'Zhejiang', 'Fujian', 'Jiangxi', 'Anhui', 'Jiangsu'
sizes = [65.77, 41.88, 45.28, 61.27, 85.15]
explode = (0,0.1,0.2,0,0.1)
plt.pie(sizes, explode=explode, labels=labels,autopct='%1.1f%%',shadow=False,startangle=80)
plt.axis('equal')
plt.title('Population Sizes in China')
plt.show()