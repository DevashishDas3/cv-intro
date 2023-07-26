import numpy as np
import lane_detection

def get_lane_center(lanes: list):
    center = (lane_detection.get_intercepts(lanes[0][0]) + lane_detection.get_intercepts(lanes[0][1])) / 2
    for i in range(1, len(lanes)):
        lane_center = (lane_detection.get_intercepts(lanes[i][0]) + lane_detection.get_intercepts(lanes[i][1])) / 2
        # we get intercepts for line 1 and line 2 for each lane and get the average
        if np.abs(lane_center - 1000) < np.abs(center - 1000):
            center = lane_center
            slope = (lane_detection.get_slopes(lanes[i][0]) + lane_detection.get_slopes(lanes[i][1])) / 2

    return center, slope
    '''
    x_list = []
    indices = []
    i = 0
    for lane in lanes:
        x1, y1, x2, y2 = lane[0]
        x_list.append(x1)
        i+=1
    for i in range(len(x_list)):
        pass

    for lane in lanes:
        x1, y1, x2, y2 = lane[0]
        center = ((x1 + x2)/2, (y1 + y2)/2)
        slope = (y2 - y1)/(x2 - x1)
    '''
