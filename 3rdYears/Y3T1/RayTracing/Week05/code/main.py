import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl

def renderQuad():

    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 1.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 20
    main_camera.max_depth = 3
    main_camera.vertical_fov = 90
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    left_red = rtm.Lambertian(    rtu.Color(1.0, 0.2, 0.2))
    back_green = rtm.Lambertian(  rtu.Color(0.2, 1.0, 0.2))
    right_blue = rtm.Lambertian(  rtu.Color(0.2, 0.2, 1.0))
    upper_orange = rtm.Lambertian(rtu.Color(1.0, 0.5, 0.0))
    lower_teal = rtm.Lambertian(  rtu.Color(0.2, 0.8, 0.8))

    world = rts.Scene()
    world.add_object(rto.Quad(rtu.Vec3(-3,-2, 5), rtu.Vec3(0, 0,-4), rtu.Vec3(0, 4, 0), left_red))
    world.add_object(rto.Quad(rtu.Vec3(-2,-2, 0), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 4, 0), back_green))
    world.add_object(rto.Quad(rtu.Vec3( 3,-2, 1), rtu.Vec3(0, 0, 4), rtu.Vec3(0, 4, 0), right_blue))
    world.add_object(rto.Quad(rtu.Vec3(-2, 3, 1), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0, 4), upper_orange))
    world.add_object(rto.Quad(rtu.Vec3(-2,-3, 5), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0,-4), lower_teal))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png("week05_quad.png")
    
def renderQuadLight():

    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 1.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 10
    main_camera.max_depth = 8
    main_camera.vertical_fov = 90
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 0.0
    focus_distance = 3.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    left_red = rtm.Lambertian(    rtu.Color(1.0, 0.2, 0.2))
    back_green = rtm.Lambertian(  rtu.Color(0.2, 1.0, 0.2))
    right_blue = rtm.Lambertian(  rtu.Color(0.2, 0.2, 1.0))
    upper_orange = rtm.Lambertian(rtu.Color(1.0, 0.5, 0.0))
    lower_teal = rtm.Lambertian(  rtu.Color(0.2, 0.8, 0.8))

    right_light = rtl.Diffuse_light(rtu.Color(1.0, 1.0, 1.0))

    world = rts.Scene()
    world.add_object(rto.Quad(rtu.Vec3(-3,-2, 5), rtu.Vec3(0, 0,-4), rtu.Vec3(0, 4, 0), left_red))
    world.add_object(rto.Quad(rtu.Vec3(-2,-2, 0), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 4, 0), back_green))
    world.add_object(rto.Quad(rtu.Vec3( 3,-2, 1), rtu.Vec3(0, 0, 4), rtu.Vec3(0, 4, 0), right_light))
    world.add_object(rto.Quad(rtu.Vec3(-2, 3, 1), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0, 4), upper_orange))
    world.add_object(rto.Quad(rtu.Vec3(-2,-3, 5), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0,-4), lower_teal))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week05_quad_light1.png')    

def renderPointLight():

    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 1.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 5
    main_camera.max_depth = 4
    main_camera.vertical_fov = 90
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 0.0
    focus_distance = 3.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    left_red = rtm.Lambertian(    rtu.Color(1.0, 0.2, 0.2))
    back_green = rtm.Lambertian(  rtu.Color(0.2, 1.0, 0.2))
    right_blue = rtm.Lambertian(  rtu.Color(0.2, 0.2, 1.0))
    upper_orange = rtm.Lambertian(rtu.Color(1.0, 0.5, 0.0))
    lower_teal = rtm.Lambertian(  rtu.Color(0.2, 0.8, 0.8))
    """2. Add a point light source (white color [1.0,1.0,1.0]) at the location (0,0,0) and render it with the scene in 'renderPointLight()'."""
    point_light = rtl.Diffuse_light(rtu.Color(1.0, 1.0, 1.0))

    world = rts.Scene()
    """3. Keep quad patches on the left and the right (remove the rest). Keep the point light at the location (0,0,0). 
    it and compare the differences between results from (2.) and (3.)."""
    world.add_object(rto.Quad(rtu.Vec3(-3,-2, 5), rtu.Vec3(0, 0,-4), rtu.Vec3(0, 4, 0), left_red))
    world.add_object(rto.Quad(rtu.Vec3( 3,-2, 1), rtu.Vec3(0, 0, 4), rtu.Vec3(0, 4, 0), right_blue))
    """ remove the rest"""
    # world.add_object(rto.Quad(rtu.Vec3(-2,-2, 0), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 4, 0), back_green))
    # world.add_object(rto.Quad(rtu.Vec3(-2, 3, 1), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0, 4), upper_orange))
    # world.add_object(rto.Quad(rtu.Vec3(-2,-3, 5), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0,-4), lower_teal))
    """2. Add a point light source (white color [1.0,1.0,1.0]) at the location (0,0,0) and render it with the scene in 'renderPointLight()'."""
    world.add_object(rto.Sphere(rtu.Vec3(0, 0, 0), 0.1, point_light))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week05(3)_1-point_light.png')
    # Greenish-blue color สีเขียวอมน้ำเงิน    
    # renderer.write_img2png('what_is_teal_color.png')    

