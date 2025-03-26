# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm 
#Function Definition which have N,I1,R1,beta, gamma, vaccination_rate, times=1000
#S=susceptible, I=infected, R=recovered,V=vaccination
#loop over 1000 time points.
#Caculate the number of the people who was infected newly and the people who recover newly.
#list the results of S1,I1,R1,V1 and add them into arrays.
#return four lists, each containing the number of susceptible individuals, infected individuals, recovered individuals, and vaccinated individuals for each time.
def sir_model(N, I1, R1, beta, gamma, vaccination_rate, times=1000):
    S1 = N - I1 - R1 - int(vaccination_rate * N)
    S, I, R, V = [S1], [I1], [R1], [int(vaccination_rate * N)]
    V1=0
    for t in range(1, times):
        new_infections = beta * S1 * (I1 / N) 
        new_recoveries = gamma * I1
        S1=S1- new_infections
        I1=I1 + new_infections - new_recoveries
        R1=R1+new_recoveries
        V1=V1
        S.append(S1)
        I.append(I1)
        R.append(R1)
        V.append(V1)
    return S, I, R, V
#N is the total number of people in the population.
#S=susceptible, I=infected, R=recovered, this 1 means initial value.
#generate 11 equidistant values from 0 to 1, representing different vaccination rates.
#beta is  an infection probability and gamma is the recovery probability.
N=10000
I1=1
R1=0
vaccination_rates = np.linspace(0, 1, 11)
beta=0.3
gamma=0.05
plt.figure(figsize=(10, 6))
#use sir model to run this.
times=1000
for int, vaccination_rate in enumerate(vaccination_rates):
    S, I, R, V = sir_model(N, I1, R1, beta, gamma, vaccination_rate,times)
    color = cm.viridis(int / len(vaccination_rates))  
    plt.plot(I, label=f'{vaccination_rate*100}%', color=color)
#plot a picture.
plt.xlabel('Time step')
plt.ylabel('Number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()
 