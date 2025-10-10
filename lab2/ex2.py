import numpy as np
import matplotlib.pyplot as plt

lambdas = [1, 2, 5, 10]
n = 1000

# 1.
data_fixed = [np.random.poisson(lam, n) for lam in lambdas]

# 2.
random_lambdas = np.random.choice(lambdas, size=n)
data_random = np.array([np.random.poisson(lam) for lam in random_lambdas])

# 3.
plt.figure(figsize=(12, 8))
for i, lam in enumerate(lambdas):
	plt.subplot(2, 3, i+1)
	plt.hist(data_fixed[i], bins=range(0, max(data_fixed[i])+2), alpha=0.7, color='skyblue', edgecolor='black')
	plt.title(f'Poisson(λ={lam})')
	plt.xlabel('Number of calls')
	plt.ylabel('Frequency')
    
plt.subplot(2, 3, 5)
plt.hist(data_random, bins=range(0, max(data_random)+2), alpha=0.7, color='salmon', edgecolor='black')
plt.title('Randomized λ')
plt.xlabel('Number of calls')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()
