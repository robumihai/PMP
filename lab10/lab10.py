import pymc as pm
import arviz as az
import numpy as np
import matplotlib.pyplot as plt

# 1. [span_0](start_span)Definirea datelor (extrase din tabel)[span_0](end_span)
# X = cheltuieli publicitate, Y = vanzari
x_data = np.array([1.5, 2.0, 2.3, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 
                   6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0])
y_data = np.array([5.2, 6.8, 7.5, 8.0, 9.0, 10.2, 11.5, 12.0, 13.5, 14.0, 
                   15.0, 15.5, 16.2, 17.0, 18.0, 18.5, 19.5, 20.0, 21.0, 22.0])

# 2. [span_1](start_span)Construirea modelului Bayesian[span_1](end_span)
with pm.Model() as model_regresie:
    # a) Definire prior-uri (distributii a priori)
    # alpha = intercept, beta = panta, sigma = eroare/zgomot
    alpha = pm.Normal('alpha', mu=0, sigma=10)
    beta = pm.Normal('beta', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=10)

    # Relatia liniara determinista: mu = alpha + beta * X
    mu = alpha + beta * x_data

    # Likelihood (distributia observatiilor reale)
    y_obs = pm.Normal('y_obs', mu=mu, sigma=sigma, observed=y_data)

    # Esantionare MCMC (antrenarea modelului)
    # Se fac 2000 de pasi de "tune" si 2000 de extrageri efective
    idata = pm.sample(2000, tune=2000, return_inferencedata=True, random_seed=42)

# 3. [span_2](start_span)Afisarea rezultatelor pentru coeficienti (Cerintele a si b)[span_2](end_span)
# 'mean' este estimarea, 'hdi_3%' si 'hdi_97%' sunt intervalele de credibilitate
print("Rezumat parametrii (alpha, beta, sigma):")
summary = az.summary(idata, var_names=['alpha', 'beta', 'sigma'], hdi_prob=0.95)
print(summary)

# 4. Predictie pentru o valoare noua (Cerinta c)
# Calculam manual predictia folosind distributia posterioara (trace)
# Sa zicem ca vrem predictie pentru 12.0 (mii $) investitie
x_nou = 12.0
posterior = idata.posterior

# Generam distributia posibila a vanzarilor
y_pred_dist = posterior['alpha'] + posterior['beta'] * x_nou

print(f"\n--- Predictie pentru investitie de {x_nou} ---")
print(f"Vanzari estimate (medie): {y_pred_dist.mean().values:.2f}")

# Calculam intervalul HDI de 95% pentru aceasta predictie
hdi_pred = az.hdi(y_pred_dist, hdi_prob=0.95)
print(f"Interval de incredere 95%: {hdi_pred['x'].values}")

# 5. Vizualizare grafica (Optional)
plt.figure(figsize=(10, 6))
# Punctele reale
plt.scatter(x_data, y_data, c='black', label='Date reale')
# Linia de regresie medie
avg_alpha = summary.loc['alpha', 'mean']
avg_beta = summary.loc['beta', 'mean']
plt.plot(x_data, avg_alpha + avg_beta * x_data, c='red', label=f'Regresie: y={avg_alpha:.2f} + {avg_beta:.2f}x')
plt.xlabel('Publicitate')
plt.ylabel('Vanzari')
plt.legend()
plt.title('Regresie Liniara Publicitate vs Vanzari')
plt.show()
