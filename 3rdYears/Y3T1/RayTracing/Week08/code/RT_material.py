# material class
import RT_utility as rtu
import RT_ray as rtr
import math
import RT_texture as rtt

def reflect(vRay, vNormal):
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

def halfvector(vView, vLight):
    vH = (vView + vLight)*0.5
    return vH

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
        attenuation_color = self.BRDF(rRayIn, scattered_ray, hHinfo)
        return rtu.Scatterinfo(scattered_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        return attenuation_color


# a mirror class
class Mirror(Material):
    def __init__(self, cAlbedo) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())

    def scattering(self, rRayIn, hHinfo):
        # generate a reflected ray
        reflected_ray = rtr.Ray(hHinfo.getP(), reflect(rRayIn.getDirection(), hHinfo.getNormal()))

        # get attenuation_color
        attenuation_color = self.BRDF(rRayIn, reflected_ray, hHinfo)

        # return scattering info
        return rtu.Scatterinfo(reflected_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        return attenuation_color


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
        uv = rtu.Vec3.unit_vector(rRayIn.getDirection())
        refracted_dir = refract(uv, hHinfo.getNormal(), refract_ratio)
        scattered_ray = rtr.Ray(hHinfo.getP(), refracted_dir)

        attenuation_color = self.BRDF(rRayIn, scattered_ray, hHinfo)
        # return scattering info
        return rtu.Scatterinfo(scattered_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        return attenuation_color

# a texture
class TextureColor(Material):
    def __init__(self, color_or_texture) -> None:
        super().__init__()
        if isinstance(color_or_texture, rtu.Color):
            self.color_albedo = rtt.SolidColor(color_or_texture)
        else:
            self.color_albedo = color_or_texture

    def scattering(self, rRayIn, hHinfo):
        scattered_direction = hHinfo.getNormal() + rtu.Vec3.random_vec3_unit()
        if scattered_direction.near_zero():
            scattered_direction = hHinfo.getNormal()

        scattered_ray = rtr.Ray(hHinfo.getP(), scattered_direction)
        attenuation_color = self.BRDF(rRayIn, scattered_ray, hHinfo)

        return rtu.Scatterinfo(scattered_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = self.color_albedo.tex_value(hHinfo.u, hHinfo.v, hHinfo.point)
        return attenuation_color


# A metal class with roughness parameter
class Metal(Material):
    def __init__(self, cAlbedo, fRoughness) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.roughness = fRoughness
        if self.roughness > 1.0:
            self.roughness = 1.0

    def scattering(self, rRayIn, hHinfo):
        # compute scattered ray based on the roughtness parameter
        reflected_direction = reflect(rtu.Vec3.unit_vector(rRayIn.getDirection()), hHinfo.getNormal()) + rtu.Vec3.random_vec3_unit()*self.roughness
        reflected_ray = rtr.Ray(hHinfo.getP(), reflected_direction)
        attenuation_color = self.BRDF(rRayIn, reflected_ray, hHinfo)

        # check if the reflected direction is below the surface normal
        if rtu.Vec3.dot_product(reflected_direction, hHinfo.getNormal()) <= 1e-8:
            attenuation_color = rtu.Color(0,0,0)

        return rtu.Scatterinfo(reflected_ray, attenuation_color)

    def BRDF(self, rView, rLight, hHinfo):
        attenuation_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b())
        return attenuation_color    

"""1. Complete 'scattering()' and 'BRDF()' methods in the 'class Phong(Material)' to represent the Phong BRDF."""
# Phong reflection model
# fr = kd + ks*(R.V)^roughness
class Phong(Material):
    def __init__(self, cAlbedo, kd, ks, fAlpha) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.kd = kd
        self.ks = ks
        self.alpha = fAlpha

    def scattering(self, rRayIn, hHinfo):
        reflected_direction = -hHinfo.getNormal()
        # check if the reflected direction is below the surface normal
        while rtu.Vec3.dot_product(reflected_direction, hHinfo.getNormal()) <= 1e-8:

            # compute scattered ray
            reflected_direction = hHinfo.getNormal() + rtu.Vec3.random_vec3_unit()
            if reflected_direction.near_zero():
                reflected_direction = hHinfo.getNormal()

        reflected_ray = rtr.Ray(hHinfo.getP(), reflected_direction)
        phong_color = self.BRDF(rRayIn, reflected_ray, hHinfo)

        return rtu.Scatterinfo(reflected_ray, phong_color)

    def BRDF(self, rView, rLight, hHinfo):
        # calculate diffuse color
        diff_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b()) * self.kd * (1.0/math.pi)
        reflection_vector = rtu.Vec3.unit_vector(reflect(-rLight.getDirection(), hHinfo.getNormal()))
        view_direction_vector = rtu.Vec3.unit_vector(-rView.getDirection())
        r_dot_v = max(0.0, rtu.Vec3.dot_product(reflection_vector, view_direction_vector))
        spec_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b()) * self.ks * math.pow(r_dot_v, self.alpha)

        return diff_color + spec_color

