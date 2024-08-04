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
            # get the hit info
            hinfo = scene.getHitList()
            # get the material of the object
            hmat = hinfo.getMaterial()
            # compute scattering
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
                    tolight_dir = light.center - hinfo.getP()
                    tolight_ray = rtr.Ray(hinfo.getP(), tolight_dir)
                    max_distance = tolight_dir.len()
                    occlusion_hit = scene.find_occlusion(tolight_ray, rtu.Interval(0.000001, max_distance))
                    # if not occluded.
                    if not occlusion_hit:
                        # accumulate all unoccluded light
                        Le = Le + (light.material.emitting() * min(1.0, 1.0/max_distance))

            # return the color
            return (Le * sinfo.attenuation_color) + self.compute_scattering(rtr.Ray(hinfo.getP(), sinfo.scattered_ray.getDirection()), scene, maxDepth-1) * sinfo.attenuation_color

        """4. Render a scene with at least 2 mirrors and the sky background (no point light)."""
        return scene.get_sky_background_color(rGen_ray)
        # return scene.getBackgroundColor()

