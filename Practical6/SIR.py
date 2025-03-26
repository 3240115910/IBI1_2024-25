#import necessary libraries
import numpy as np
import matplotlib . pyplot as plt
#N is the total number of people in the population.
#S=susceptible, I=infected, R=recovered, this 1 means initial value.
#beta is an infection probability and gamma is the recovery probability.
N=10000
I1=1
S1=N-I1
R1=0
beta=0.3
gamma=0.05
S=[]
I=[]
R=[]
S.append(S1)
I.append(I1)
R.append(R1)
#loop over 1000 time points.
#Caculate the number of the people who was infected newly and the people who recover newly.
#list the results of S1,I1,R1 and add them into arrays.
times=1000
for t in range (times):
    NewI= beta*S1*(I1/N)
    NewR= gamma*I1
    S1=S1-NewI
    I1=I1-NewR+NewI
    R1=R1+NewR
    S.append(S1)
    I.append(I1)
    R.append(R1)
t=t+1
print (S,I,R)
#plot a picture.
plt.figure(figsize=(6,4), dpi=150)
plt.plot(S, label='susceptible')
plt.plot(I, label='infected')
plt.plot(R, label='recovered')
plt.xlabel('Times')
plt.ylabel('Number of people')
plt.title('SIR')
plt.legend()
plt.savefig('SIR.png', format='png')
plt.show()