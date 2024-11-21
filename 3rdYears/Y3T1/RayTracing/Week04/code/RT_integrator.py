# a simple integrator class
# A ray is hit and then get the color.
# It is the rendering equation solver.
import RT_utility as rtu
import RT_ray as rtr

class Integrator():
    def __init__(self) -> None:
        pass

    def compute_scattering(self, rGen_ray, scene):
        # if the generated ray hits an object
        found_hit = scene.find_intersection(rGen_ray, rtu.Interval(0.000001, rtu.infinity_number))
        if found_hit == True:
            # get the hit info
            hinfo = scene.getHitList()
            # get the material of the object
            hmat = hinfo.getMaterial()
            # return the color
            return hmat.color_albedo

        return self.background_color(rGen_ray)

    def background_color(self, rGen_ray):
        unit_direction = rtu.Vec3.unit_vector(rGen_ray.getDirection())
        a = (unit_direction.y() + 1.0)*0.5
        return rtu.Color(1,1,1)*(1.0-a) + rtu.Color(0.5, 0.7, 1.0)*a

    # def get_color(self, rGen_ray, scene):

    #     found_hit = scene.find_intersection(rGen_ray, rtu.Interval(0.000001, rtu.infinity_number))
    #     if found_hit == True:
    #         tmpN = scene.getHitList().getNormal()
    #         return (rtu.Color(tmpN.x(), tmpN.y(), tmpN.z()) + rtu.Color(1,1,1))*0.5

    #     return self.background_color(rGen_ray)
