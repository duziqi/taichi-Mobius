from scene import Scene
import taichi as ti
from taichi.math import *

scene = Scene(exposure=1)
scene.set_directional_light((1, 0.5, 1), 0.1, (1, 1, 1))
scene.set_floor(-0.7, (0.6, 0.8, 1.0))
scene.set_background_color((0.3, 0.4, 0.6))


@ti.kernel
def inifunc():
    circle(30)
    circle(33)
    circle(36)
    circle(39)
    circle(42)


@ti.func
def circle(size):
    t = -0.5
    r = ti.random()
    g = ti.random()
    while t <= 0.5:
        f = 0.0
        while f <= 2 * pi:
            x = (1 + t * ti.cos(f / 2)) * ti.cos(f) * size
            y = t * ti.sin(f / 2) * size
            z = (1 + t * ti.cos(f / 2)) * ti.sin(f) * size
            scene.set_voxel(vec3(x, y, z), 1, vec3(r, g * ti.random(), ti.random()))
            f += pi / 256
        t += 0.001


inifunc()

scene.finish()
