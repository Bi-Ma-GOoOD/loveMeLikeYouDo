import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl
import RT_texture as rtt  

def renderGalaxy():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 3840
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 10
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 2.0
    focus_distance = 5.0
    aperture = 16
    main_camera.init_camera(defocus_angle, focus_distance, aperture)
    # # Add objects to the scene
    mat_ground = rtm.Lambertian(rtu.Color(0.85, 0.85, 0.85))
    sun_color = rtm.Lambertian(rtu.Color(1.00, 0.541, 0.031))               # orange -> sun
    mercury_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\Week11\\final-proj-texture\\2k_mercury.jpg')
    venus_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\Week11\\final-proj-texture\\2k_venus_atmosphere.jpg')
    earth_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week11\\final-proj-texture\\2k_earth_daymap.jpg')
    mars_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week11\\final-proj-texture\\2k_mars.jpg')
    jupiter_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week11\\final-proj-texture\\2k_jupiter.jpg')
    saturn_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week11\\final-proj-texture\\2k_saturn.jpg')
    uranus_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week11\\final-proj-texture\\2k_uranus.jpg')
    nepturn_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week11\\final-proj-texture\\2k_neptune.jpg')

    # Main light (Sun)
    sun_light = rtl.Diffuse_light(rtu.Color(0.98, 0.82, 0.53))
    # Minor light (0.85)
    above_light = rtl.Diffuse_light(rtu.Color(1.0, 1.0, 1.0))
    # < - - - - - >
    mercury = rtm.TextureColor(mercury_texture)
    venus = rtm.TextureColor(venus_texture)
    earth = rtm.TextureColor(earth_texture)
    mars = rtm.TextureColor(mars_texture)
    jupiter = rtm.TextureColor(jupiter_texture)
    saturn = rtm.TextureColor(saturn_texture)
    uranus = rtm.TextureColor(uranus_texture)
    nepturn = rtm.TextureColor(nepturn_texture)
    # Add planet
    world = rts.Scene()
     # พื้น
    # world.add_object(rto.Sphere(rtu.Vec3( 0.0,-100.5, -1),  100, mat_ground))
    # ดวงอาทิตย์
    # world.add_object(rto.Sphere(rtu.Vec3( 1.3, 0.6, -2.8),  1.3, sun_color))
    world.add_object(rto.Sphere(rtu.Vec3( 1.3, 0.6, -2.8),  1.3, sun_light))
    # ดาวพุธ ขนาด 0.15
    world.add_object(rto.Sphere(rtu.Vec3( 0.99, 0.0, -0.9),  0.15, mercury))
    # ดาวศุกร์
    world.add_object(rto.Sphere(rtu.Vec3( 3.0, 0.0, -1.0),  0.3, venus))
    # ดาวโลก
    world.add_object(rto.Sphere(rtu.Vec3( 1.9, 0.0, 0.4),  0.45, earth))
    # ดาวอังคาร
    world.add_object(rto.Sphere(rtu.Vec3( 1.25, 0.0, 1.2),  0.35, mars))
    # ดาวพฤหัส
    world.add_object(rto.Sphere(rtu.Vec3( -1.2, 0.0, -3.5),  0.75, jupiter))
    # ดาวเสาร์
    world.add_object(rto.Sphere(rtu.Vec3( -1.85, 0.0, -0.68),  0.65, saturn))
    # ดาวยูเรนัส
    world.add_object(rto.Sphere(rtu.Vec3( 0.0, 0.0, 0.0),  0.45, uranus))
    # ดาวเนปจูน
    world.add_object(rto.Sphere(rtu.Vec3( -0.4, 0.0, -1.35),  0.35, nepturn))

    
    """Add squad(area) light """
    world.add_object(rto.Quad(rtu.Vec3(4, 1.95, -4), rtu.Vec3(0, 0, 4), rtu.Vec3(-4, 0, 0), above_light))


    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render_jittered()
    renderer.write_img2png('test-img01-v112.png')   

def renderToonShading():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 3840
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 10
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 2.0
    focus_distance = 5.0
    aperture = 4.0
    main_camera.init_camera(defocus_angle, focus_distance, aperture)
    # Initialize object 
    tex_checker_color = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))
    mat_tex_checker_color = rtm.TextureColor(tex_checker_color)
    """ Use Toon shading -> Shade Toon + Phong lighting"""
    mat_phong1 = rtm.ToonPhong(rtu.Color(0.02, 0.82, 0.01), 0.25, 1.0, 0.8, 4, 0.6) # Green
    mat_phong2 = rtm.ToonPhong(rtu.Color(0.95, 0.10, 0.42), 0.25, 1.0, 0.8, 4, 0.6) # Violet
    mat_phong3 = rtm.ToonPhong(rtu.Color(0.62, 0.87, 1.00), 0.25, 1.0, 0.8, 4, 0.6) # Blue
    """ Use Dielectric material"""
    mat_dielectric = rtm.Dielectric(rtu.Color(1.00, 0.89, 0.10), 0.1)
    """ Use Metal"""
    mat_metal = rtm.Metal(rtu.Color(0.47, 0.33, 0.35), 0.65)
    light = rtl.Diffuse_light(rtu.Color(0.35, 0.35, 0.35))

    # Add objects to the scene
    world = rts.Scene()
    # floor
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_color))
    # object
    world.add_object(rto.Sphere(rtu.Vec3(0.0, 0.0, -3.0),  0.5, mat_phong1)) # top - left
    world.add_object(rto.Sphere(rtu.Vec3(0.0, 0.0, -1.35),  0.5, mat_phong2)) # center
    world.add_object(rto.Sphere(rtu.Vec3(0.0, 0.0, 0.0),  0.5, mat_phong3)) # low - right
    world.add_object(rto.Sphere(rtu.Vec3(2.7, 0.0, -0.3),  0.5, mat_dielectric)) # top - right
    world.add_object(rto.Sphere(rtu.Vec3(-2.0 , 0.0, -2.0), 0.5, mat_metal)) # low - left
    # light
    world.add_object(rto.Sphere(rtu.Vec3(   0.0, 5.0, 0.0),  0.05, light))
    
    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render_jittered()
    renderer.write_img2png('test-img02-v040.png')


if __name__ == "__main__":
    # renderGalaxy()
    renderToonShading()

