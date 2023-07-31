import cv2 
from matplotlib import pyplot as plt
import numpy as np

def detect_lines(img, thresh1 = 50, thresh2 = 150, apertureSize = 3, minLineLength = 100, maxLineGap = 10):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale
    edges = cv2.Canny(gray, thresh1, thresh2, apertureSize)
    lines = cv2.HoughLinesP(
            edges,
            1,
            np.pi/180,
            100,
            minLineLength = minLineLength,
            maxLineGap = maxLineGap,
    )
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

def draw_lines(img, lines):
    try:
        for line in lines:
            try:
                x1, y1, x2, y2 = line[0]
            except:
                print("Only three vals")
                continue
            cv2.line(img, (x1, y1), (x2, y2), (255,0,0), 2)
    except:
        pass

    return img #.tolist()

def get_slopes_intercepts(lines):
    slopeList = []
    interceptList = []

    for line in lines:
        x1, y1, x2, y2 = line[0]
        if (x1-x2) != 0 and (y1-y1) != 0: 
            slope = (y1-y2)/(x1-x2)
            intercept = ((1080-y1)/slope) + x1 #use point slope form
            interceptList.append(intercept)
            slopeList.append(slope)
        else:
            continue

    return slopeList, interceptList

def detect_lanes(line_list):
    lanes = []
    slopeList, interceptList = get_slopes_intercepts(line_list)
    if len(interceptList) > 1:
        for i in range(0, len(interceptList)):
            for j in range(i+1, len(interceptList)): #iterate through rest of all elements onward
                slope_difference = abs(slopeList[i] - slopeList[j])
                intercept_difference = abs(interceptList[i] - interceptList[j])

                if True: #slope_difference < 1 and (intercept_difference > 100 and intercept_difference < 1000):
                    xCoord = ((slopeList[i] * interceptList[i]) - (slopeList[j] * interceptList[j]))/(slopeList[i] - slopeList[j])
                    yCoord = slopeList[i] * (xCoord - interceptList[i]) + 1080
                    lanes.append([[interceptList[i], 1080, xCoord, yCoord], [interceptList[j], 1080, xCoord, yCoord]])
    print(lanes)
    return lanes

def draw_lanes(img, lanes):
    for lane in lanes:
        for line in lane:
            x1, y1, x2, y2 = line
            cv2.line(img, int(x1), int(y1), int(x2), int(y2), (255,0,0), 2)
    return img

