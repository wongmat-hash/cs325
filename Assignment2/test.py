class Solution:
   def isRectangleOverlap(self, R1, R2):
      if (R1[0]>=R2[2]) or (R1[2]<=R2[0]) or (R1[3]<=R2[1]) or
         (R1[1]>=R2[3]):
         return False
      else:
   return True
ob = Solution()
print(ob.isRectangleOverlap([0,0,2,2],[1,1,3,3]))



#work cited: https://gamedevelopment.tutsplus.com/tutorials/collision-detection-using-the-separating-axis-theorem--gamedev-169
#work cited: https://stackoverflow.com/questions/40795709/checking-whether-two-rectangles-overlap-in-python-using-two-bottom-left-corners
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#return true if two rectangles overlap
def overlap(l1, r1, l2, r2):
    #if one rectangle is on left side of other
    if (l1.x >= r2.x or l2.x >= r1.x) or (l1.y <= r2.y or l2.y <= r1.y):
        return False
	else:
    return True

#drive code
if __name__ == "__main__":
    l1 = Point(0, 0)
    r1 = Point(1, 1)
    l2 = Point(1, 0)
    r2 = Point(2, 1)
    if(overlap(l1, r1, l2, r2)):
        print("true")
    else:
        print("false")
