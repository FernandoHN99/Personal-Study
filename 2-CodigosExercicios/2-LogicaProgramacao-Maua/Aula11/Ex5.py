# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 17:40:38 2018

@author: User
"""
algo = "EFB403"
def teste (algo):
    resp = ''
    for c in algo:
        resp = c + resp
    return resp

print(teste (algo))
    