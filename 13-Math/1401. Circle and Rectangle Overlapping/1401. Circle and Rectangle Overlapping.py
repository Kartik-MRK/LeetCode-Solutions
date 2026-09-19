1class Solution:
2    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
3
4        xclosest=min(max(xCenter,x1),x2)
5        yclosest=min(max(yCenter,y1),y2)
6        dx=xCenter-xclosest
7        dy=yCenter-yclosest
8        return dx*dx+dy*dy<=radius*radius
9        
10        