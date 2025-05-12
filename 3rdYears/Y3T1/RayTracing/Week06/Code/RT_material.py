# material class
import RT_utility as rtu
import RT_ray as rtr
import math

def reflect(vRay, vNormal):
    """1. Implement 'reflect()' function to support a mirror material."""
    # return the perfect reflection direction
    return vRay - vNormal*rtu.Vec3.dot_product(vRay, vNormal)*2.0

def refract(vRay, vNormal, fRefractRatio):
    cos_theta = min(rtu.Vec3.dot_product(-vRay, vNormal), 1.0)
    sin_theta = math.sqrt(1.0 - cos_theta*cos_theta)
    cannot_refract = fRefractRatio*sin_theta > 1.0

    if cannot_refract or schlick(cos_theta, fRefractRatio) > rtu.random_double():
        return reflect(vRay, vNormal)
    else:
        perpendiular_dir = (vRay + vNormal*cos_theta)*fRefractRatio
        parallel_dir = vNormal*(-math.sqrt(math.fabs(1.0 - perpendiular_dir.len_squared())))
        return perpendiular_dir + parallel_dir

def schlick(fCosine, fIOR):
    r0 = (1-fIOR) / (1+fIOR)
    r0 = r0*r0
    return r0 + (1-r0)*math.pow(1-fCosine, 5)

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
    
# a mirror class
class Mirror(Material):
    def __init__(self, cAlbedo) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())

    def scattering(self, rRayIn, hHinfo):
        """2. Implement Mirror class by using 'reflect()' function."""
        # generate a reflected ray
        reflected_ray = rtr.Ray(hHinfo.getP(), reflect(rRayIn.getDirection(), hHinfo.getNormal()))
        # get attenuation_color
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        # return scattering info
        return rtu.Scatterinfo(reflected_ray, attenuation_color)
    
"""5. Implement Dielectric class by using 'refract()' function."""
# A dielectric transparent material 
class Dielectric(Material):
    def __init__(self, cAlbedo, fIor) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.IOR = fIor

    def scattering(self, rRayIn, hHinfo):

        refract_ratio = self.IOR
        if hHinfo.front_face:
            refract_ratio = 1.0/self.IOR

        # generate a refracted ray
        attenuation_color = self.color_albedo
        unit_direction = rtu.Vec3.unit_vector(rRayIn.getDirection())
        refracted_ray = refract(unit_direction, hHinfo.getNormal(), refract_ratio)
        scattered_ray = rtr.Ray(hHinfo.getP(), refracted_ray) 


        # return scattering info
        return rtu.Scatterinfo(scattered_ray, attenuation_color)

