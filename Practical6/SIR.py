import numpy as np
import matplotlib . pyplot as plt
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