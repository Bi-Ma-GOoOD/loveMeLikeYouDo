# Scene class
import RT_utility as rtu
import numpy as np

class Scene:
    def __init__(self) -> None:
        self.obj_list = []
        self.hit_list = None
        pass

    def add_object(self, obj):
        self.obj_list.append(obj)

    def find_intersection(self, vRay, cInterval):

        np_obj_list = np.array(self.obj_list)
        found_hit = False
        # initialize the closet maximum of t
        closest_tmax = cInterval.max_val
        hinfo = None
        # for each object in the given scene
        for obj in np_obj_list:
            # get the hit info from the intersection between an object and the given ray.
            hinfo = obj.intersect(vRay, rtu.Interval(cInterval.min_val, closest_tmax))
            # if the object is hit by the given ray.
            if hinfo is not None:
                # update the closet maximum of t
                # update the hit list
                closest_tmax = hinfo.getT()
                found_hit = True
                self.hit_list = hinfo
        # return if found any hit or not
        return found_hit


    def getHitNormalAt(self, idx):
        return self.hit_list[idx].getNormal() 
    
    def getHitList(self):
        return self.hit_list


