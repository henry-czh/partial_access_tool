#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

'''
    author: chaozhanghu
    email:  chaozhanghu@foxmail.com
    date:   2019.02.15
    version:1.0
    function: deal with strobe and data fields for partial access
'''
import sys

def locat(locat,value,level,top):
    locat=int(locat)
    level=int(level)
    top=int(top)
    unuse='0'*(len(value))
    if level==1:
        if locat==0:
            be=unuse*top+unuse*top+unuse*top+value
        elif locat==1:
            be=unuse*top+unuse*top+value+unuse
        elif locat==2:
            be=unuse*top+value+unuse+unuse
        elif locat==3:
            be=value+unuse+unuse+unuse
    elif level==2:
        if locat==0:
            be=unuse*top+value
        elif locat==1:
            be=value+unuse
    elif level==3:
        be=value
    return be

def genbe(size):
    addr_low=addr[-2:]

    if int(addr_low[-1])<4:
        byte_locate=0
    elif 3<int(addr_low[-1])<8:
        byte_locate=1
    elif 7<int(addr_low[-1])<12:
        byte_locate=2
    elif 11<int(addr_low[-1])<16:
        byte_locate=3
    
    size=size.split('x')[1]
    if size=='2':
        base_be='f'
        print 'BE  : 64\'h'+locat(addr_low[-2],locat(byte_locate,base_be,1,1),1,0)
        print 'DATA: 512\'h'+locat(addr_low[-2],locat(byte_locate,data,1,1),1,0)
    elif size=='3':
        base_be='ff'
        print 'BE  : 64\'h'+locat(addr_low[-2],locat(byte_locate,base_be,2,1),1,0)
        print 'DATA: 512\'h'+locat(addr_low[-2],locat(byte_locate,data,2,1),1,0)
    elif size=='4':
        base_be='ffff'
        print 'BE  : 64\'h'+locat(addr_low[-2],base_be,1,0)
        print 'DATA: 512\'h'+locat(addr_low[-2],data,1,0)
    elif size=='5':
        base_be='ffffffff'
        print 'BE  : 64\'h'+locat(addr_low[-3],base_be,2,0)
        print 'DATA: 512\'h'+locat(addr_low[-3],data,2,0)
    elif size=='6':
        print 'BE  : 64\'h'+'ffffffff_ffffffff'
        print 'DATA: 512\'h'+data

if __name__=='__main__':
    #get opts
    if sys.argv[1]=='-h':
        print 'usage:'
        print './partial_access.py [0xaddr] [0xsize] [0xdata]'
    else:
        addr=sys.argv[1]
        size=sys.argv[2]
        data=sys.argv[3].split('x')[1]
        #main
        genbe(size)
