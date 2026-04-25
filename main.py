from setuptools.command.rotate import rotate
from ursina import *
from ursina.color import rgba
from ursina.lights import DirectionalLight

app = Ursina()
window.size = (1540, 900)
Sky()

camera.rotation_x = 42
camera.rotation_y = 25
camera.y = 18
camera.x = -8
camera.z = -16
camera.fov = 70
light = DirectionalLight()
light.look_at(Vec3(2, -4, 1))



gitara = Entity(
        model="cube",
        color=color.rgb32(203, 147, 70),
        position=(0, 0, 9),
        texture="Wood.png",
        scale=(12,5,50)
)
gitara.texture_scale = (2, 6)
gitara2 = Entity(
        model="Circle",
        color=color.rgb32(203, 147, 70),
        position=(0, 2.501, -8),
        texture="Wood.png",
        rotation_x=90,
        scale=(22,26)
)
gitara2.texture_scale = (10, 2)

gitara3 = Entity(
        model=Cylinder(resolution=40, radius=3, height=5),
        color=color.black,
        position=(0, -2.498, -8),
)
centr = Entity(
        model="cube",
        color=color.gray,
        position=(0, 3, 0),
        texture="grass",
)

def input(key):
    pass
def update():
    camera.x += held_keys["d"] * time.dt * 5
    camera.x -= held_keys["a"] * time.dt * 5
    camera.z += held_keys["w"] * time.dt * 5
    camera.z -= held_keys["s"] * time.dt * 5
    camera.y += held_keys["e"] * time.dt * 5
    camera.y -= held_keys["q"] * time.dt * 5
app.run()