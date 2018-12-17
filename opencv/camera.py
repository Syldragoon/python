#!/usr/bin/env python

import cv2
import numpy as np

def onThresholdChange(value):
  print 'threshold changed to ',value

def onInvertChange(value):
  print 'threshold inverted'

if __name__ == "__main__":
  
  # initialize the camera
  cam = cv2.VideoCapture("rtp://127.0.0.1:8080/")

  # create the window(s)
  cv2.namedWindow("img_raw",cv2.CV_WINDOW_AUTOSIZE)
  cv2.namedWindow("img_gray",cv2.CV_WINDOW_AUTOSIZE)
  cv2.namedWindow("img_hsv",cv2.CV_WINDOW_AUTOSIZE)
  cv2.namedWindow("img_bin",cv2.CV_WINDOW_AUTOSIZE)

  # create the trackbars for img_bin window
  cv2.createTrackbar("threshold","img_bin",155,255,onThresholdChange)
  cv2.createTrackbar("invert","img_bin",0,1,onInvertChange)

  while 1:
    s,img_raw = cam.read()
    if s:
      img_gray = cv2.cvtColor(img_raw,cv2.COLOR_BGR2GRAY)
      cv2.rectangle(img_raw,(10,10),(200,200),(0,255,0))
      
      img_hsv = cv2.cvtColor(img_raw,cv2.COLOR_BGR2HSV)

      threshold = cv2.getTrackbarPos("threshold","img_bin")
      invert = cv2.getTrackbarPos("invert","img_bin")

      if invert:
        s,img_bin = cv2.threshold(img_gray,threshold,255,cv2.THRESH_BINARY_INV)
      else:
        s,img_bin = cv2.threshold(img_gray,threshold,255,cv2.THRESH_BINARY)

      cv2.imshow("img_raw",img_raw)
      cv2.imshow("img_gray",img_gray)
      cv2.imshow("img_hsv",img_hsv)
      if s:
        cv2.imshow("img_bin",img_bin)
      else:
        print 'threshold failed'
    else:
      print 'frame captured with errors'
    key = cv2.waitKey(1)
    if key != -1:
      break

  # destroy the window(s)
  cv2.destroyAllWindows()
