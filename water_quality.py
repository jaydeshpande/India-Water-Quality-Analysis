import pandas as pd
import matplotlib.pyplot as plt
def mask(df, key, value):
	return df[df[key] == value]
pd.DataFrame.mask = mask;
#Mask can filter out rows for a given key and value
pd09=pd.read_csv('QUALITY_AFFECTED_HABITATIONS_AS_ON_1_APR_09.csv') #data series for 2009
pd10=pd.read_csv('QUALITY_AFFECTED_HABITATIONS_AS_ON_1_APR_10.csv') #data series for 2010
pd11=pd.read_csv('QUALITY_AFFECTED_HABITATIONS_AS_ON_1_APR_11.csv') #data series for 2011
pd12=pd.read_csv('QUALITY_AFFECTED_HABITATIONS_AS_ON_1_APR_12.csv') #data series for 2012

states_list = (pd09['State Name']).tolist() #converts series object to list 
quality_list = (pd09['Quality Parameter']).tolist()

states =[]
for i in states_list:
  if i not in states:
    states.append(i)
#states creates a list of all states -- removes repeats from the original list object

quality=[]
for i in quality_list:
  if i not in quality:
    quality.append(i)
#quality creates a list of all quality parameters -- removes repeats from the original list

for i in states:
	l09 = len(pd09.mask('State Name', i).index) # .index returns major length of dataframe
	l10 = len(pd10.mask('State Name', i).index)
	l11 = len(pd11.mask('State Name', i).index)
	l12 = len(pd12.mask('State Name', i).index)
	print i
	print [l09, l10, l11, l12] # this is printing out affected cases over time 

for i in quality:
	l09 = len(pd09.mask('Quality Parameter', i).index) # .index returns major length of dataframe
	l10 = len(pd10.mask('Quality Parameter', i).index)
	l11 = len(pd11.mask('Quality Parameter', i).index)
	l12 = len(pd12.mask('Quality Parameter', i).index)
	print i
	print [l09, l10, l11, l12] # this is printing out affected cases over time
	