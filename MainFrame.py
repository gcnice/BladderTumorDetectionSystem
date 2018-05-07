# -*- coding: utf-8 -*-
"""
Created on Sun Apr 29 11:41:40 2018

@author: cao
"""

import wx
  
from PIL import Image 
from Template import Template
from Contour import Contour

'''
该类为主窗口类
'''
class MainFrame(wx.Frame):

    '''
    该类用于面板初始化，绑定按钮与动作
    '''
    def __init__(self,parent,id):  
        wx.Frame.__init__(self,parent,id,'膀胱肿瘤系统',pos=(100,100),size=(600,600))  
        panel=wx.Panel(self)
        
        choose_image=wx.Button(panel,label='选择图片',pos=(0,0),size=(100,60))  
        self.Bind(wx.EVT_BUTTON, self.choose_image_button,  choose_image)
        
        automatic_cut=wx.Button(panel,label='自动裁剪',pos=(0,60),size=(100,60))  
        self.Bind(wx.EVT_BUTTON, self.automatic_cut_button, automatic_cut)
        
        contour_extract=wx.Button(panel,label='轮廓提取',pos=(0,120),size=(100,60))  
        self.Bind(wx.EVT_BUTTON, self.contour_extract_button, contour_extract)
        
        detect_tumor=wx.Button(panel,label='检测肿瘤',pos=(0,180),size=(100,60))  
        self.Bind(wx.EVT_BUTTON, self.detect_tumor_button, detect_tumor)
        
    '''
    该类为选择图片按钮绑定的动作
    '''        
    def choose_image_button(self, event):
        dlg = wx.FileDialog(self,u"选择图片",style=wx.DD_DEFAULT_STYLE ) 
        if dlg.ShowModal() == wx.ID_OK:
            open_image = Image.open(dlg.GetPath())            
            open_image.save('picture\\original_picture.png')
            image = wx.Image(dlg.GetPath())
            image_bitmap = image.ConvertToBitmap() 
            self.choose_image_bitmap = wx.StaticBitmap(self, -1, image_bitmap,pos = (100,0),size = (image_bitmap.GetWidth(), image_bitmap.GetHeight()))
            dlg.Destroy()
            
    '''
    该类为自动裁剪按钮绑定的动作
    '''          
    def automatic_cut_button(self, event):
        Template.template_match()
        
        '''
        读入模版匹配后的图，消除之前的图，展示模版匹配的图
        '''         
        image =  wx.Image('picture\\match.png')
        image_bitmap = image.ConvertToBitmap()
        
        self.choose_image_bitmap.Destroy()
        self.automatic_cut_bitmap = wx.StaticBitmap(self, -1, image_bitmap,pos = (100,0),size = (image_bitmap.GetWidth(), image_bitmap.GetHeight()))
      
 
    '''
    该类为轮廓提取按钮绑定的动作
    '''  
    def contour_extract_button(self, event):
        Contour.contour_extract()
        
        image =  wx.Image('picture\\contour_image.png')
        image_rescale = image.Rescale(200,200)
        image_rescale_bitmap = image_rescale.ConvertToBitmap()
        
        self.automatic_cut_bitmap.Destroy()
        self.contourExtractBitmap = wx.StaticBitmap(self, -1, image_rescale_bitmap,pos = (100,0),size = (image_rescale_bitmap.GetWidth(), image_rescale_bitmap.GetHeight()))
        
    '''
    该类为检测肿瘤按钮绑定的动作
    '''       
    def detect_tumor_button(self, event):
        pass
        
'''
主函数，创建窗口并进行侦听动作
'''  
def main():
    app=wx.App() 
    main_frame=MainFrame(parent=None,id=-1)  
    main_frame.Show(True)
    app.MainLoop()

'''
函数入口
'''    
if __name__ == '__main__':
    main()