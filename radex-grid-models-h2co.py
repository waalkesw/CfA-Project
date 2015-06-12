#! /usr/bin/python
#
import math
import os
import time
import sys
import numpy as np
from math import *
import pyfits
import pylab as pl
from pylab import *


#
maxiter = 100
debug   = False
radexpath = '~/local/Radex/data/'
extension = '.dat'

pc = 3.08568025e18 # cm
pi = 3.14159265
k =  1.3806503e-16 # erg /K

tbg = 2.73   # cmb temp
dv = 0.6


fmt = "%7.2e cm^-2"
cdmin = 1e10   # range of column densities explored: from 10^10 to 10^13 cm-2
cdmax = 1e13
ncd = 20       # number of column densities 

# Collision partners
#
# ph2co -> ph2, oh2
# oh2co -> ph2, oh2

moles = ['oh2co','ph2co']
frequencies = [[140.8395],[145.6029]]

############################################################

# this routine will write the input file for RADEX
def write_input(file,source,tkin,nh2,mole,cdmol,freqs):
    ne = 0.1*nh2
    op = 3
    nph2 = nh2/(op+1)
    noh2 = nph2*op
    file.write(mole+'-h2.dat\n')
    file.write("out/"+source+'-radex-'+mole+'.out\n')
    file.write(str(freqs[0]-0.001)+' '+str(freqs[-1]+0.001)+'\n')
    file.write(str(tkin)+'\n')
    file.write('2\n')
    file.write('oh2\n')
    file.write(str(noh2)+'\n')
    file.write('ph2\n')
    file.write(str(nph2)+'\n')
    file.write(str(tbg)+'\n')
    file.write(str(cdmol)+'\n')
    file.write(str(dv)+'\n')
 
# this read the output created by RADEX and extracts the information you want: tkin,density,column density and flux 
def read_radex(results,freq):
    line  = results.readline()
    words = line.split()
    while (words[1] != "T(kin)"):
        line  = results.readline()
        words = line.split()
    tkin = words[-1] 
    line  = results.readline()
    words = line.split()
    dens = words[-1]
    line  = results.readline()
    words = line.split()
    while (words[1] != "Column"):
        line  = results.readline()
        words = line.split()
    cdmol = words[-1] 
    line  = results.readline()
    words = line.split()
    while (words[-1] != "FLUX"):
        line  = results.readline()
        words = line.split()
    line  = results.readline()
    line  = results.readline()
    words = line.split()
    ftmp  = float(words[4])
    while (freq!=ftmp):
        line  = results.readline()
        words = line.split()
        ftmp  = float(words[4])
    TR = float(words[-5])
    return tkin,dens,cdmol,TR
 
# Begin of main program
def main(source):
    # Read Tdust and nH2 data 
    tgas,hdr = pyfits.getdata("../Td-NH-maps/"+source+"_HGBS_Tdust_r500.fits", 0, header=True)
    NH2   = pyfits.getdata("../Td-NH-maps/"+source+"_HGBS_coldens_r500.fits", 0)
    ngas = NH2/1e17  # determine the H2 density from the H2 column density map. 
    cdmol =  tgas*0

    for imole in range(len(moles)):
        mole  = moles[imole]
        print "Molecule: ",mole
        freqs = frequencies[imole]
        number_models = 0

        # Run grids of RADEX models

        # this loop creates the input file for RADEX
        file = open("inp/"+source+'-radex-'+mole+'.inp','w')
        for i in range(tgas.shape[0]):
            for j in range(tgas.shape[1]):
                for icd in range(ncd):
                    cd = cdmin*((cdmax/cdmin)**(float(icd)/ncd))
                    write_input(file,source,tgas[i,j],ngas[i,j],mole,cd,freqs)
                    number_models += 1

                    if((i==tgas.shape[0]-1) & (j==tgas.shape[1]-1) & (icd==ncd-1)): 
                        file.write('0\n')
                        file.close()
                    else:
                        file.write('1\n')
                        
        start = time.time()
         
        # run the models
        print "Runing ",number_models," models"
        os.system('radex < inp/'+source+'-radex-'+mole+'.inp > /dev/null')
      
        stop = time.time()
        duration = stop-start
        print "Run time = ",duration," seconds"

        # Read and save model results 

        for freq in freqs:

            tgas_radex = np.zeros(shape=(ncd,tgas.shape[0],tgas.shape[1]))
            ngas_radex = np.zeros(shape=(ncd,tgas.shape[0],tgas.shape[1]))
            cdmol_radex = np.zeros(shape=(ncd,tgas.shape[0],tgas.shape[1]))
            TR_radex = np.zeros(shape=(ncd,tgas.shape[0],tgas.shape[1]))

            print "Reading results for line "+mole+" "+str(freq)
            results = open("out/"+source+'-radex-'+mole+'.out','r')
            for i in range(tgas.shape[0]):
                for j in range(tgas.shape[1]):
                    for k in range(ncd):
                        tgas_radex[k,i,j],ngas_radex[k,i,j],cdmol_radex[k,i,j],TR_radex[k,i,j] = read_radex(results,freq)
                
            # update header            
            hdr.update('NAXIS', 3)
            hdr.update('NAXIS3', ncd)

            # save results: FITS cube with the different column density maps
            pyfits.writeto("fits-radex-models-lines/"+source+"-radex-"+mole+"-"+str(freq)+".fits", TR_radex, hdr, clobber=True)
        
        results.close()

############################################################

# main("aql_1")
# main("aql_2")
# main("aql_3")
# main("aql_4")
# main("aql_5")
# main("aql_6")

main("tau_1")
main("tau_2")
main("tau_3")
main("tau_4")
main("tau_6")
