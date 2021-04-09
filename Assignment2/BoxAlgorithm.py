
#work cited: https://gamedevelopment.tutsplus.com/tutorials/collision-detection-using-the-separating-axis-theorem--gamedev-169
#work cited: https://stackoverflow.com/questions/40795709/checking-whether-two-rectangles-overlap-in-python-using-two-bottom-left-corners
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#return true if two rectangles overlap
def overlap(l1, r1, l2, r2):
    #check if its actually a line this makes it impossible 
    if (l1.x == r1.x or l1.y == r2.y or l2.x == r2.x or l2.y == r2.y):
        return False    #line cannot have positive overlap

    #if one rectangle is on left side of other
    if (l1.x >= r2.x or l2.x >= r1.x):
        return False

    #if one rectangle is above other
    if(l1.y <= r2.y or l2.y <= r1.y):
        return False

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
