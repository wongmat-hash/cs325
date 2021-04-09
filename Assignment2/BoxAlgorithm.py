
class Point:
    def _init_(self, x, y):
        self.x = x
        self.y = y

#return true if ttwo rectangles overlap
def doOverlap(l1, r1, l2, r2):
    #check if its actually a line
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
    if _name_ == "_main_":
        l1 = Point(0, 0)
        r1 = Point(2, 2)
        l2 = Point(1, 1)
        r2 = Point(3, 3)

    if(doOverlap(l1, r1, l2, r2)):
        print("true")
    else:
        print("false")
