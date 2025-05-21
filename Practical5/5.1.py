#Create a dictionary to store five datas.
Languages_use = {'JavaScript':62.3,
             'HTML':52.9,
             'Python':51,
             'SQL':51,
             'TypeScript':38.5}
print (f'Languages use is {Languages_use}')
#Start to draw a bar.
import matplotlib.pyplot as plt
import numpy as np
#There are five bars.
N = 5
#To define the bar location on the x axis.
ind = np.arange(N)
#To list the x and y axis.
Languages = list(Languages_use.keys())
Percentages = list(Languages_use.values())
#The width of every bar.
width = 0.35
#Draw the bar.
p1 = plt.bar(Languages, Percentages, width)
#y axis
plt.ylabel('Percentages(%)')
#x axis
plt.xticks(ind,('JavaScript','HTML','Python','SQL','TypeScript'))
#the title of the bar.
plt.title('Percentages of Developers Using Different Languages')
#The range of the y axis
plt.ylim(0,70)
plt.show()
# This variable can be modified as needed
requested_language = "Python" 
if requested_language in Languages_use:
    print(f"The percentage of developers who use {requested_language} is {Languages_use[requested_language]}%")
else:
    print("The requested language is not in the list.")