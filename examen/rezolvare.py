import pandas as pd
import numpy as np
import pymc as pm
import arviz as az
import matplotlib.pyplot as plt
import seaborn as sns

#1.incarcam datele
df=pd.read_csv('bike_daily.csv')
sns.pairplot(df[['temp_c','humidity','wind_kph','rentals']])
plt.show()

#2.
#a)standardizare
features=['temp_c','humidity','wind_kph']
df_std=df.copy()
df_std[features]=(df[features]-df[features].mean())/df[features].std()
df_std['temp_c2']=df_std['temp_c']**2

#b),c)
with pm.Model() as model_linear:
    alpha=pm.Normal('alpha',mu=0,sigma=10)
    betas=pm.Normal('betas',mu=0,sigma=10,shape=3)
    sigma=pm.Exponential('sigma',1)

    mu=alpha+betas[0]*df_std['temp_c']+betas[1]*df_std['humidity']+betas[2]*df_std['wind_kph']
    y=pm.Normal('y',mu=mu,sigma=sigma,observed=df['rentals'])
    trace_linear=pm.sample(2000,tune=1000,target_accept=0.9)

with pm.Model() as model_poly:
    alpha=pm.Normal('alpha',mu=0,sigma=10)
    betas=pm.Normal('betas',mu=0,sigma=10,shape=4)
    sigma=pm.Exponential('sigma',1)
    
    mu=alpha+betas[0]*df_std['temp_c']+betas[1]*df_std['humidity']+betas[2]*df_std['wind_kph']+betas[3]*df_std['temp_c2']
    y=pm.Normal('y',mu=mu,sigma=sigma,observed=df['rentals'])
    trace_poly=pm.sample(2000,tune=1000,target_accept=0.9)