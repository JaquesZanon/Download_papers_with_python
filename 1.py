# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 15:32:40 2021

@author: Jaques Zanon
"""

!pip3 install -U scidownl
from scidownl.scihub import *


DOIs = [...]# here is the list of papers DOIs 
out = 'paper'
   
for doi in DOIS:
    try:
        SciHub(doi, out).download(choose_scihub_url_index=3)
        
    except:
        print("Oops!", sys.exc_info()[0], "occurred.","in",doi)
        print("Next entry.")
        print()
    else:
        sci = SciHub(doi, out).download(choose_scihub_url_index=3)
    
