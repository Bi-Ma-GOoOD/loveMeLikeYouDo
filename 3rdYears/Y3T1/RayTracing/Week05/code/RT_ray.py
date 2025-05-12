# Ray class
import RT_utility as rtu

class Ray:
    def __init__(self, vOrigin=rtu.Vec3(), vDir=rtu.Vec3()) -> None:
        self.origin = vOrigin
        self.direction = vDir
        pass

    def at(self, t):
        return self.origin + self.direction*t

    def getOrigin(self):
        return self.origin
    
    def getDirection(self):
        return self.direction
    

