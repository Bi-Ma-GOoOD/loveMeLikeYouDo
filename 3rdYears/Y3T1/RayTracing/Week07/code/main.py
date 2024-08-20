import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl
import RT_texture as rtt

"""2. Complete the 'renderProceduralTexture()' in main.py by creating textuers and use them accordingly. 
The scene is lit up by the sky as a background. Submit the rendered result as 'week07_texture_sky.png'."""
def renderProceduralTexture():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 130
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    mat_center = rtm.Lambertian(rtu.Color(0.7, 0.3, 0.3))
    checker_bw = rtt.CheckerTexture(0.56, rtu.Color(0.0, 0.0, 0.0), rtu.Color(1.0, 1.0, 1.0))
    checker_color = rtt.CheckerTexture(0.24, rtu.Color(0.95, 0.79, 0.32), rtu.Color(0.5, 1.0, 0.5))
    # สีส้ม
    solid_color = rtt.SolidColor(rtu.Color(1.0, 0.5, 0.2))

    # create textures
    mat_tex_checker_bw = rtm.TextureColor(checker_bw)           # black and white checker board
    mat_tex_checker = rtm.TextureColor(checker_color)           # colorful checker board
    mat_tex_solid = rtm.TextureColor(solid_color)               # solid color

    world = rts.Scene()
    # ลูกรองพื้น
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    # ลูกหน้าสุด
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_tex_checker))
    # ลูกตรงกลาง
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_center))
    # ลูกหลังสุดสีส้ม
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_tex_solid))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week07(2)_texture_sky-v010.png')    

def renderEarth():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 130
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene
    """3. Complete the 'renderEarth()' in main.py by creating textures, loaded up from files, and use them accordingly. 
    The scene is lit up by the sky as a background. Submit the rendered result as 'week07_texture_earth_sky.png'."""
    # checker_bw = rtt.CheckerTexture(0.24, rtu.Color(0.0, 0.0, 0.0), rtu.Color(1.0, 1.0, 1.0))
    # earth_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week07\\texture\\earthmap.jpg')
    # basketball_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week07\\texture\\basketball.jpg')
    # soccer_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week07\\texture\\soccer.jpg')
    # pepsi_texture = rtt.ImageTexture('3rdYears\\Y3T1\\RayTracing\\Week07\\texture\\pepsi.jpg')

    # mat_tex_checker_bw = rtm.TextureColor(checker_bw)               # black and white checker board
    # mat_tex_earth = rtm.TextureColor(earth_texture)                 # earth texture
    # mat_tex_basketball = rtm.TextureColor(basketball_texture)       # basketball
    # mat_tex_soccer = rtm.TextureColor(soccer_texture)               # soccer
    # mat_tex_pepsi = rtm.TextureColor(pepsi_texture)                 # pepsi logo

    # world = rts.Scene()
    # world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_earth))
    # world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_tex_checker_bw))
    # world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_tex_basketball))
    # world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_tex_soccer))

    # world.add_object(rto.Quad(rtu.Vec3(1.0, 0.0, -1), rtu.Vec3(1.0, 2.0, -1), rtu.Vec3(1.0, 0.0, 1), mat_tex_pepsi))

    """5. Submit the rendered result from (3.). by setting up a scene with 6 matal balls."""
    """5.1 Roughness paramters = 0.0001, 0.0005, 0.05, 0.1, 0.8, 1.0"""
    # # Add objects to the scene
    mat_metal_ball1 = rtm.Metal(rtu.Color(0.027, 0.25, 0.45), 0.0001)       # navy blue
    mat_metal_ball2 = rtm.Metal(rtu.Color(0.77, 1.0, 0.58), 0.0005)         # green
    mat_metal_ball3 = rtm.Metal(rtu.Color(0.77, 0.05, 0.05), 0.05)          # Red
    mat_metal_ball4 = rtm.Metal(rtu.Color(1.0, 0.76, 0.0), 0.1)             # yellow
    mat_metal_ball5 = rtm.Metal(rtu.Color(1.0, 0.98, 0.82), 0.8)            # weak yellow
    mat_metal_ball6 = rtm.Metal(rtu.Color(0.79, 0.96, 1.0), 1.0)            # weak blue
    mat_ground = rtm.Lambertian(rtu.Color(0.85, 0.85, 0.85))

    """5.2 Use a quad(area) light source above all of the balls."""
    # Add light to the scene
    above_light = rtl.Diffuse_light(rtu.Color(1.0, 1.0, 1.0))

    world = rts.Scene()
    
    """Add metal balls from 5.1"""
    # พื้น
    world.add_object(rto.Sphere(rtu.Vec3( 0.0,-100.5, -1),  100, mat_ground))
    # ลูกซ้ายบน
    world.add_object(rto.Sphere(rtu.Vec3( 1.3,   0.0, -1.9),  0.6, mat_metal_ball1))
    # ลูกกลางบน
    world.add_object(rto.Sphere(rtu.Vec3( 0.8,   -0.3, -0.9),  0.3, mat_metal_ball2))
    # ลูกขวาบน
    world.add_object(rto.Sphere(rtu.Vec3( 1.5,   0.0, 0.2),  0.5, mat_metal_ball3))
    # ลูกซ้ายล่าง
    world.add_object(rto.Sphere(rtu.Vec3(-1.3,   0.0,-2.8),  0.5, mat_metal_ball5))
    # ลูกกลางล่าง
    world.add_object(rto.Sphere(rtu.Vec3( -0.5,   0.0,-1.5),  0.5, mat_metal_ball6))
    # ลูกขวาล่าง
    world.add_object(rto.Sphere(rtu.Vec3( -0.9,   0.0, -0.1),  0.5, mat_metal_ball4))
    """Add squad(area) light above metal balls from 5.2 """
    world.add_object(rto.Quad(rtu.Vec3(4, 4, -4), rtu.Vec3(0, 0, 4), rtu.Vec3(-4, 0, 0), above_light))


    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    # renderer.write_img2png('week07(3)_texture_earth_sky-v006.png')    
    renderer.write_img2png('week07(5)_metal_balls-v029.png')    


if __name__ == "__main__":
    # renderProceduralTexture()
    renderEarth()


