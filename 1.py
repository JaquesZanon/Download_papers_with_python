# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:32:40 2021

@author: jaques
"""



!pip3 install -U scidownl

scidownl -l

from scidownl.scihub import *
import numpy as np
import pandas as pd

DOI = "10.1016/j.marpolbul.2016.08.011"
out = 'paper'
sci = SciHub(DOI, out).download(choose_scihub_url_index=3)
sci
DOIs = [...]
out = 'paper'
for i in range(0,1,1): 
    SciHub(DOIS[i], out).download(choose_scihub_url_index=3)
  
for doi in DOIS: 
    SciHub(doi, out).download(choose_scihub_url_index=3)
    
for doi in DOIS:
    try:
        SciHub(doi, out).download(choose_scihub_url_index=3)
        
    except:
        print("Oops!", sys.exc_info()[0], "occurred.","in",doi)
        print("Next entry.")
        print()
    else:
        sci = SciHub(doi, out).download(choose_scihub_url_index=3)
    
    
    
    
    
    
    
    
    
    

df.loc[:100,0]
data = np.loadtxt('lista.csv',delimiter=';',skiprows=1)
df = pd.read_csv('lista.csv', delimiter=';')
len(DOIs)
range(DOIS)
DOIS[0]


