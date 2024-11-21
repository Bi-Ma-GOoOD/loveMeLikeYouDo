import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl

def renderMirrorPointLight():

    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 5
    main_camera.vertical_fov = 30
    # main_camera.look_from = rtu.Vec3(-2, 2, 1)
    # main_camera.look_at = rtu.Vec3(0, 0, -1)
    # main_camera.vec_up = rtu.Vec3(0, 1, 0)
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)
    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))
    mat_glass1 = rtm.Mirror(rtu.Color(0.8, 0.8, 0.8))
    """3. Render a scene with at least 2 mirrors and a point light."""
    mat_glass2 = rtm.Mirror(rtu.Color(0.5, 0.6, 0.7))

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_ground))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1), -0.4, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3(-0.8,   0.0,1),  0.2, mat_glass2))
    world.add_object(rto.Sphere(rtu.Vec3( 0, 0.0,2), -0.2, mat_glass2))
    world.add_object(rto.Sphere(rtu.Vec3( 0.65,   0.0,3),  0.1, mat_glass2))
    """4. Render a scene with at least 2 mirrors and the sky background (no point light)."""
    # point_light = rtl.Diffuse_light(rtu.Color(1.0, 1.0, 1.0))
    # world.add_object(rto.Sphere(rtu.Vec3(0, 2.5, 0), 0.1, point_light))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    # """3. Render a scene with at least 2 mirrors and a point light."""
    # renderer.write_img2png('week06(3)-with-one-pointLight.png')   
    """4. Render a scene with at least 2 mirrors and the sky background (no point light).""" 
    renderer.write_img2png('week06(4)-with-sky-background-and-no-pointlight.png')   


def renderMirrors():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 20
    main_camera.max_depth = 7
    main_camera.vertical_fov = 50
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))
    mat_glass1 = rtm.Mirror(rtu.Color(0.8, 0.8, 0.8))

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_ground))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1), -0.4, mat_glass1))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_glass1))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week06_glass_sky.png')    

"""6. Render a scene with at least 2 transparent materials and the sky background."""
def renderDielectric():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 5
    main_camera.vertical_fov = 50
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_ground = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))
    mat_glass1 = rtm.Mirror(rtu.Color(0.8, 0.8, 0.8))
    mat_dielect1 = rtm.Dielectric(rtu.Color(1.0, 1.0, 1.0), 1.5)
    mat_dielect2 = rtm.Dielectric(rtu.Color(0.2, 0.3, 0.4), 2.0)
    mat_dielect3 = rtm.Dielectric(rtu.Color(0.25, 0.6, 0.0), 2.5)

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_ground))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    # ลูกทางซ้าย
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_glass1))
    # ลูกทางขวา
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_dielect1))
    # world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1), -0.4, mat_glass1))
    # ลูกหลังบน สีน้ำเงินอมดำ
    world.add_object(rto.Sphere(rtu.Vec3( 0.6,   0.0,-2.5),  0.5, mat_dielect2))
    # ลูกหน้าล่าง สีเขียว
    world.add_object(rto.Sphere(rtu.Vec3(0.6, 0.0, 0.25), 0.3, mat_dielect3))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week06(6)_dielec_sky.png')

""" Render a scene with the following materials and the sky background.a mirror"""
def renderMyScene():
    # Camera
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 110
    main_camera.max_depth = 6
    main_camera.vertical_fov = 50
    main_camera.look_from = rtu.Vec3(0, 2, 8.5)
    main_camera.look_at = rtu.Vec3(0, -0.6, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # Adding Dielectric Material
    """ dielectric material with index of refraction = 1.5 """
    mat_dielect1 = rtm.Dielectric(rtu.Color(1.0, 0.8, 0.8), 1.5)
    """ dielectric material with index of refraction = 1.0 """       
    mat_dielect2 = rtm.Dielectric(rtu.Color(0.8, 1.0, 0.8), 1.0)    
    """ dielectric material with index of refraction = 0.5 """   
    mat_dielect3 = rtm.Dielectric(rtu.Color(0.8, 0.8, 1), 0.5)  
    # Adding Lambertian Material
    """ lambertian material """
    mat_sphere = rtm.Lambertian(rtu.Color(0.773, 1.0, 0.584))
    mat_ground = rtm.Lambertian(rtu.Color(0.027, 0.255, 0.451))
    # Adding Mirror Material
    """ mirror """
    mat_quad_glass = rtm.Mirror(rtu.Color(0.3, 0.3, 0.3))

    world = rts.Scene()
    # Ground
    world.add_object(rto.Sphere(rtu.Vec3(0, -100.5, -1), 100, mat_ground))
    # Mirror
    world.add_object(rto.Quad(rtu.Vec3(-4, -4, 0), rtu.Vec3(8, 0, 0), rtu.Vec3(0, 8, 0), mat_quad_glass))
    # Lambertian
    world.add_object(rto.Sphere(rtu.Vec3(0.4, 0, 3), 0.7, mat_sphere))
    # Dielectric
    world.add_object(rto.Sphere(rtu.Vec3(-1.6, 0, 3), 0.9, mat_dielect1))
    world.add_object(rto.Sphere(rtu.Vec3(1.9, 0, 3), 0.5, mat_dielect2))
    world.add_object(rto.Sphere(rtu.Vec3(0.38, 0, 5.5), 0.3, mat_dielect3))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week06(7)_my_scene-v034.png')
         

if __name__ == "__main__":
    # renderMirrors()
    # renderMirrorPointLight()
    renderDielectric()
    renderMyScene()

