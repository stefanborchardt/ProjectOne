# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:18:05 2015

@author: Stefan
"""
import pandas
from ggplot import *
from scipy.stats import ttest_rel

if __name__ == "__main__":
    # load csv
    data = pandas.read_csv('stroopdata.csv')
    # description of data
    print(data.describe())
    # handle categorical variable by adding dummy 
    data = pandas.melt(data)
    data.columns = {'Congruence', 'Time'}

    # two plots
    print(ggplot(data, aes(x='Time', fill='Congruence', color='Congruence')) + \
    geom_histogram(binwidth=1, alpha=0.6) + labs(title='Number of Measurements in 1-second intervals'))   
    
    print(ggplot(data, aes(x='Time', color='Congruence')) + \
    geom_density()  + labs(title='Density of Measurements'))  
    
    # perform two-tailed test for dependent samples
    t, p = ttest_rel(data[data.Congruence=='Congruent']['Time'], \
    data[data.Congruence==' Incongruent']['Time'])
    # convert p to one-sided
    p = p / 2
    print('t value: {0}, one-sided p value: {1}'.format(t, p))
    
    
 
   