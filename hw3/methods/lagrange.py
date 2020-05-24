from .common import Point

'''Interpolate by Lagrange method
return coordinates in list [(x1, y1), ...]
'''
def lagrange(data: Point, minVal=0, maxVal=10, off=0.001):
    p = []
    x = minVal
    while x <= maxVal:
        ansY = 0
        for i in range(len(data)):
            tmp = 1
            for j in range(len(data)):
                if i == j:
                    continue
                tmp *= (x - data[j].x) / (data[i].x - data[j].x)
            ansY += tmp * data[i].y
        p.append(Point(x, ansY))
        x += off

    return p
