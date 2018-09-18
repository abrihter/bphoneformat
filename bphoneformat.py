#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
title           : phone number format
author          : bojan
date            : 20180918
version         : 1.00
usage           : as master class
notes           :
python_version  : 3.4.4
description     : Class to format phone numbers based on input county and phone
#==============================================================================
#==============================================================================
v1.00 - 18.09.2018
    - first working version
"""

import json

class bPhoneFormat:
    '''phone number format class'''
    
    #cfg file
    CFG_FILE = 'config.json'
    #cfg mockup
    CFG = {
        'codes-file': ''
    }
    #list of country codes
    COUNTRY_CODES = {}
    
    def __init__(self):
        '''init'''
        if self.read_cfg() == False:
            return
        if self.read_country_codes() == False:
            return
        
    def read_cfg(self):
        '''read cfg file
        :return bool: Returns True if all is OK | False on error
        '''
        try:
            #read config file
            with open(self.CFG_FILE, 'r') as f:
                cfg = json.loads(f.read())
            # if no config then error
            for c in self.CFG:
                self.CFG[c] = cfg[c]
        except Exception as e:
            print('Error reading config.json file!')
            return False
        return True
        
    def read_country_codes(self):
        '''read country codes file
        :return bool: Returns True if all is OK | False on error
        '''
        try:
            #read codes file
            with open(self.CFG['codes-file'], 'r') as f:
                self.COUNTRY_CODES = json.loads(f.read())
        except Exception as e:
            print('Error reading country codes file!')
            return False
        return True
    
    def format_phone(self, country, phone):
        '''format phone number
        :param str country: Country name
        :param str phone: Phone number:
        :return str: Returns formated string with full phone number or False 
                     on error
        '''
        try:
            #if leading zero, remove it
            if phone[0] == '0':
                phone = phone[1:]
            return '+{}{}'.format(
                self.COUNTRY_CODES[country.upper()]['code'], 
                phone
            )
        except:
            return False
            
    def get_country_keys(self, sorted = True):
        '''return all country keys
        :param bool sorted: Define if list need to be sorted
        :return list: Returns list of country keys, to use as keys
        '''
        cc = [x.strip() for x in self.COUNTRY_CODES]
        if sorted:
            cc.sort()
        return cc
        
    def get_country_names(self, sorted = True):
        '''return all country names
        :param bool sorted: Define if list need to be sorted
        :retrun list: Returns list of country names
        '''
        cc = [self.COUNTRY_CODES[x.strip()]['name'].strip() 
                for x in self.COUNTRY_CODES]
        if sorted:
            cc.sort()
        return cc