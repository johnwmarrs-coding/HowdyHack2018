import numpy as np
import cv2
import statistics
from identifier import get_color
import copy


#read image and convert to HSV and grayScale
rawImg = cv2.imread('../images/rockWall.jpg')
rawImgHSV = cv2.cvtColor(rawImg,cv2.COLOR_BGR2HSV)
rawImgGray = cv2.cvtColor(rawImg,cv2.COLOR_BGR2GRAY)

#Trying Contour Detection
blur = cv2.GaussianBlur(rawImgGray,(5,5),0)

ret,thresh = cv2.threshold(blur,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#cv2.drawContours(rawImg,contours,-1,(0,255,0),3)
#cv2.imshow("contours",rawImg)
#print(contours)
#print(hierarchy)

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

print("Lower Median: " + str(lower_median))
print("Upper Median: " + str(upper_median))
median = statistics.median(area_list)
print("Median: " + str(median))

mean = statistics.mean(area_list)
standard_dev = statistics.stdev(area_list)

new_contours = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    area_dif = abs(mean - area)
    if (area_dif < 5*standard_dev and area > 50):
        new_contours.append(cnt)


print(np.min(area_list))
#cv2.drawContours(rawImg,new_contours,-1,(0,255,0),3)
#cv2.imshow("contours",rawImg)
#cv2.imshow("Original Contour Mask",im2)


#This is not really needed. can remove
roi_gbr_list = []
#roi_gbr_list = np.array([])

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

    #Sort contours by color
    #BGR to RGB
    colorDict[get_color([roi[2],roi[1],roi[0]])].append(new_contours[i])
    
    #Draws all the Regions of interest. Can Delete. Only needed to test
    #cv2.rectangle(rawImg,(x,y),(x+w,y+h),(0,0,255),2)

#Writing the files

for i in ["WHITE","BLACK","BLUE","GREEN","RED","YELLOW","ORANGE","PURPLE","PINK"]:
    #writes image if there are contours of that color
    if len(colorDict[i]) != 0:
        rawImg2 = copy.deepcopy(rawImg)
        cv2.drawContours(rawImg2,colorDict[i],-1,(0,255,0),3)
        cv2.imwrite(i + "Routes.jpg",rawImg2)
        del rawImg2




#print(roi.shape)
print(len(roi_gbr_list))



cv2.imshow("raw img 1",rawImg)

<<<<<<< HEAD

=======
cv2.imshow("contours",rawImg)
cv2.waitKey(0)
>>>>>>> 155a7c60c6ef627c83be2abb291761ba602b6186


    



