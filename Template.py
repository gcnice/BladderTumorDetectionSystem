# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 13:09:27 2018

@author: cao
"""

import cv2  
import numpy as np
  
from matplotlib import pyplot as plt  

'''
该类为模版类
'''
class Template():

    '''
    该方法为模版匹配方法，采用OpenCV的模版匹配方法
    '''
    def template_match():
    
        '''
        读入原图，读入模版图
        '''    
        image = cv2.imread("picture\\original_picture.png",0)
        image_copy = image.copy()  
     
        template_image = cv2.imread("picture\\template_picture.png",0)    
        template_image_width,template_image_height = template_image.shape[::-1]
        
        '''
        模版匹配的六种方式
        '''           
        methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',  
                   'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
                   
        '''
        遍历模版匹配的六种方式，取最好的效果
        '''            
        for meth in methods:  
            img = image_copy.copy()            
            method = eval(meth)          
            templateImageResult = cv2.matchTemplate(img,template_image,method)  
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(templateImageResult)  
          
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:  
                top_left = min_loc  
            else:  
                top_left = max_loc  
            bottom_right = (top_left[0] + template_image_width, top_left[1] + template_image_height)
            
        '''
        读取匹配后边界，然后存储在图中
        ''' 
        crop_image = img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] 
        cv2.imwrite('picture\\match.png',crop_image)