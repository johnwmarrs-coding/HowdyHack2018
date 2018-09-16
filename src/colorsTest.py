import numpy as np
import cv2
import statistics
#read image and convert to HSV and grayScale
rawImg = cv2.imread('../images/rockWall.jpg')
rawImgHSV = cv2.cvtColor(rawImg,cv2.COLOR_BGR2HSV)
rawImgGray = cv2.cvtColor(rawImg,cv2.COLOR_BGR2GRAY)

#Color Ranges in HSV
#Colors: green, blue, yellow, orange, red, pink, black, white
#test using green, red, yellow first
lowerGreen = np.array([40,100,0])
upperGreen = np.array([80,255,255])
lowerRed = np.array([136,87,111])
upperRed = np.array([180,255,255])
lowerYellow = np.array([22,60,200])
upperYellow = np.array([60,255,255])

#maskYellow = cv2.inRange(rawImgHSV,lowerYellow,upperYellow)
#testImg = cv2.bitwise_and(rawImg,rawImg,mask=maskYellow)


#Trying Contour Detection
blur = cv2.GaussianBlur(rawImgGray,(5,5),0)
#blur = cv2.GaussianBlur(rawImg,(5,5),0)

ret,thresh = cv2.threshold(blur,127,255,0)
im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


#cv2.imshow("contours",im2)
#cv2.imshow("blur",blur)

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
cv2.drawContours(rawImg,new_contours,-1,(0,255,0),3)
#cv2.imshow("contours",rawImg)
#cv2.imshow("Original Contour Mask",im2)


#This is not really needed. can remove
roi_hsv_list = []
#roi_gbr_list = np.array([])

#array to collect contours of different colors
colorDict = {"white":[],"black":[],"blue":[],"red":[],"yellow":[],"orange":[],"purple":[],"pink":[]}
for i in range(0,len(new_contours)):
    cnt = new_contours[i]
    x,y,w,h = cv2.boundingRect(cnt)

    #roi_list.append(rawImg[x:x+w,y:y+h])
    #Roi w,y,w,h
    x = x + int(round(.25*w))
    y = y + int(round(.25*h))
    w = int(.5*w)
    h = int(.5*h)

    roi = rawImgHSV[y:y+h,x:x+w]
    flatRoi = roi.shape[0]*roi.shape[1]
    roi = roi.reshape([flatRoi,3])
    #roi = np.mean(roi,axis=0)
    roi = np.median(roi,axis=0)
    
    roi_hsv_list.append(roi) #HSV of all regions of interest
    #roi_gbr_list = np.append(roi_gbr_list,roi)

    #Sort contours by color
    #colorDict[function(roi)].append(new_contours[i])
    
    #Draws all the Regions of interest. Can Delete. Only needed to test
    #cv2.rectangle(rawImg,(x,y),(x+w,y+h),(0,0,255),2)

#Writing the files
for i in ["white","black","blue","red","yellow","orange","purple","pink"]:
    #writes image if there are contours of that color
    if len(colorDict[i]) != 0:
        rawImg2 = rawImg
        cv2.drawContours(rawImg2,colorDict[i],-1,(0,255,0),3)
        cv2.imwrite(i + "Routes.jpg",rawImg2)
        del rawImg2




#print(roi.shape)
#print(roi)
#print(roi_hsv_list)


cv2.imshow("contours",rawImg)
cv2.waitKey(0)


    



