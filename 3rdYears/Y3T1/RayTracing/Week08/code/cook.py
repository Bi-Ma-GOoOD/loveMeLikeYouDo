import numpy as np

class CookTorrance():
    def __init__(self, cAlbedo, kd, ks) -> None:
        super().__init__()
        self.cAlbedo = cAlbedo  # Albedo color
        self.kd = kd            # Diffuse reflection coefficient
        self.ks = ks            # Specular reflection coefficient

    def fresnel_schlick(self, cos_theta, F0):
        """
        Schlick's approximation for Fresnel factor.
        :param cos_theta: Cosine of the angle between the incident direction and the normal.
        :param F0: Fresnel reflectance at normal incidence.
        :return: Fresnel factor (float).
        """
        return F0 + (1 - F0) * (1 - cos_theta) ** 5

    def normal_distribution_ggx(self, NdotH, roughness):
        """
        GGX (Trowbridge-Reitz) normal distribution function.
        :param NdotH: Cosine of the angle between normal and half-vector.
        :param roughness: Surface roughness (float between 0 and 1).
        :return: Normal distribution factor (float).
        """
        a = roughness ** 2
        a2 = a * a
        NdotH2 = NdotH * NdotH

        denom = (NdotH2 * (a2 - 1.0) + 1.0)
        return a2 / (np.pi * denom * denom)

    def geometry_smith(self, NdotV, NdotL, roughness):
        """
        Smith's geometry function using Schlick-GGX.
        :param NdotV: Cosine of the angle between normal and view direction.
        :param NdotL: Cosine of the angle between normal and light direction.
        :param roughness: Surface roughness (float between 0 and 1).
        :return: Geometry factor (float).
        """
        def geometry_schlick_ggx(cos_theta, roughness):
            k = (roughness + 1.0) ** 2 / 8.0
            return cos_theta / (cos_theta * (1.0 - k) + k)

        return geometry_schlick_ggx(NdotV, roughness) * geometry_schlick_ggx(NdotL, roughness)

    def scattering(self, rRayIn, hHinfo):
        # Placeholder for scattering behavior (if needed)
        return None

    def BRDF(self, rView, rLight, hHinfo):
        # Extract required vectors and scalars
        N = hHinfo.normal
        H = (rView + rLight) / np.linalg.norm(rView + rLight)
        NdotV = max(np.dot(N, rView), 0.0)
        NdotL = max(np.dot(N, rLight), 0.0)
        NdotH = max(np.dot(N, H), 0.0)
        VdotH = max(np.dot(rView, H), 0.0)

        # Fresnel reflectance at normal incidence, typically for conductors like metals
        F0 = 0.04  # Default value, this could be parameterized based on the material

        # Fresnel term
        F = self.fresnel_schlick(VdotH, F0)

        # Normal distribution function
        D = self.normal_distribution_ggx(NdotH, hHinfo.roughness)

        # Geometry function
        G = self.geometry_smith(NdotV, NdotL, hHinfo.roughness)

        # Specular reflection
        spec_color = (F * D * G) / max(4 * NdotV * NdotL, 1e-5)

        # Diffuse reflection
        diff_color = self.cAlbedo / np.pi

        # Combine diffuse and specular terms
        return self.kd * diff_color + self.ks * spec_color
