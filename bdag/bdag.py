# -*- coding: utf-8 -*-
import datetime as dt
import os

END     = '\033[0m'
REDbg   = '\033[41m'
REDfg   = '\033[31m'
GREENbg = '\033[42m'
GREENfg = '\033[32m'
YELLOfg = '\033[33m'
BLACKfg = '\033[30m'
BLINK   = '\033[5m'

class bdager:

    def __init__(self):
        path = os.getcwd()
        with open(path+'/bdag/datoer.csv','r') as datoer:
            alle = []
            idag        = dt.date.today()
            for line in datoer:
                templine    = line.strip().split(',')
                navn        = templine[0]
                dag         = int(templine[1]) 
                maaned      = int(templine[2])
                aar         = int(templine[3])
                datoen      = dt.date(aar,maaned,dag)
                d_igjen     = (datoen.replace(year=idag.year) - idag).days
                alle.append({'navn':navn,'bdag':datoen,'d_igjen':d_igjen})
        
            self.alle = sorted(alle, key=lambda k: k['d_igjen'])
        

    def igjen(self):

        siste = ''
        ut_streng = '{0:10}  {1:3} dager {2}\n'
        for pers in self.alle:
            digjen = pers['d_igjen']
            if digjen<0:
                igjen_siden = REDfg+'siden'
            elif digjen >0 and digjen <5:
                igjen_siden = BLINK+YELLOfg+'igjen'
            else:
                igjen_siden = GREENfg+'igjen'
            igjen_siden += END
            siste += ut_streng.format(pers['navn'],abs(pers['d_igjen']),igjen_siden)
        return siste

if __name__=='__main__':

    dager = bdager()
    print(dager.igjen())
