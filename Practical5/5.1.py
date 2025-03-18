#Create a dictionary to store five datas.
Languages_use = {'JavaScript':62.3,
             'HTML':52.9,
             'Python':51,
             'SQL':51,
             'TypeScript':38.5}
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
#To input the language we want to seek.
language=(input("Developers use language):"))
#Find the percentage of the specific language and print the result.
if language in Languages:
    print(f"The percentage of developers who use {language} is {Languages_use[language]}%")
else:
    print(f"The language {language} is not in the list.")