def renderPointLightShadow():

    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 1.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 10
    main_camera.max_depth = 4
    main_camera.vertical_fov = 90
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 0.0
    focus_distance = 3.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    left_red = rtm.Lambertian(    rtu.Color(1.0, 0.2, 0.2))
    back_green = rtm.Lambertian(  rtu.Color(0.2, 1.0, 0.2))
    right_blue = rtm.Lambertian(  rtu.Color(0.2, 0.2, 1.0))
    upper_orange = rtm.Lambertian(rtu.Color(1.0, 0.5, 0.0))
    lower_teal = rtm.Lambertian(  rtu.Color(0.2, 0.8, 0.8))
    
    """5. Add a render function called 'renderPointLightShadow()' by changing the location of the point light to (4,0,0). 
    Render the scene and explain the rendered result."""
    point_light = rtl.Diffuse_light(rtu.Color(1.0, 1.0, 1.0))

    world = rts.Scene()
    world.add_object(rto.Quad(rtu.Vec3(-3,-2, 5), rtu.Vec3(0, 0,-4), rtu.Vec3(0, 4, 0), left_red))
    world.add_object(rto.Quad(rtu.Vec3( 3,-2, 1), rtu.Vec3(0, 0, 4), rtu.Vec3(0, 4, 0), right_blue))
    world.add_object(rto.Quad(rtu.Vec3(-2,-2, 0), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 4, 0), back_green))
    world.add_object(rto.Quad(rtu.Vec3(-2, 3, 1), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0, 4), upper_orange))
    world.add_object(rto.Quad(rtu.Vec3(-2,-3, 5), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0,-4), lower_teal))

    """Location point light (4, 0, 0)."""
    world.add_object(rto.Sphere(rtu.Vec3(4, 0, 0), 0.1, point_light))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week05(5)_1-point_light.png')

"""6.Create a scene containing spheres and quads then light the scene up with a point light."""
def renderMyScene():

    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 1.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 3
    main_camera.vertical_fov = 90
    main_camera.look_from = rtu.Vec3(0, 0, 10)
    main_camera.look_at = rtu.Vec3(0, 0, 0)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle = 0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    #Adding Quads
    left_light_blue = rtm.Lambertian(rtu.Color(0.8, 0.9, 1.0))
    back_turquoise = rtm.Lambertian(rtu.Color(0.25, 0.85, 0.8))
    right_soft_pink = rtm.Lambertian(rtu.Color(1, 0.8, 0.9))
    upper_golden_yellow = rtm.Lambertian(rtu.Color(1.0, 0.85, 0.0))
    lower_Terracotta = rtm.Lambertian(rtu.Color(0.8, 0.4, 0.2))
    #Adding spheres
    sphere_sage_green = rtm.Lambertian(rtu.Color(0.7, 0.85, 0.6))
    sphere_lavender = rtm.Lambertian(rtu.Color(0.9, 0.8, 0.1))
    sphere_white = rtm.Lambertian(rtu.Color(1, 1, 1))
    #Adding lights
    right_point_light = rtl.Diffuse_light(rtu.Color(1, 1, 1))
    left_point_light = rtl.Diffuse_light(rtu.Color(0.5, 0.5, 0.5))

    world = rts.Scene()
    world.add_object(rto.Quad(rtu.Vec3(-3,-2, 5), rtu.Vec3(0, 0,-4), rtu.Vec3(0, 4, 0), left_light_blue))
    world.add_object(rto.Quad(rtu.Vec3(-2,-2, 0), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 4, 0), back_turquoise))
    world.add_object(rto.Quad(rtu.Vec3( 3,-2, 1), rtu.Vec3(0, 0, 4), rtu.Vec3(0, 4, 0), right_soft_pink))
    world.add_object(rto.Quad(rtu.Vec3(-2, 3, 1), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0, 4), upper_golden_yellow))
    world.add_object(rto.Quad(rtu.Vec3(-2,-3, 5), rtu.Vec3(4, 0, 0), rtu.Vec3(0, 0,-4), lower_Terracotta))

    world.add_object(rto.Sphere(rtu.Vec3(-1, 0.5, 0), 0.25, sphere_sage_green))
    world.add_object(rto.Sphere(rtu.Vec3(1, 0.5, 0), 0.25, sphere_lavender))
    world.add_object(rto.Sphere(rtu.Vec3(0, -1, 0), 1, sphere_white))

    world.add_object(rto.Sphere(rtu.Vec3(4, 0, 0), 0.2, right_point_light))
    world.add_object(rto.Sphere(rtu.Vec3(-4, 0, 0), 0.1, left_point_light))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png("week05(6)_myScene-v020.png")


if __name__ == "__main__":
    # renderQuad()
    # renderQuadLight()
    renderPointLight()
    # renderPointLightShadow()
    # renderMyScene()
