# -*- coding: utf-8 -*-
"""
Created on Tue May  3 19:49:27 2022

@author: jagpreet
"""

def solve(s):
    """ 
    s: positive integer, what the sum should add up to
    Solves the following optimization problem:
        x1 + x2 + x3 + x4 is minimized 
        subject to the constraint x1*25 + x2*10 + x3*5 + x4 = s
        and that x1, x2, x3, x4 are non-negative integers.
    Returns a list of the coefficients x1, x2, x3, x4 in that order
    """
    ans=[0,0,0,0]
    while s!=0:
        if s==1:
            ans[3]+=1
            return ans
            
        if s>=25:
           
            if s%25==0:
                ans[0]+=1
                s=s-25
            else:
                s=s-25
                ans[0]+=1
            
                
        if s>=10 and s<25:
            
            if s%10:  
                ans[1]+=1
                s=s-10
            else:
                s=s-10
                ans[1]+=1
           
                
        if s>=5 and s<10 :
            
            if s%5==0:
                ans[2]+=1
                s=s-5
            else:
                s=s-5
                ans[2]+=1
            
                
        if s>1 and s<5 and (s%1==0):
            
            
            ans[3]+=1*s
            s=0
                
    return ans
print(solve(100))
                
        
        
        
            
        
        
  
        
        
        
    

            
        
    