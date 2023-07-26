import numpy as np

def get_lane_center(lanes: list):
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
