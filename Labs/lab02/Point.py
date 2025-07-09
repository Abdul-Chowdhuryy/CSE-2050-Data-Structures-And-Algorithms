class Point:
    def __init__(self, x, y):
        """Initializes a 2-D point with x- and y- coordinates"""
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        """Making sure x and y cordinates of both are equal to eachother"""
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def equidistant(self, other):
        """Making sure the distance of both point is equal"""
        if ((self.x ** 2 + self.y ** 2)**(1/2)) == ((other.x ** 2 + other.y ** 2)**(1/2)):
            return True
        else:
            return False
    def within(self, distance, other):
     """Making sure the distance is less than the sqrt of x and y also pythagorean therom"""
     if ((other.x - self.x)**2 + (other.y - self.y)**2) ** 0.5 <= distance:
        return True
     else: 
        return False

   