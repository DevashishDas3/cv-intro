import numpy as np
import cv2
import matplotlib.pyplot as plt
import random as rand


def detect_lines(img, threshold1=50, threshold2=150, apertureSize=3, minLineLength=100,maxLineGap=10):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert to grayscale
    edges = cv2.Canny(gray, threshold1, threshold2, apertureSize) # detect edges


    slope_list=[]
    line_list=[]
    color_order=[(0,255,0),(0,0,255),(255,0,0),(100,100,100),(0,0,0),(150,30,90),(180,50,20)]
    color_order=[(0,255,0)]
    i=0
    j=0

    lines = cv2.HoughLinesP(edges,7,np.pi/30,50,minLineLength,maxLineGap,) # detect lines
    return(lines)

    


def draw_lines(img, lines, color=(0,255,0)):
    slope_list=[]
    line_list=[]
    i=0
    j=0
    if lines is not None:
        for line in lines:
            if line is not None:
                x1, y1, x2, y2 = line[0]
                if (x2-x1)==0:
                    x2+=.00000001
                slope=(y2-y1)/(x2-x1)
                slope_list.append(slope)
                line_list.append(([x1,y1,x2,y2]))
                i+=1
                i=i%6
                j+=1

                for k in range(len(slope_list)):
                    if np.abs(slope)>.9:
                        if round(slope,2) ==round(slope_list[k],2):
                            cv2.line(img,(x1,y1),(line_list[k][2],line_list[k][3]),color,10)
                        else:
                            cv2.line(img, (x1, y1), (x2, y2), color, 2)
    plt.show(img)
    plt.imshow(img)
    return(img)

def get_slopes_intercepts(lines):
    slopes=[]
    intercepts=[]
    slope=0

    for line in lines:
        if line is not None:
            x1, y1, x2, y2 = line[0]
            if (x2-x1)!=0:
                slope=(y2-y1)/(x2-x1)
            else:
                slope=(y2-y1)/.00000000000001
            slopes.append(slope)
            intercepts.append((-y1/slope)+x1)


# def detect_lanes(lines):
#     slopes=[]
#     intercepts=[]
#     get_slopes_intercepts(lines)


#     lanes=[]
#     ##optional, turn slopes into tuples or something concrete because they don't change and it will make code more efficient
#     j=0
#     parallel_lines=[]
#     for slope in slopes:
#         i=j
#         while i < len(slopes):
#             if  slope ==slopes[i]:
#                 lanes.append([])
#           (x1,x2,x3,x4)
    


##Jules wrote this
def detect_lanes(lines):
    i = 0
    lanes = []
    while i <= len(get_slopes_intercepts(lines)[0]):
        j = 0
        #if parrelel then it is a lane
        while j < i:
            m = round(get_slopes_intercepts(lines)[0][j], 1)
            a = round(get_slopes_intercepts(lines)[0][i],1)

            if (m <= 0.2+a or m >= a-0.2):
                lanes.append([lines[j], lines[i]])
            j+=1
        #if eventualy going to intersect but not currently intersecting it is a lane

        i+=1


##Rome wrote this
def get_color():
    #gets integer from 0 to 255, inclusive or not isn't really important
    c=rand.randint(0,255)
    b=rand.randint(0,255)
    a=rand.randint(0,255)
    #returns tuple you can use that 
    return((a,b,c))


def draw_lanes(img, lanes):

    for lane in lanes:
        for line in lane:
            draw_lines(img,line,get_color())

##AJ Wrote this
def get_lane_center(lanes):
    ##get_slopes_intercepts returns the slope and intercept in a tuple, lanes[0][0] gets the first line in the first lane
    
    center = (get_slopes_intercepts(lanes[0][0])[1] + get_slopes_intercepts(lanes[0][1])[1]) / 2
    for i in range(1, len(lanes)):
        lane_center = (get_slopes_intercepts(lanes[i][0])[1] + get_slopes_intercepts(lanes[i][1])[1]) / 2
        # we get intercepts for line 1 and line 2 for each lane and get the average
        if np.abs(lane_center - 960) < np.abs(center - 960):
            center = lane_center
            slope = (get_slopes_intercepts(lanes[i][0])[0] + get_slopes_intercepts(lanes[i][1])[0]) / 2

    return center, slope

def recommend_direction(center,slope):
    #Gets if center is within 10 pixels of 960, it returns forward, otherwise gets back to center
    if center< 950:
        return("left")
    elif center>970:
        return("right")
    elif center <970 and center>950:
        return("forward")
    else:
        return("cannot generate direction recommendation...")


if __name__ ==  "__main__":
    draw_lines()


    

#if the slopes are equal or if their x1 coordinates are equally distant from the midpoint of their x2 coordinates