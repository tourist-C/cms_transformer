#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageCms

def load_img(fp):
    img = Image.open(fp)
    return img

def main():
    
    # config
    fp = r"color-profile-correction/color-profile-correction/skin-crop-non-color-corrected.tif"
    profile_src = r"color-profile-correction/color-profile-correction/source color profile/leica_scanner.icm"
    profile_dst = r"color-profile-correction/color-profile-correction/destination color profile/sRGB_v4_ICC_preference.icc"
    mode = "RGB"
    
    # ingest
    img_raw = load_img(fp)

    # build transformer
    transformer = ImageCms.buildTransform(profile_src,profile_dst,mode,mode)
    
    # transform
    img_out = transformer.apply(img_raw)
    
    # plotting before and after
    imgs = [img_raw, img_out]
    imgs = [np.array(i) for i in imgs]
    
    fig, axes = plt.subplots(1,2)
    axes[0].imshow(imgs[0])
    axes[0].set_title("BEFORE")
#     axes[0].axis('off')
    axes[1].imshow(imgs[1])
    axes[1].set_title("AFTER")
#     axes[1].axis('off')

    fig.set_figwidth(40)
    fig.set_figheight(30)
    
if __name__ == "__main__":
    main()

