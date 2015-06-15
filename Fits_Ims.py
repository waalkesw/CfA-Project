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
           CH3OH_E_96745,CH3OH_E_145093,CH3OH_E_145097,DCOp_32,dcop,H2CO_140839,H2CO_145603,
           H2CO_211211,H13CN,H13COp,HC3N,HC15N,HC17Op,HCN,HCOp,HN13C,HNC,N2Hp,NH2D,SO,Tdust,coldens]
mol_label=['$C_3H_2$','$C_2H-1$','$C_2H-2$','$CH_3OH-A$ 97GHz','$CH_3OH-A$ 145GHz',
           '$CH_3OH-E$ 96.73GHz','$CH_3OH-E$ 96.74GHz','$CH_3OH-E$ 145GHz','$CH_3OH-E$ 145GHz',
           '$DCO^+-32$','$DCO^+$','$H_2CO$ 141GHz','$H_2CO$ 146GHz','$H_2CO$ 211GHz',
           '$H^{13}CN$','$H^{13}CO^+$','$HC_3N$','$HC^{15}N$','$HC^{17}O^+$','$HCN$','$HCO^+$',
           '$HN^{13}C$','$HNC$','$N_2H^+$','$NH_2D$','$SO$','Dust Temp','$H_2$ CD']
           
data_cube=[]
data=[]

vmin=0
vmax=0.8

#setting a condition for the mask:
#condition=np.where()
for i in range(len(molecules)):
    data_cube.append(pyfits.getdata(molecules[i]))
    data.append(np.squeeze(data_cube[i]))
    
#==============================================================================
# for i in range(len(data)):
#             plt.imshow(data[i],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=vmin,vmax=vmax)
#             plt.xlabel('Arcseconds')
#             plt.ylabel('Arcseconds')
#             plt.title(mol_label[i])
#             plt.colorbar(label='Intensity')
#             plt.show()
#==============================================================================
            
f, axarr = plt.subplots(4, 7)
axarr[0, 0].imshow(data[0],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=.01,vmax=0.7)
axarr[0, 0].set_title(mol_label[0],size='6')
#axarr[0, 0].plt.colorbar()
axarr[0, 1].imshow(data[1],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.3)
axarr[0, 1].set_title(mol_label[1],size='6')
axarr[0, 2].imshow(data[2],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.2)
axarr[0, 2].set_title(mol_label[2],size='6')
axarr[0, 3].imshow(data[3],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.8)
axarr[0, 3].set_title(mol_label[3],size='4.5')
axarr[0, 4].imshow(data[4],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.6)
axarr[0, 4].set_title(mol_label[4],size='4.5')
axarr[0, 5].imshow(data[5],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.65)
axarr[0, 5].set_title(mol_label[5],size='4.5')
axarr[0, 6].imshow(data[6],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.14)
axarr[0, 6].set_title(mol_label[6],size='4.5')
axarr[1, 0].imshow(data[7],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.2)
axarr[1, 0].set_title(mol_label[7],size='5')
axarr[1, 1].imshow(data[8],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.5)
axarr[1, 1].set_title(mol_label[8],size='5')
axarr[1, 2].imshow(data[9],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.9)
axarr[1, 2].set_title(mol_label[9],size='6')
axarr[1, 3].imshow(data[10],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=1.5)
axarr[1, 3].set_title(mol_label[10],size='6')
axarr[1, 4].imshow(data[11],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0.01,vmax=1.4)
axarr[1, 4].set_title(mol_label[11],size='6')
axarr[1, 5].imshow(data[12],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=1.1)
axarr[1, 5].set_title(mol_label[12],size='6')
axarr[1, 6].imshow(data[13],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=1.2)
axarr[1, 6].set_title(mol_label[13],size='6')
axarr[2, 0].imshow(data[14],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.23)
axarr[2, 0].set_title(mol_label[14],size='6')
axarr[2, 1].imshow(data[15],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=1.0)
axarr[2, 1].set_title(mol_label[15],size='6')
axarr[2, 2].imshow(data[16],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.25)
axarr[2, 2].set_title(mol_label[16],size='6')
axarr[2, 3].imshow(data[17],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.17)
axarr[2, 3].set_title(mol_label[17],size='6')
axarr[2, 4].imshow(data[18],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.2)
axarr[2, 4].set_title(mol_label[18],size='6')
axarr[2, 5].imshow(data[19],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.5)
axarr[2, 5].set_title(mol_label[19],size='6')
axarr[2, 6].imshow(data[20],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0.14,vmax=1.5)
axarr[2, 6].set_title(mol_label[20],size='6')
axarr[3, 0].imshow(data[21],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.5)
axarr[3, 0].set_title(mol_label[21],size='6')
axarr[3, 1].imshow(data[22],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0.05,vmax=1.5)
axarr[3, 1].set_title(mol_label[22],size='6')
axarr[3, 2].imshow(data[23],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.5)
axarr[3, 2].set_title(mol_label[23],size='6')
axarr[3, 3].imshow(data[24],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.6)
axarr[3, 3].set_title(mol_label[24],size='6')
axarr[3, 4].imshow(data[25],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0,vmax=0.6)
axarr[3, 4].set_title(mol_label[25],size='6')
axarr[3, 5].imshow(data[26],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=10,vmax=14)
axarr[3, 5].set_title(mol_label[26],size='6')
axarr[3, 6].imshow(data[27],extent=[-100,100,-100,100],origin='lower',cmap='jet',vmin=0.5e22,vmax=4e22)
axarr[3, 6].set_title(mol_label[27],size='6')

plt.setp([a.get_xticklabels() for a in axarr[3, :]], visible=True,size='4')
plt.setp([a.get_yticklabels() for a in axarr[:, 0]], visible=True,size='4')

plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[1, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[2, :]], visible=False)

plt.setp([a.get_yticklabels() for a in axarr[:, 6]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 5]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 4]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 3]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 2]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)

plt.savefig('Montage.png', dpi=900)