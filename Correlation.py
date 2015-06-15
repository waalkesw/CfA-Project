import pylab as pl
import numpy as np
from pylab import *
import pyfits
from matplotlib import *
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

##getting the data from the .fits files and finding out the dimensions    

Tdust_data_cube=pyfits.getdata(Tdust)
Tdust_data_cube.shape

coldens_data_cube=pyfits.getdata(coldens)
coldens_data_cube.shape

##removing size 1 dimensions from the array
colors=np.squeeze(Tdust_data_cube)
colors2=np.squeeze(coldens_data_cube)

##array of 'x' values
##array of 'y' values
colors.shape[0]
colors.shape[1]
colors2.shape[0]
colors2.shape[1]
#multipyling the values together, turning a 2-D array into a 1-D array
colors_reshape=colors.reshape(colors.shape[0]*colors.shape[1])
colors2_reshape=colors2.reshape(colors2.shape[0]*colors2.shape[1])
molecules=[C3H2,CCH_1,CCH_2,CH3OH_A_96741,CH3OH_A_145103,CH3OH_E_96739,
           CH3OH_E_96745,CH3OH_E_145093,CH3OH_E_145097,H2CO_140839,H2CO_145603,
           H2CO_211211,N2Hp]
mol_label=['$C_3H_2$','$C_2H-1$','$C_2H-2$','$CH_3OH-A$ 96741 MHz','$CH_3OH-A$ 145103 MHz','$CH_3OH-E$ 96739 MHz',
           '$CH_3OH-E$ 96745 MHz','$CH_3OH-E$ 145093 MHz','$CH_3OH-E$ 145097 MHz','$H_2CO$ 140839 MHz','$H_2CO$ 145603 MHz',
           '$H_2CO$ 211211 MHz','$N_2H^+$']
           
data_cube=[]
data=[]
data_reshape=[]
data_mask=[]

#setting a condition for the mask:
#condition=np.where()
for i in range(len(molecules)):
    data_cube.append(pyfits.getdata(molecules[i]))
    data.append(np.squeeze(data_cube[i]))
    data_mask.append(data[i])
    #data_mask[condition]=0.0
    data_reshape.append(data[i].reshape(data[i].shape[0]*data[i].shape[1]))
    
for i in range(len(data_reshape)):
    for j in range(len(data_reshape)):
        if (i != j): 
            molecule_1=data_reshape[i]
            molecule_2=data_reshape[j]
            plt.scatter(molecule_1,molecule_2,s=1,marker='o',c=colors2_reshape,edgecolor='none')
            plt.xlabel(mol_label[i])
            plt.ylabel(mol_label[j])
            plt.title('Spatial Correlation')
            plt.colorbar(label='Column Density ($cm^{-2}$)')
            plt.show()
