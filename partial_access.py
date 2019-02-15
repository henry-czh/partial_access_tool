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
    level=int(level)
    top=int(top)
    unuse='0'*(len(value))
    if level==1:
        if locat=='00':
            be=unuse*top+unuse*top+unuse*top+value
        elif locat=='01':
            be=unuse*top+unuse*top+value+unuse
        elif locat=='10':
            be=unuse*top+value+unuse+unuse
        elif locat=='11':
            be=value+unuse+unuse+unuse
    elif level==2:
        if locat=='0':
            be=unuse*top+value
        elif locat=='1':
            be=value+unuse
    elif level==3:
        be=value
    return be

def genbe(size):
    
    if size=='2':
        base_be='f'
        print 'BE  : 64\'h'+locat(addr[-6:-4],locat(addr[-4:-2],base_be,1,1),1,0)
        print 'DATA: 512\'h'+locat(addr[-6:-4],locat(addr[-4:-2],data,1,1),1,0)
    elif size=='3':
        base_be='ff'
        print 'BE  : 64\'h'+locat(addr[-6:-4],locat(addr[-4],base_be,2,1),1,0)
        print 'DATA: 512\'h'+locat(addr[-6:-4],locat(addr[-4],data,2,1),1,0)
    elif size=='4':
        base_be='ffff'
        print 'BE  : 64\'h'+locat(addr[-6:-4],base_be,1,0)
        print 'DATA: 512\'h'+locat(addr[-6:-4],data,1,0)
    elif size=='5':
        base_be='ffffffff'
        print 'BE  : 64\'h'+locat(addr[-6],base_be,2,0)
        print 'DATA: 512\'h'+locat(addr[-6],data,2,0)
    elif size=='6':
        print 'BE  : 64\'h'+'ffffffff_ffffffff'
        print 'DATA: 512\'h'+data

def getopts():
    addr=''
    for byte in addr_init:
        if byte=='0':
            addr=addr+'0000'
        elif byte=='1':
            addr=addr+'0001'
        elif byte=='2':
            addr=addr+'0010'
        elif byte=='3':
            addr=addr+'0011'
        elif byte=='4':
            addr=addr+'0100'
        elif byte=='5':
            addr=addr+'0101'
        elif byte=='6':
            addr=addr+'0110'
        elif byte=='7':
            addr=addr+'0111'
        elif byte=='8':
            addr=addr+'1000'
        elif byte=='9':
            addr=addr+'1001'
        elif byte=='a':
            addr=addr+'1010'
        elif byte=='b':
            addr=addr+'1011'
        elif byte=='c':
            addr=addr+'1100'
        elif byte=='d':
            addr=addr+'1101'
        elif byte=='e':
            addr=addr+'1110'
        elif byte=='f':
            addr=addr+'1111'
    return addr

if __name__=='__main__':
    #get opts
    if sys.argv[1]=='-h':
        print 'usage:'
        print './partial_access.py [0xaddr] [0xsize] [0xdata]'
    else:
        addr_init=sys.argv[1].split('x')[1]
        size=sys.argv[2].split('x')[1]
        data=sys.argv[3].split('x')[1]
        addr=getopts()
        #main
        genbe(size)
