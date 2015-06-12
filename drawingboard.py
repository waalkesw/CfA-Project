# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:32:02 2015

@author: willwaalkes
"""

So, to make the mask you can do something like this:
im_mask = im    # first copy the array
im_mask[condition] = 0.0

The 'condition' here can be different things. For example, you could mask the noise in one of the images (like N2H+), or you could mask the regions with very low column density, etc. You do that with the "where" command from numpy:

condition = np.where(NH2<1e10) 

that will create an array with the indexes that fulfill the condition inside. 