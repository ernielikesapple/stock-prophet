#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 20:15:32 2020

@author: ernie
"""

# data source , sock name and current price:
    
    
    
                # company names, prices
dataSources = { 'Google': 1598,88,    
                'Apple': 116,60,
                'Tesla': 424,68,
                'AMD': 78,88,
                'NIKE': 127,99,
                'Starbucks' 90,05 ,
                'boeing', 155,24,
                'disney', 123,31,
                'exxon',32,82,     #gas supplier
                'astraZeneca', 52,48,    #usa vaccine suppliers , UK
                'sanofi',47,40,    #usa vaccine suppliers       Fr
                'moderna', 70,67,  #canada vaccine suppliers
                'pfizer',47,40,    #canada vaccine suppliers
                'baba', 317,14,    # china 
                'baidu',134,89,    # china 
                
            
                }



currentPriceBoeing = 155,24
currentPriceExxon = 32,82

normalPriceBoeing = 300
normalPriceExxon  = 70


x1 = 1  #share should buy for Boeing

x2 = 1  #share should buy for Boeing


sumMoney = x1*currentPriceBoeing + x2 * currentPriceExxon 

Profit = (normalPriceBoeing - currentPriceBoeing) * x1 + (normalPriceExxon - currentPriceExxon) * x2



