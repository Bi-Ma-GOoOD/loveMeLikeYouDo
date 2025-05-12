import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren
import RT_material as rtm
import RT_scene as rts
import RT_object as rto
import RT_integrator as rti

def renderSphere():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 20
    main_camera.max_depth = 4
    main_camera.vertical_fov = 90
    main_camera.look_from = rtu.Vec3(0, 0, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)
    # add objects to the scene
    mat_yellow = rtm.Lambertian(rtu.Color(0.8, 0.8, 0.0))
    mat_red = rtm.Lambertian(rtu.Color(0.8, 0, 0.0))
    mat_blue = rtm.Lambertian(rtu.Color(0, 0, 0.8))

    world = rts.Scene()
    world.add_object(rto.Sphere(rtu.Vec3(   0,-100.5,-1),  100, mat_blue))
    world.add_object(rto.Sphere(rtu.Vec3(   0,   0.0,-1),  0.5, mat_yellow))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1),  0.5, mat_red))
    world.add_object(rto.Sphere(rtu.Vec3(-1.0,   0.0,-1), -0.4, mat_yellow))
    world.add_object(rto.Sphere(rtu.Vec3( 1.0,   0.0,-1),  0.5, mat_red))

    intg = rti.Integrator()

    renderer = rtren.Renderer(main_camera, intg, world)
    renderer.render()
    renderer.write_img2png("week04-sphere-001.png")


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
    renderer.write_img2png("week04-quad-001.png")
    

if __name__ == "__main__":
    #Render spheres using 'renderSphere()' function.
    renderSphere()
    #Render spheres using 'renderQuad()' function.
    renderQuad()


