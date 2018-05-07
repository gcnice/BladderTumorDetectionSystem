# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 14:49:45 2018

@author: cao
"""

import numpy as np

from keras.preprocessing.image import load_img,  array_to_img, img_to_array
from Unet import Unet
from PIL import Image 

'''
该类为轮廓类
'''
class Contour():
   
    '''
    该方法为轮廓提取
    '''
    def contour_extract():

        '''
        将模版匹配后的图进行处理
        '''    
        image = Image.open('picture\\match.png')
        image_resize = image.resize((512,512))
        image_resize.save('picture\\match.png')
        
        '''
        加载图片后将其转化为向量
        '''        
        match_image = load_img('picture\\match.png',grayscale = True)
        match_image_datas = np.ndarray((1,512,512,1), dtype=np.uint8)
        match_image_datas_array = img_to_array(match_image)
        match_image_datas[0] = match_image_datas_array
        images_test = match_image_datas.astype('float32')
        
        '''
        将向量归一化
        '''          
        images_test /= 255
        
        '''
        调用网络结构，并加载模型权重
        '''         
        unet = Unet()
        model = unet.get_unet()
        model.load_weights('weight\\unet.hdf5')
        
        '''
        进行预测
        '''          
        images_mask_test = model.predict(images_test, verbose=1)
        
        '''
        将预测后得到的向量保存为图片
        '''        
        for i in range(images_mask_test.shape[0]):
            img = images_mask_test[i]
            img = array_to_img(img)
            img.save("picture\\contour_image.png")            
        
        