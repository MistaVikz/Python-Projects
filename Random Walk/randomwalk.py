# Simulate a random walk and plot the distribution of results
import numpy as np
import matplotlib.pyplot as plt

# Setup
np.random.seed(123)
plt.clf()

# Iniialize game results list
all_walk=[]

for i in range(5000):
    # Initialize Random Walk
    random_walk = [0]

    # Next Step in Walk
    for x in range(100):
        # Initialize and roll dice
        step=random_walk[-1]
        dice = np.random.randint(1,7)

        # Game Control
        if dice <= 2:
            step=max(0,step-1)
        elif dice > 2 and dice < 6:
            step=step+1
        else:
            step=step + np.random.randint(1,7)

        # Add chance of returning back to the beginning
        if np.random.rand() <= 0.005 :
            step=0
        
        # Append Next Step
        random_walk.append(step)

    # Append Final Result
    all_walk.append(random_walk)
    
# Select last row from transpose
np_aw_t = np.transpose(np.array(all_walk))
ends = np_aw_t[-1,:]

# Display distribution of results
plt.hist(ends)
plt.show()
