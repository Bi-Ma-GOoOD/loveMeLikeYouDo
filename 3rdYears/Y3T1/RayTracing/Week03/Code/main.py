import RT_utility as rtu
import RT_camera as rtc
import RT_renderer as rtren

def render():
    main_camera = rtc.Camera()
    main_camera.aspect_ratio = 16.0/9.0
    main_camera.img_width = 400
    main_camera.center = rtu.Vec3(0,0,0)
    main_camera.samples_per_pixel = 50
    main_camera.max_depth = 7
    main_camera.vertical_fov = 90
    main_camera.look_from = rtu.Vec3(0, 0, 1)
    main_camera.look_at = rtu.Vec3(0, 0, -1)
    main_camera.vec_up = rtu.Vec3(0, 1, 0)

    defocus_angle =0.0
    focus_distance = 10.0
    main_camera.init_camera(defocus_angle, focus_distance)

    renderer = rtren.Renderer(main_camera)
    renderer.render()
    renderer.write_img2png("week03-1-2.png")


if __name__ == "__main__":
    render()


