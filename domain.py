# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:39:35 2018

@author: h.muhammed
"""

from urllib.parse import urlparse

# get the domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split('.')
        return results[-2] + '.' + results[-1]
    except:
        return ''

# get sub domain name (name.domain.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
    
