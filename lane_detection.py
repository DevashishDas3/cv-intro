import cv2 
from matplotlib import pyplot as plt
import numpy as np

def get_slopes_intercepts(lines):
    slopeList = []
    interceptList = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        slope = (y1-y2)/(x1-x2)
        intercept = ((1080-y1)/slope) + x1 #use point slope form
        interceptList.append(intercept)
        slopeList.append(slope)
    
    return slopeList, interceptList


def detect_lines(img, thresh1 = 50, thresh2 = 150, aperture_Size = 3, min_LineLength = 100, max_LineGap = 10): #william vals
    gray = cv2.cvtColor(img, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(gray, thresh1, thresh2, apertureSize=aperture_Size)
    lines = cv2.HoughLinesP(
                edges, #what to draw lines on
                1, #number of lines on each edge
                np.pi/180,
                100,
                minLineLength=min_LineLength, #down goes more frequent, up goes less 300
                maxLineGap=max_LineGap, #inverse relation 30
        ) # detect lines
    return lines
    #i = 1
    '''
    slopes = []
    for line in lines:
        slope = np.round(get_slope(line), 2)
        if slope not in slopes:
            slopes.append(slope)
            cv2.putText(img, f"slope = {slope}", (x2, y2), cv2.FONT_HERSHEY_DUPLEX, 1, (0,225,0), 3)
            
            theta = np.arctan((x2-x1)/(y2-y1))
            theta = np.round(np.degrees(theta), 2)
            cv2.putText(img, f"angle offset = {theta}", (x1, y1), cv2.FONT_HERSHEY_DUPLEX, 1, (0,225,0), 3)
            cv2.line(img, (x1, y1), (x2, y2), (255,0, 0), 2)
        else:
            continue    
        #i+=1
    plt.imshow(img)
    '''
def detect_lanes(line_list):
    lanes = []
    slopeList, interceptList = get_slopes_intercepts(line_list)



    for i in range(len(interceptList)):
        for j in range(i+1, len(interceptList)): #iterate through rest of all elements onward
            slope_difference = abs(slopeList[i] - slopeList[j])
            intercept_difference = abs(interceptList[i] - interceptList[j])

            if slope_difference < 2 and (intercept_difference > 50 and intercept_difference < 1000):
                pass



    i=0
    for slope in slopes:
        if i == len(slopes) - 1:
            break
        if i == 0:
            continue
        if (slopes[i + 1] - slopes[i] < 0.6) and (intercepts[i + 1] - intercepts[i] < 200):
            valid_list1.append([line[i], line[i-1]])
        else:
            continue
    

        

    
    '''
    for j in range(len(valid_list1)):
        pass
    '''

    return valid_list1

def draw_lines(imgin, thresh1in, thresh2in, aperture_Sizein, min_LineLengthin, max_LineGapin):
    pass

cap = cv2.VideoCapture('AUV_Vid.mkv')
ret, frame = cap.read()
draw_lines(frame, 50, 50, 3, 300, 30)