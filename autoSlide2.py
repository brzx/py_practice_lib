# -*- coding: UTF-8 -*-
import win32com.client
import os
import re

def PowerPoint():

  fcount=0
  picWidth=340
  picHeigh=255
  picTop=150
  ppt = os.path.join(os.getcwd(), "template.pptx")
  App = win32com.client.Dispatch("PowerPoint.Application")
  App.Visible = True
  Presentation = App.Presentations.Open(ppt)

  fL_list = os.listdir(os.path.join(os.getcwd())+"/picsL")
  fR_list = os.listdir(os.path.join(os.getcwd())+"/picsR")

  fLName_list = []
  fRName_list = []

  for fname in fL_list:
    fLName_list.append(int(re.findall(r"IMG_(.+?).png",fname)[0]))
  for fname in fR_list:
    fRName_list.append(int(re.findall(r"IMG_(.+?).png",fname)[0]))

  fLName_list.sort()
  fRName_list.sort()
  
  if (len(fLName_list) >= len(fRName_list)):
    fcount=len(fLName_list)
  else:
    fcount=len(fRName_list)

  for i in range(int(fcount)):
    mySlide = Presentation.Slides.Add(i+1, 11)
    if i< len(fLName_list):
      img = os.path.join(os.getcwd(), "picsL/IMG_"+str(fLName_list[i])+".png")
      mySlide.Shapes.AddPicture(img,LinkToFile=False,SaveWithDocument=True,Left=12,Top=picTop,Width=picWidth,Height=picHeigh)
    if i< len(fRName_list):
      img2 = os.path.join(os.getcwd(), "picsR/IMG_"+str(fRName_list[i])+".png")
      mySlide.Shapes.AddPicture(img2,LinkToFile=False,SaveWithDocument=True,Left=picWidth+25,Top=picTop,Width=picWidth,Height=picHeigh)

PowerPoint()