"""2. Implement 'class Blinn(Material)'."""
# Blinn-Phong reflection model
# fr = kd + ks*(H.N)^roughness
class Blinn(Material):
    def __init__(self, cAlbedo, kd, ks, fAlpha) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.kd = kd
        self.ks = ks
        self.alpha = fAlpha

    def scattering(self, rRayIn, hHinfo):
        reflected_direction = -hHinfo.getNormal()
        while rtu.Vec3.dot_product(reflected_direction, hHinfo.getNormal()) <= 1e-8:
            reflected_direction = hHinfo.getNormal() + rtu.Vec3.random_vec3_unit()
            if reflected_direction.near_zero():
                reflected_direction = hHinfo.getNormal()

        reflected_ray = rtr.Ray(hHinfo.getP(), reflected_direction)
        blinn_color = self.BRDF(rRayIn, reflected_ray, hHinfo)

        return rtu.Scatterinfo(reflected_ray, blinn_color)

    def BRDF(self, rView, rLight, hHinfo):
        # calculate diffuse color
        diff_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b()) * self.kd * (1.0/math.pi)
        half_way_vector = rtu.Vec3.unit_vector(halfvector(-rView.getDirection(), rLight.getDirection()))
        h_dot_n = max(0.0, rtu.Vec3.dot_product(half_way_vector, hHinfo.getNormal()))
        spec_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b()) * self.ks * math.pow(h_dot_n, self.alpha)

        return diff_color + spec_color
    
"""3. Implement 'class CookTorrance(Material)'. The parameters and equations used in the Cook-Torrance model is in the link."""
# Cook-Torrance BRDF model
# fr = kd/pi + ks*(DFG/4(w_o.N * w_i.N))
class CookTorrance(Material):
    def __init__(self, cAlbedo, kd, ks, froughness, fIor) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())
        self.kd = kd
        self.ks = ks
        self.roughness = froughness
        self.IOR = fIor

    def normal_distribution(self, froughness, h_dot_n):
        a = math.pow(froughness, 2)
        a2 = a * a
        h_dot_n2 = h_dot_n * h_dot_n

        denom = (h_dot_n2 * (a2 - 1.0) + 1.0)
        return a2 / (math.pi * denom * denom)
    
    def geometry_schlick_ggx(fCosine, froughness, n_dot_v):
        r = 0.5 + 0.5 * froughness
        k = (r * r) / 2.0
        denom = n_dot_v * (1.0 - k) + k
        return max(n_dot_v, 0.0) / denom
    
    def geometry_smith(self, v_dot_n, l_dot_n, froughness):
        g1_v = self.geometry_schlick_ggx(v_dot_n, froughness)
        g1_l = self.geometry_schlick_ggx(l_dot_n, froughness)
        return g1_v * g1_l

    def scattering(self, rRayIn, hHinfo):
        reflected_direction = -hHinfo.getNormal()
        while rtu.Vec3.dot_product(reflected_direction, hHinfo.getNormal()) <= 1e-8:
            reflected_direction = hHinfo.getNormal() + rtu.Vec3.random_vec3_unit()
            if reflected_direction.near_zero():
                reflected_direction = hHinfo.getNormal()

        reflected_ray = rtr.Ray(hHinfo.getP(), reflected_direction)
        cook_torrence = self.BRDF(rRayIn, reflected_ray, hHinfo)

        return rtu.Scatterinfo(reflected_ray, cook_torrence)

    def BRDF(self, rView, rLight, hHinfo):
        n_vector = hHinfo.getNormal()
        half_way_vector = rtu.Vec3.unit_vector(halfvector(-rView.getDirection(), rLight.getDirection()))
        view_direction_vector = rtu.Vec3.unit_vector(-rView.getDirection())
        v_dot_n = rtu.Interval(0, 1).clamp(max(0.0, rtu.Vec3.dot_product(view_direction_vector, n_vector)))
        n_dot_l = rtu.Interval(0, 1).clamp(max(0.0, rtu.Vec3.dot_product(n_vector, rLight.getDirection())))
        h_dot_n = rtu.Interval(0, 1).clamp(max(0.0, rtu.Vec3.dot_product(half_way_vector, n_vector)))
        v_dot_h = rtu.Interval(0, 1).clamp(max(0.0, rtu.Vec3.dot_product(view_direction_vector, half_way_vector)))

        # f0 = (self.IOR * math.pow(self.roughness, 2))
        # call fresnel schlick
        F = schlick(v_dot_h, self.IOR)
        # call normal distribution
        D = self.normal_distribution(h_dot_n, self.roughness)
        # call geometry
        G = self.geometry_smith(v_dot_n, n_dot_l, self.roughness)
        # calculate diffuse color
        full_cook = (F * D * G) / max((4.0 * (v_dot_n * n_dot_l)), 1e-5)
        diff_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b()) * self.kd * (1.0/math.pi)
        spec_color = rtu.Color(self.color_albedo.r(), self.color_albedo.g(), self.color_albedo.b()) * self.ks * full_cook
        
        return diff_color + spec_color
    