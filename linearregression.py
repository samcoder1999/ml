import pandas as pd
import numpy as np
import math
from pandas import DataFrame
data=pd.read_csv('cost-revenue-clean.csv')
x=data['production_budget_usd']
y=data['worldwide_gross_usd']
money_made=x.values
production_budget=y.values
maxim=0
for i in range(0,len(money_made)):
    if money_made[i]>maxim:
        maxim=money_made[i]
print(maxim)
max_money=maxim
#prediction
mincost=10e10
cost=0
min_slope=0
min_intercept=0
iarr=np.linspace(0.000001,3,10000)
for slope in range(0,len(iarr)):

    for intercept in range(0,maxim):
        cost=0
        for i in range(0,len(production_budget)):
            yvalue=money_made[i]
            xvalue=production_budget[i]
            ns=-1/(iarr[i])
            #error estimation
            A=np.array([[-slope,1],[-ns,1]])
            b=np.array([[intercept],[ns*xvalue+yvalue]])
            sol=np.linalg.solve(A,b)
            cost==cost+(math.sqrt(math.pow(sol[0]-xvalue,2)+math.pow(sol[1]-yvalue,2)))
        #error correction    
        if cost<mincost:
            mincost=cost
            min_slope=slope
            min_intercept=intercept
            print(min_slope,min_intercept)



print(min_slope,min_intercept)

          
                