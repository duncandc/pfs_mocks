#!/usr/bin/env python

from __future__ import print_function, division
import numpy as np 
import os, sys

def main():
    
    #box parameters
    Lbox = 400.0
    Nsub = 4 #number of subdivisions Ntot=Nsub**3
    
    
    ##########################################
    #####create qeuries to get particles######
    ##########################################
    
    #create base of query
    snapnum = '48'
    q_base = '"SELECT * FROM SMDPL.Rockstar WHERE snapnum='+snapnum
    
    #save queries to a file
    f = open('halocat_queries_list.txt','w')

    #print out header in each file
    f.write("#index      query     filename"+'\n')
    
    N=1 #counter
    for i in range(0,Nsub):
        for j in range(0,Nsub):
            l=1 # counter to split up queries file 
            for k in range(0,Nsub):
                x_min = Lbox/Nsub * i
                x_max = Lbox/Nsub * (i+1)
                
                y_min = Lbox/Nsub * j
                y_max = Lbox/Nsub * (j+1)
                
                z_min = Lbox/Nsub * k
                z_max = Lbox/Nsub * (k+1)
                
                if i == 0: i_op='>= '
                else: i_op='> '
                if j == 0: j_op='>= '
                else: j_op='> '
                if k == 0: k_op='>= '
                else: k_op='> '


                q_tail = ' AND x '+i_op+'%.6s' % ('%.4f' % x_min) + ' AND x <= ' + '%.6s' % ('%.4f' % x_max) +\
                         ' AND y '+j_op+'%.6s' %('%.4f' % y_min) + ' AND y <= ' +'%.6s' %('%.4f' % y_max) +\
                         ' AND z '+k_op+'%.6s' %('%.4f' % z_min) + ' AND z <= ' +'%.6s' %('%.4f' % z_max)+'"'
                q = q_base + q_tail
                
                fname = 'subvol_'+str(i)+'_'+str(j)+'_'+str(k)+'_snapnum_'+snapnum+'.csv'
                
                s = '%3s'%N + '     '+ q + '     ' + fname +'\n'

                f.write(s)
                
                N=N+1

    f.close()
    

    ##########################################################
    #####create qeuries to get total number of particles######
    ##########################################################
    
    #create base of query
    q_base = '"SELECT COUNT(rockstarId) FROM SMDPL.Rockstar WHERE snapnum='+snapnum
    
    #save queries to a file
    f = open('count_queries_list.txt','w')

    #print out header in each file
    f.write("#index     query     filename"+'\n')

    N=1 #counter
    for i in range(0,Nsub):
        for j in range(0,Nsub):
            l=1 # counter to split up queries file 
            for k in range(0,Nsub):
                x_min = Lbox/Nsub * i
                x_max = Lbox/Nsub * (i+1)
                
                y_min = Lbox/Nsub * j
                y_max = Lbox/Nsub * (j+1)
                
                z_min = Lbox/Nsub * k
                z_max = Lbox/Nsub * (k+1)
                
                if i == 0: i_op='>= '
                else: i_op='> '
                if j == 0: j_op='>= '
                else: j_op='> '
                if k == 0: k_op='>= '
                else: k_op='> '

                q_tail = ' AND x '+i_op+'%.6s' % ('%.4f' % x_min) + ' AND x <= ' + '%.6s' % ('%.4f' % x_max) +\
                         ' AND y '+j_op+'%.6s' %('%.4f' % y_min) + ' AND y <= ' +'%.6s' %('%.4f' % y_max) +\
                         ' AND z '+k_op+'%.6s' %('%.4f' % z_min) + ' AND z <= ' +'%.6s' %('%.4f' % z_max)+'"'
                q = q_base + q_tail
                
                fname = 'subvol_N_'+str(i)+'_'+str(j)+'_'+str(k)+'_snapnum_'+snapnum+'.csv'
                
                s = '%3s'%N + '     ' + q + '     ' + fname +'\n'

                f.write(s)

                N=N+1
    
    f.close()

if __name__ == "__main__":
    main()