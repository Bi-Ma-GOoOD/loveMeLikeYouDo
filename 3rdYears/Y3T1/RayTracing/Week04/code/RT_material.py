# material class
import RT_utility as rtu
import RT_ray as rtr

class Material:
    def __init__(self) -> None:
        pass

    def scattering(self, rRayIn, hHinfo):
        pass

class Lambertian(Material):
    def __init__(self, cAlbedo) -> None:
        super().__init__()
        self.color_albedo = rtu.Color(cAlbedo.r(), cAlbedo.g(), cAlbedo.b())

    def scattering(self, rRayIn, hHinfo):
        return None

