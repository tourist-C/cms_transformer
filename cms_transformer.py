#!/usr/bin/env python
# coding: utf-8

# In[3]:


import os
import argparse
import configparser
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageCms

def load_img(fp):
    img = Image.open(fp)
    return img

def convert_img(fp, profile_src, profile_dst, plot=False):
    
    # config
    # fp = r"color-profile-correction/color-profile-correction/skin-crop-non-color-corrected.tif"
    # profile_src = r"color-profile-correction/color-profile-correction/source color profile/leica_scanner.icm"
    # profile_dst = r"color-profile-correction/color-profile-correction/destination color profile/sRGB_v4_ICC_preference.icc"
    mode = "RGB"

    # ingest
    img_raw = load_img(fp)

    # build transformer
    transformer = ImageCms.buildTransform(profile_src,profile_dst,mode,mode)
    
    # transform
    img_out = transformer.apply(img_raw)
    
    # plotting before and after
    if plot:
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
        plt.show()
    
def main():

    # load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    profile_src = config['color_profiles']['src']
    profile_dst = config['color_profiles']['dst']

    # arg parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-tif', '--filepath_tif',
                         type=str, 
                         metavar="", 
                         required=True,
                         help="tiff file to be converted")
    parser.add_argument('-src', '--source_colour_profile',
                         type=str, 
                         metavar="", 
                         required=False, 
                         default=profile_src,
                         help="absolute path to input color profile. Default:\n{}".format(profile_src))
    parser.add_argument('-dst', '--destination_colour_profile',
                         type=str, 
                         metavar="", 
                         required=False, 
                         default=profile_dst,
                         help="absolute path to output color profile. Default:\n{}".format(profile_dst))
    args = parser.parse_args()

    # tidy up args
    fp = args.filepath_tif
    profile_src = args.source_colour_profile
    profile_dst = args.destination_colour_profile
    args = [fp, profile_src, profile_dst]
    kwargs = {'plot':True}

    # todo: add function to take a list of tiffs
    
    # main function
    convert_img(*args, **kwargs)


if __name__ == "__main__":
    main()

