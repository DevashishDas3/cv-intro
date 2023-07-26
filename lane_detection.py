import cv2 
from matplotlib import pyplot as plt
import numpy as np

def get_slopes(line, m):
    x1, y1, x2, y2 = line[0]
    m.append((y2 - y1) / (x2 - x1))

def get_intercepts(line, ints):
    x1, y1, x2, y2 = line[0]
    m=(y2 - y1) / (x2 - x1)
    ints.append(((0-y1)/m) + x1)

def analyze_lines(img, thresh1, thresh2, aperture_Size, min_LineLength, max_LineGap):
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
def analyze_lanes(line_list):
    slopes = []
    intercepts = []
    valid_list1 = []
    valid_list2 = []
    lane_list = []
    indices = []

    for line in line_list:
        get_slopes(line, slopes)
        get_intercepts(line, intercepts)
    
    slopes.sort()
    intercepts.sort()

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
    lines = analyze_lines(imgin, thresh1in, thresh2in, aperture_Sizein, min_LineLengthin, max_LineGapin)
    lines = analyze_lanes(lines)
    print(lines)
    i = 0
    slopes_1 = []
    intercepts_1 = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        get_slopes(line, slopes_1)
        get_intercepts(line, intercepts_1)
        
        cv2.putText(imgin, f"slope = {slopes_1[i]}", (x2, y2), cv2.FONT_HERSHEY_DUPLEX, 1, (0,225,0), 3)

        theta = np.arctan((x2-x1)/(y2-y1))
        theta = np.round(np.degrees(theta), 2)
        cv2.putText(imgin, f"angle offset = {theta}", (x1, y1), cv2.FONT_HERSHEY_DUPLEX, 1, (0,225,0), 3)
        cv2.line(imgin, (x1, y1), (x2, y2), (255,0, 0), 2)
        i+=1
    plt.imshow(imgin)

cap = cv2.VideoCapture('AUV_Vid.mkv')
ret, frame = cap.read()
draw_lines(frame, 50, 50, 3, 300, 30)