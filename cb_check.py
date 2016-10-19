# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 12:14:54 2016

@author: X154045
"""

lst1=[(x%2)+1 for x in range(1,16)]
#lst2=list([5,2,9,5,4,6,4,8,5,2,0,1,3,6,7])
lst2=list([5,2,9,5,4,6,4,8,5,2,0,1,3,6,7])

lst3=[a*b for a,b in zip(lst1,lst2)]

def az(a,b):
    if a*b>=10:
        return (a*b)-9
    else:
        return a*b
        
lst4=[az(a,b) for a,b in zip(lst1,lst2)]

if sum(lst4) % 10 !=0:
    print ('not valid')
else:
    print('valid')
