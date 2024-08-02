# a simple integrator class
# A ray is hit and then get the color.
# It is the rendering equation solver.
import RT_utility as rtu
import RT_ray as rtr

class Integrator():
    def __init__(self, bDlight=True) -> None:
        self.bool_direct_lighting = bDlight
        pass

    def compute_scattering(self, rGen_ray, scene, maxDepth):    

        if maxDepth <= 0:
            return rtu.Color()

        # if the generated ray hits an object
        found_hit = scene.find_intersection(rGen_ray, rtu.Interval(0.000001, rtu.infinity_number))
        if found_hit == True:
            # get the hit information. If there's an intersection, this line retrieves the information about the hit point
            hinfo = scene.getHitList()
            # get the material of the object from hinfo
            hmat = hinfo.getMaterial()
            # compute scattering
            # attenuation color = light intensity
            sinfo = hmat.scattering(rGen_ray, hinfo)
            # if no scattering (It is a light source)
            if sinfo is None:
                # return Le
                return hmat.emitting()

            Le = rtu.Color()
            # if direct lighting is enabled
            if self.bool_direct_lighting:
                # for each point light
                for light in scene.point_light_list:
                    # check if there is an occlusion between a point light and a surface point.
                    """1. Implement direct lighting effect in the 'compute_scattering()' method. 
                    As of now, the direct lighting only handle point lights."""
                    #from_obj_to_light = calculate direction vector from the hit point to the center of the current point light.
                    #build_new_ray = create a new ray from the hit point to the point light.
                    #dis_from_hit_to_light = calculate the distance between the hit point and the point light.
                    #occlusion_obj = check if there is an occlusion between the hit point and the point light.
                    from_obj_to_light = light.center - hinfo.getP()
                    build_new_ray = rtr.Ray(hinfo.getP(), from_obj_to_light)
                    dis_from_hit_to_light = from_obj_to_light.len()
                    occlusion_obj = scene.find_occlusion(build_new_ray, rtu.Interval(0.000001, dis_from_hit_to_light))
                    # if not occluded.
                    if not occlusion_obj:
                        # accumulate all unoccluded light
                        Le = Le + (light.material.emitting() * (1/dis_from_hit_to_light))
            # return the color
            return (Le * sinfo.attenuation_color) + self.compute_scattering(rtr.Ray(hinfo.getP(), sinfo.scattered_ray.getDirection()), scene, maxDepth-1) * sinfo.attenuation_color
        return scene.getBackgroundColor()

