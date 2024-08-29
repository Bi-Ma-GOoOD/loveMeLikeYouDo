import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti
import RT_light as rtl
import RT_texture as rtt

def renderPhong():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))
    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)
    """1.2 Render a scene with 3 balls in the scene. Each ball exhibits a Phong material with roughness parameters = 0.8, 8 and 30."""
    mat_phong1 = rtm.Phong(rtu.Color(0.77, 1.0, 0.58), 0.25, 1.0, 0.8)      # green
    mat_phong2 = rtm.Phong(rtu.Color(0.63, 0.87, 1.0), 0.25, 1.0, 8)        # blue
    mat_phong3 = rtm.Phong(rtu.Color(1.0, 0.4, 0.0), 0.25, 1.0, 30)        # orange

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_phong1))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_phong2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_phong3))    # right

    dlight = rtl.Diffuse_light(rtu.Color(0.9, 0.9, 0.9))
    world.add_object(rto.Sphere(rtu.Vec3(   0, 1.0, 0.0), 0.05, dlight))
    # world.add_object(rto.Quad(rtu.Vec3(-0.5,1.5,-0.5), rtu.Vec3(0,0,-7.5), rtu.Vec3(3,0,-0.5), dlight))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week08(1)_brdf_Phong-v005.png')    

def renderBlinn():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)
    """2.2 Render a scene with 3 balls in the scene. Each ball exhibits a Phong material with roughness parameters = 0.8, 8 and 30."""
    mat_blinn1 = rtm.Blinn(rtu.Color(0.77, 1.0, 0.58), 0.25, 1.0, 0.08)      # green
    mat_blinn2 = rtm.Blinn(rtu.Color(0.63, 0.87, 1.0), 0.25, 1.0, 8)        # blue
    mat_blinn3 = rtm.Blinn(rtu.Color(1.0, 0.4, 0.0), 0.25, 1.0, 300)        # orange


    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_blinn1))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_blinn2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_blinn3))    # right

    dlight = rtl.Diffuse_light(rtu.Color(0.9, 0.9, 0.9))
    world.add_object(rto.Sphere(rtu.Vec3(   0, 1.0, 0.0), 0.05, dlight))
    # world.add_object(rto.Quad(rtu.Vec3(-0.5,1.5,-0.5), rtu.Vec3(0,0,-7.5), rtu.Vec3(3,0,-0.5), dlight))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week08(2)_brdf_Blinn-v006.png')    


def renderLetMeCook():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 200
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)
    """3.2 Reuse the above scene for this problem."""
    mat_blinn1 = rtm.CookTorrance(rtu.Color(0.77, 1.0, 0.58), 0.25, 1.0, 0.08, 0.0)      # green
    mat_blinn2 = rtm.CookTorrance(rtu.Color(0.63, 0.87, 1.0), 0.25, 1.0, 8, 0.0)        # blue
    mat_blinn3 = rtm.CookTorrance(rtu.Color(1.0, 0.4, 0.0), 0.25, 1.0, 300, 0.0)        # orange


    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_blinn1))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_blinn2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_blinn3))    # right

    dlight = rtl.Diffuse_light(rtu.Color(0.9, 0.9, 0.9))
    world.add_object(rto.Sphere(rtu.Vec3(   0, 1.0, 0.0), 0.05, dlight))
    # world.add_object(rto.Quad(rtu.Vec3(-0.5,1.5,-0.5), rtu.Vec3(0,0,-7.5), rtu.Vec3(3,0,-0.5), dlight))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week08(3)_let_me_cook-v024.png')    

def renderLetMeCookV2():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 480
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 100
    main_camera.max_depth = 5
    main_camera.vertical_fov = 60
    main_camera.look_from = rtu.Vec3(-2, 2, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene

    tex_checker_bw = rtt.CheckerTexture(0.32, rtu.Color(.2, .2, .2), rtu.Color(.9, .9, .9))

    mat_tex_checker_bw = rtm.TextureColor(tex_checker_bw)
    """3.2 Reuse the above scene for this problem."""
    mat_blinn1 = rtm.CookTorrance(rtu.Color(0.77, 1.0, 0.58), 0.25, 1.0, 0.08, 1.0)      # green
    mat_blinn2 = rtm.CookTorrance(rtu.Color(0.63, 0.87, 1.0), 0.25, 1.0, 8, 1.0)        # blue
    mat_blinn3 = rtm.CookTorrance(rtu.Color(1.0, 0.4, 0.0), 0.25, 1.0, 300, 1.0)        # orange


    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_tex_checker_bw))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_blinn1))    # left
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_blinn2))    # center
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_blinn3))    # right

    dlight = rtl.Diffuse_light(rtu.Color(0.9, 0.9, 0.9))
    world.add_object(rto.Sphere(rtu.Vec3(   0, 1.0, 0.0), 0.05, dlight))
    # world.add_object(rto.Quad(rtu.Vec3(-0.5,1.5,-0.5), rtu.Vec3(0,0,-7.5), rtu.Vec3(3,0,-0.5), dlight))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png('week08(3)_let_me_cook(2)-v002.png')    

if __name__ == "__main__":
    # renderPhong()
    # renderBlinn()
    renderLetMeCook()
    # renderLetMeCookV2()