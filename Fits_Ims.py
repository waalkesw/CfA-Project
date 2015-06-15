# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:54:53 2015

@author: willwaalkes
"""

import pylab as pl
import numpy as np
from pylab import *
import pyfits
import matplotlib.pyplot as plt

C3H2='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/C3H2-reproj.fits'
CCH_1='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/CCH-1-reproj.fits' 
CCH_2='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/CCH-2-reproj.fits'
CH3OH_A_96741='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/CH3OH-A-96741-reproj.fits'
CH3OH_A_145103='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/CH3OH-A-145103-reproj.fits' 
CH3OH_E_96739='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/CH3OH-E-96739-reproj.fits'
CH3OH_E_96745='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/CH3OH-E-96745-reproj.fits'
CH3OH_E_145093='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/CH3OH-E-145093-reproj.fits'
CH3OH_E_145097='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/CH3OH-E-145097-reproj.fits'
DCOp_32='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/DCOp-32-reproj.fits'
dcop='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/dcop-reproj.fits' 
H2CO_140839='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/H2CO-140839-reproj.fits'
H2CO_145603='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/H2CO-145603-reproj.fits'
H2CO_211211='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/H2CO-211211-reproj.fits'
H13CN='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/H13CN-reproj.fits'
H13COp='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/H13COp-reproj.fits' 
HC3N='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/HC3N-reproj.fits'
HC15N='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/HC15N-reproj.fits'
HC17Op='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/HC17Op-reproj.fits' 
HCN='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/HCN-reproj.fits'
HCOp='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/HCOp-reproj.fits'
HN13C='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/HN13C-reproj.fits' 
HNC='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/HNC-reproj.fits'
N2Hp='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/n2hp-reproj.fits'
NH2D='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/NH2D-reproj.fits'
SO='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/SO-reproj.fits' 
Tdust='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/tau_1_HGBS_Tdust_r500.fits'
coldens='/Users/willwaalkes/Desktop/CfA/dense-cores-taurus1/tau_1_HGBS_coldens_r500.fits'

molecules=[C3H2,CCH_1,CCH_2,CH3OH_A_96741,CH3OH_A_145103,CH3OH_E_96739,
           CH3OH_E_96745,CH3OH_E_145093,CH3OH_E_145097,H2CO_140839,H2CO_145603,
           H2CO_211211,N2Hp]
mol_label=['$C_3H_2$','$C_2H-1$','$C_2H-2$','$CH_3OH-A$ 96741 MHz','$CH_3OH-A$ 145103 MHz','$CH_3OH-E$ 96739 MHz',
           '$CH_3OH-E$ 96745 MHz','$CH_3OH-E$ 145093 MHz','$CH_3OH-E$ 145097 MHz','$H_2CO$ 140839 MHz','$H_2CO$ 145603 MHz',
           '$H_2CO$ 211211 MHz','$N_2H^+$']
           
data_cube=[]
data=[]

vmin=.01
vmax=.6

#setting a condition for the mask:
#condition=np.where()
for i in range(len(molecules)):
    data_cube.append(pyfits.getdata(molecules[i]))
    data.append(np.squeeze(data_cube[i]))
    
for i in range(len(data)):
            plt.imshow(data[i],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
            plt.xlabel('Arcseconds')
            plt.ylabel('Arcseconds')
            plt.title(mol_label[i])
            plt.colorbar(label='Intensity')
            plt.show()
            
f, axarr = plt.subplots(3, 4)
axarr[0, 0].imshow(data[0],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[0, 0].set_title(mol_label[0],size='7')
axarr[0, 1].imshow(data[1],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[0, 1].set_title(mol_label[1],size='7')
axarr[0, 2].imshow(data[2],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[0, 2].set_title(mol_label[2],size='7')
axarr[0, 3].imshow(data[3],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[0, 3].set_title(mol_label[3],size='7')
axarr[1, 0].imshow(data[4],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[1, 0].set_title(mol_label[4],size='7')
axarr[1, 1].imshow(data[5],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[1, 1].set_title(mol_label[5],size='7')
axarr[1, 2].imshow(data[6],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[1, 2].set_title(mol_label[6],size='7')
axarr[1, 3].imshow(data[7],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[1, 3].set_title(mol_label[7],size='7')
axarr[2, 0].imshow(data[8],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[2, 0].set_title(mol_label[8],size='7')
axarr[2, 1].imshow(data[9],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[2, 1].set_title(mol_label[9],size='7')
axarr[2, 2].imshow(data[10],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
axarr[2, 2].set_title(mol_label[10],size='7')

f.colorbar(label='Intensity')

plt.setp([a.get_xticklabels() for a in axarr[2, :]], visible=True,size='5')
plt.setp([a.get_yticklabels() for a in axarr[:, 0]], visible=True,size='5')
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[1, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 3]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 2]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
