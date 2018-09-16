import numpy as np
import cv2
import statistics
from identifier import get_color
import copy


def get_contours(image_file):
    #read image and convert to HSV and grayScale
    rawImg = cv2.imread(image_file)
    rawImgHSV = cv2.cvtColor(rawImg,cv2.COLOR_BGR2HSV)
    rawImgGray = cv2.cvtColor(rawImg,cv2.COLOR_BGR2GRAY)

    #Trying Contour Detection
    blur = cv2.GaussianBlur(rawImgGray,(5,5),0)
    ret,thresh = cv2.threshold(blur,127,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    area_list = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        area_list.append(area)

    area_list.sort()
    lower_list = area_list[0:round(len(area_list)/2-1)]
    upper_list = area_list[round(len(area_list)/2+2):]
    lower_median = statistics.median(lower_list)
    upper_median = statistics.median(upper_list)
    iqr = (upper_median - lower_median)

    #print("Lower Median: " + str(lower_median))
    #print("Upper Median: " + str(upper_median))
    median = statistics.median(area_list)
    #print("Median: " + str(median))

    mean = statistics.mean(area_list)
    standard_dev = statistics.stdev(area_list)

    new_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        area_dif = abs(mean - area)
        if (area_dif < 5*standard_dev and area > 50):
            new_contours.append(cnt)


    #print(np.min(area_list))

    #This is not really needed. can remove
    roi_gbr_list = []

    #array to collect contours of different colors
    colorDict = {"WHITE":[],"BLACK":[],"BLUE":[],"GREEN":[],"RED":[],"YELLOW":[],"ORANGE":[],"PURPLE":[],"PINK":[]}
    for i in range(0,len(new_contours)):
        cnt = new_contours[i]
        x,y,w,h = cv2.boundingRect(cnt)

        #roi_list.append(rawImg[x:x+w,y:y+h])
        #Roi w,y,w,h
        x = x + int(round(.25*w))
        y = y + int(round(.25*h))
        w = int(.5*w)
        h = int(.5*h)

        roi = rawImg[y:y+h,x:x+w]
        flatRoi = roi.shape[0]*roi.shape[1]
        roi = roi.reshape([flatRoi,3])
        #roi = np.mean(roi,axis=0)
        roi = np.median(roi,axis=0)
        
        roi_gbr_list.append(roi) #HSV of all regions of interest
        #roi_gbr_list = np.append(roi_gbr_list,roi)

        #Sort contours by color BGR to RGB
        colorDict[get_color([roi[2],roi[1],roi[0]])].append(new_contours[i])

    #Writing the files
    img_file_dict = {"WHITE":[],"BLACK":[],"BLUE":[],"GREEN":[],"RED":[],"YELLOW":[],"ORANGE":[],"PURPLE":[],"PINK":[]}
    for i in ["WHITE","BLACK","BLUE","GREEN","RED","YELLOW","ORANGE","PURPLE","PINK"]:
        #writes image if there are contours of that color
        if len(colorDict[i]) != 0:
            rawImg2 = copy.deepcopy(rawImg)
            cv2.drawContours(rawImg2,colorDict[i],-1,(0,255,0),3)
            img_file_dict[i].append(rawImg2)
            #cv2.imwrite(i + "Routes.jpg",rawImg2)
            del rawImg2
    return img_file_dict


