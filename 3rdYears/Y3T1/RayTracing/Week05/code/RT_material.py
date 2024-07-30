# material class
import RT_utility as rtu
import RT_ray as rtr

class Material:
    def __init__(self) -> None:
        pass

    def scattering(self, rRayIn, hHinfo):
        pass

    def is_light(self):
        return False

class Lambertian(Material):
    def __init__(self, cAlbedo) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())

    def scattering(self, rRayIn, hHinfo):
        scattered_direction = hHinfo.getNormal() + rtu.Vec3.random_vec3_unit()
        if scattered_direction.near_zero():
            scattered_direction = hHinfo.getNormal()

        scattered_ray = rtr.Ray(hHinfo.getP(), scattered_direction)
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        return rtu.Scatterinfo(scattered_ray, attenuation_color)
    

