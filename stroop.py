# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:18:05 2015

@author: Stefan
"""
import pandas
import statsmodels.api as sm
from matplotlib import pyplot as plt
from ggplot import *
from scipy.stats import ttest_rel, shapiro, t as ttest

if __name__ == "__main__":
    # load csv
    data = pandas.read_csv('stroopdata.csv')

    # description of data
    print(data.describe())
    
    # handle categorical variable by adding dummy 
    data = pandas.melt(data)
    data.columns = {'Congruence', 'Time'}
    
    # test for normality with Shapiro-Wilk test an verify with Q-Q plot
    probplot = sm.ProbPlot(data['Time'])
    probplot.qqplot()
    plt.show()
    W, p = shapiro(data['Time'])
    print('p for Shapiro-Wilk test: {0}'.format(p))
 
    # two plots
    print(ggplot(data, aes(x='Time', fill='Congruence', color='Congruence')) + \
    geom_histogram(binwidth=1, alpha=0.6) + labs(title='Number of Measurements in 1-second intervals'))   
    
    print(ggplot(data, aes(x='Time', color='Congruence')) + \
    geom_density()  + labs(title='Density of Measurements'))  
    
    congruent = data[data.Congruence=='Congruent']['Time']
    incongruent = data[data.Congruence==' Incongruent']['Time']
    
    # perform two-tailed test for dependent samples
    t, p = ttest_rel(incongruent, congruent)
    # convert p to one-sided
    p = p / 2
    print('t value: {0}, one-sided p value: {1}'.format(t, p))
    
    # obtain critical value - already one-sided
    critical = ttest.ppf(0.01, len(congruent)-1)
    print('t-critical value at alpha=0.01: {0}'.format(critical))
    
    
 
   