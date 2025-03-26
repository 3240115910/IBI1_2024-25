import numpy as np
import matplotlib.pyplot as plt
# Initialize population array
population = np.zeros((100, 100))
# Randomly select the coordinates for the initial infected individual
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
beta = 0.1  # Infection probability
gamma = 0.05  # Recovery rate
times = 100
#make sure it can run 100 times
for t in range(times+1):
    # Find all infected individuals
    infected = np.argwhere(population == 1)
    # Infect neighbours
    for ag in infected:
        x, y = ag
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue#it can not infect itself
                x1, y1 = x + dx, y + dy
                if 0 <= x1 < 100 and 0 <= y1 < 100 and population[x1, y1] == 0:
                    if np.random.rand() < beta:
                        population[x1, y1] = 1
    
    # Recover infected individuals
    for ag in infected:
        x, y = ag
        if np.random.rand() < gamma:
            population[x, y] = 2
    
    # Plot the updated state
    if t in [0,10,50,100]:
        plt.figure(figsize=(6, 4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f"Time {t}")
        plt.colorbar()
        plt.show()