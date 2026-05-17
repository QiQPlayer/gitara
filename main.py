from cgitb import enable
from ursina import *
from ursina.color import rgba
from ursina.lights import DirectionalLight
import random

app = Ursina()
window.size = (2900, 1700)
Sky()

camera.rotation_x = 39
camera.rotation_y = 25
camera.y = 18
camera.x = -8
camera.z = -16
camera.fov = 70

light = DirectionalLight()
light.look_at(Vec3(2, -4, 1))

mi = Audio('mi.mp3', autoplay=False, volume=0.7)
do = Audio('do.mp3', autoplay=False, volume=0.7)
si = Audio('si.mp3', autoplay=False, volume=0.7)
sol = Audio('sol.mp3', autoplay=False, volume=0.7)
err = Audio('err.mp3', autoplay=False, volume=0.7)
su = Audio('su.mp3', autoplay=False, volume=3)

Begin = False
score = 50
popal = 0
speed = 5.25
speed_not = 0
high = 50
nota_color_r = [color.green, color.yellow, color.red, color.blue]
mode = 1
speed_a = 0.996
speed_low = 0.015
target = 0

gitara = Entity(
        model="cube",
        color=color.rgb32(203, 147, 70),
        position=(0, 0, 9),
        texture="Wood.png",
        scale=(12,5,70)
)
gitara.texture_scale = (2, 6)

gitara2 = Entity(
        model="Circle",
        color=color.rgb32(203, 147, 70),
        position=(0, 2.51, -15),
        texture="Wood.png",
        rotation_x=90,
        scale=(30,36)
)
gitara2.texture_scale = (10, 2)

gitara3 = Entity(
        model="Circle",
        color=color.black,
        position=(0, 2.52, -13),
        rotation_x=90,
        scale=(7,11)
)

lin1 = Entity(
        model="cube",
        color=color.rgba(0.85,0.85,0.85, 0.5),
        position=(1.5, 2.5, 5),
        scale=(0.3,0.3,80)
)
lin2 = Entity(
        model="cube",
        color=color.rgba(0.85,0.85,0.85, 0.5),
        position=(4.5, 2.5, 5),
        scale=(0.3,0.3,80)
)
lin3 = Entity(
        model="cube",
        color=color.rgba(0.85,0.85,0.85, 0.5),
        position=(-1.5, 2.5, 5),
        scale=(0.3,0.3,80)
)
lin4 = Entity(
        model="cube",
        color=color.rgba(0.85,0.85,0.85, 0.5),
        position=(-4.5, 2.5, 5),
        scale=(0.3,0.3,80)
)

gitara4 = Entity(
        model="cube",
        color=color.rgb(0.6,0.6,0.6),
        position=(0, 2.5, 8),
        scale=(11.99,0.25,0.2)
)
gitara5 = Entity(
        model="cube",
        color=color.rgb(0.6,0.6,0.6),
        position=(0, 2.5, 15),
        scale=(11.99,0.25,0.2)
)
gitara6 = Entity(
        model="cube",
        color=color.rgb(0.6,0.6,0.6),
        position=(0, 2.5, 22),
        scale=(11.99,0.25,0.2)
)
gitara7 = Entity(
        model="cube",
        color=color.rgb(0.6,0.6,0.6),
        position=(0, 2.5, 29),
        scale=(11.99,0.25,0.2)
)
gitara9 = Entity(
        model="cube",
        color=color.rgb(0.6,0.6,0.6),
        position=(0, 2.5, 36),
        scale=(11.99,0.25,0.2)
)

kop1 = Entity(
        model="cube",
        color=color.rgba(0.1, 0.1, 1, 0.5),
        position=(-4.5, 2.5, -5),
        scale=(2,1,2),
        collider="box"
)
kop2 = Entity(
        model="cube",
        color=color.rgba(0.1, 1, 0.1, 0.5),
        position=(-1.5, 2.5, -5),
        scale=(2,1,2),
        collider="box"
)
kop3 = Entity(
        model="cube",
        color=color.rgba(1, 0.1, 0.1, 0.5),
        position=(1.5, 2.5, -5),
        scale=(2,1,2),
        collider="box"
)
kop4 = Entity(
        model="cube",
        color=color.rgba(1, 1, 0.1, 0.5),
        position=(4.5, 2.5, -5),
        scale=(2,1,2),
        collider="box"
)

delet_note = Entity(
        model="cube",
        color=color.rgb(0.3,0.3,0.3),
        position=(0, 2.5, -17),
        collider="box",
        scale=(12, 5, 5)
)
delet_note_g = Entity(
        model="cube",
        color=color.rgba(0.3,0.3,0.3, 0.001),
        position=(0, 3.51, -12.49),
        collider="box",
        scale=(12, 1, 4)
)

Score = Text(
        text=f'score: {score}   ',
        position=(-0.85, 0.23),
        scale=2,
        color=color.white,
        background=True
)
speed_text = Text(
    text=f'speed: {0}  ',
    position=(-0.85, 0.4),
    scale=2,
    color=color.white,
    background=True
)
highscore = Text(
        text=f'high score: {high}   ',
        position=(-0.85, 0.05),
        scale=2,
        color=color.yellow,
        background=True,
)
Mode = Text(
        text=f'mode: normal',
        position=(-0.85, -0.125),
        scale=2,
        color=color.yellow,
        background=True,
)
game_over = Text(
    text='GAME OVER',
    origin=(-0.2, 0),
    scale=5,
    color=color.red,
    background=True,
    enabled=False
)

def select_easy():
    global Mode, kop1, kop2, kop3, kop4, mode, speed, speed_a, speed_low
    start_G.enabled = True
    Mode_easy.enabled = False
    Mode_normal.enabled = False
    Mode_hard.enabled = False
    Mode.text = "mode: easy"
    Mode.color = color.green
    kop1.scale = (2, 1, 3)
    kop2.scale = (2, 1, 3)
    kop3.scale = (2, 1, 3)
    kop4.scale = (2, 1, 3)
    mode = 0.5
    speed = 6
    speed_a = 0.998
    su.play()
    speed_low = 0.01

def select_normal():
    global Mode
    start_G.enabled = True
    Mode_easy.enabled = False
    Mode_normal.enabled = False
    Mode_hard.enabled = False
    Mode.text = "mode: normal"
    Mode.color = color.yellow
    su.play()

def select_hard():
    global Mode, kop1, kop2, kop3, kop4, mode, speed, speed_a, speed_low
    start_G.enabled = True
    Mode_easy.enabled = False
    Mode_normal.enabled = False
    Mode_hard.enabled = False
    Mode.text = "mode: hard"
    Mode.color = color.red
    kop1.scale = (2, 1, 1)
    kop2.scale = (2, 1, 1)
    kop3.scale = (2, 1, 1)
    kop4.scale = (2, 1, 1)
    mode = 2
    speed = 4.5
    speed_a = 0.994
    su.play()
    speed_low = 0.02

Mode_easy = Button(
    text='Easy',
    color=color.rgba32(34, 139, 34, 200),
    text_color=color.rgb32(0, 100, 0),
    scale=(0.5, 0.25),
    origin=(0, -1.25),
    enabled=True,
    text_size=2,
    on_click=select_easy
)
Mode_normal = Button(
    text='Normal',
    color=color.rgba32(139, 139, 34, 200),
    text_color=color.rgb32(100, 100, 0),
    scale=(0.5, 0.25),
    origin=(0, 0),
    enabled=True,
    text_size=2,
    on_click=select_normal
)
Mode_hard = Button(
    text='Hard',
    color=color.rgba32(139, 34, 34, 200),
    text_color=color.rgb32(100, 0, 0),
    scale=(0.5, 0.25),
    origin=(0, 1.25),
    enabled=True,
    text_size=2,
    on_click=select_hard
)

def spawn_nota(nota_color_r):
        global speed_not, speed, Begin
        if not Begin:
                return
        start_G.enabled = False
        nota_color = random.choice(nota_color_r)
        posi = 0
        if nota_color == color.blue:
                posi = -4.5
        elif nota_color == color.green:
                posi = -1.5
        elif nota_color == color.red:
                posi = 1.5
        elif nota_color == color.yellow:
                posi = 4.5
        nota = Entity(
                model="cube",
                color=nota_color,
                collider="box",
                position=(posi, 2.51, 40)
        )
        nota.animate_z(
                -25,
                duration=speed,
                curve=curve.linear,
                loop=False
        )
        speed_not += 1
        invoke(spawn_nota, nota_color_r, delay=(speed/4))

def start_game():
    global Begin
    Begin = True
    spawn_nota(nota_color_r)
    su.play()

start_G = Button(
    text='Start Game',
    color=color.rgba32(34, 139, 34, 200),
    text_color=color.rgb32(0, 100, 0),
    scale=(0.5, 0.25),
    origin=(0, 0),
    text_size=2,
    enabled=False,
    on_click=lambda: start_game()
)

def input(key):
        global target, Begin, popal, mode
        base_z = 3 if mode == 0.5 else (1 if mode == 2 else 2)
        pressed_z = base_z + 0.2
        pressed_z_f = base_z - 0.2
        if key == 'a':
                target = kop1.intersects()
                if target.hit:
                        kop1.color = color.rgba(0.1, 0.1, 1, 1)
                        kop1.animate_color(color.rgba(0.1, 0.1, 1, 0.5), duration=0.05, delay=0.1)
                        kop1.scale_z = pressed_z
                        kop1.animate_scale_z(base_z, duration=0.1, delay=0.1)
                        kop1.scale_y = 1.2
                        kop1.animate_scale_y(1, duration=0.1, delay=0.1)
                        kop1.scale_x = 2.2
                        kop1.animate_scale_x(2, duration=0.1, delay=0.1)
                        target.entity.animate_scale(0, duration=0.3, curve=curve.linear)
                        target.entity.animate_y(target.entity.y + 5, duration=0.3, curve=curve.linear)
                        target.entity.collider = None
                        destroy(target.entity, delay=0.3)
                        popal += 1
                        do.play()
                elif Begin:
                        kop1.color = color.rgba(0.5, 0.5, 0.5, 1)
                        kop1.animate_color(color.rgba(0.1, 0.1, 1, 0.5), duration=0.05, delay=0.1)
                        popal -= 1
                        err.play()
                        kop1.scale_z = pressed_z_f
                        kop1.animate_scale_z(base_z, duration=0.1, delay=0.1)
                        kop1.scale_y = 0.8
                        kop1.animate_scale_y(1, duration=0.1, delay=0.1)
                        kop1.scale_x = 1.8
                        kop1.animate_scale_x(2, duration=0.1, delay=0.1)
        elif key == 's':
                target = kop2.intersects()
                if target.hit:
                        kop2.color = color.rgba(0.1, 1, 0.1, 1)
                        kop2.animate_color(color.rgba(0.1, 1, 0.1, 0.5), duration=0.1, delay=0.1)
                        target.entity.animate_scale(0, duration=0.3, curve=curve.linear)
                        target.entity.animate_y(target.entity.y + 5, duration=0.3, curve=curve.linear)
                        destroy(target.entity, delay=0.3)
                        popal += 1
                        target.entity.collider = None
                        mi.play()
                        kop2.scale_z = pressed_z
                        kop2.animate_scale_z(base_z, duration=0.1, delay=0.1)
                        kop2.scale_y = 1.2
                        kop2.animate_scale_y(1, duration=0.1, delay=0.1)
                        kop2.scale_x = 2.2
                        kop2.animate_scale_x(2, duration=0.1, delay=0.1)
                elif Begin:
                        kop2.color = color.rgba(0.5, 0.5, 0.5, 1)
                        kop2.animate_color(color.rgba(0.1, 1, 0.1, 0.5), duration=0.1, delay=0.1)
                        popal -= 1
                        err.play()
                        kop2.scale_z = pressed_z_f
                        kop2.animate_scale_z(base_z, duration=0.1, delay=0.1)
                        kop2.scale_y = 0.8
                        kop2.animate_scale_y(1, duration=0.1, delay=0.1)
                        kop2.scale_x = 1.8
                        kop2.animate_scale_x(2, duration=0.1, delay=0.1)
        elif key == 'd':
                target = kop3.intersects()
                if target.hit:
                        kop3.color = color.rgba(1, 0.1, 0.1, 1)
                        kop3.animate_color(color.rgba(1, 0.1, 0.1, 0.5), duration=0.1, delay=0.1)
                        target.entity.animate_scale(0, duration=0.3, curve=curve.linear)
                        target.entity.animate_y(target.entity.y + 5, duration=0.3, curve=curve.linear)
                        destroy(target.entity, delay=0.3)
                        popal += 1
                        target.entity.collider = None
                        sol.play()
                        kop3.scale_z = pressed_z
                        kop3.animate_scale_z(base_z, duration=0.1, delay=0.1)
                        kop3.scale_y = 1.2
                        kop3.animate_scale_y(1, duration=0.1, delay=0.1)
                        kop3.scale_x = 2.2
                        kop3.animate_scale_x(2, duration=0.1, delay=0.1)
                elif Begin:
                        kop3.color = color.rgba(0.5, 0.5, 0.5, 1)
                        kop3.animate_color(color.rgba(1, 0.1, 0.1, 0.5), duration=0.1, delay=0.1)
                        popal -= 1
                        err.play()
                        kop3.scale_z = pressed_z_f
                        kop3.animate_scale_z(base_z, duration=0.1, delay=0.1)
                        kop3.scale_y = 0.8
                        kop3.animate_scale_y(1, duration=0.1, delay=0.1)
                        kop3.scale_x = 1.8
                        kop3.animate_scale_x(2, duration=0.1, delay=0.1)
        elif key == 'f':
                target = kop4.intersects()
                if target.hit:
                        kop4.color = color.rgba(1, 1, 0.1, 1)
                        kop4.animate_color(color.rgba(1, 1, 0.1, 0.5), duration=0.1, delay=0.1)
                        target.entity.animate_scale(0, duration=0.3, curve=curve.linear)
                        target.entity.animate_y(target.entity.y + 5, duration=0.3, curve=curve.linear)
                        destroy(target.entity, delay=0.3)
                        popal += 1
                        target.entity.collider = None
                        si.play()
                        kop4.scale_z = pressed_z
                        kop4.animate_scale_z(base_z, duration=0.1, delay=0.1)
                        kop4.scale_y = 1.2
                        kop4.animate_scale_y(1, duration=0.1, delay=0.1)
                        kop4.scale_x = 2.2
                        kop4.animate_scale_x(2, duration=0.1, delay=0.1)
                elif Begin:
                        kop4.color = color.rgba(0.5, 0.5, 0.5, 1)
                        kop4.animate_color(color.rgba(1, 1, 0.1, 0.5), duration=0.1, delay=0.1)
                        popal -= 1
                        err.play()
                        kop4.scale_z = pressed_z_f
                        kop4.animate_scale_z(base_z, duration=0.1, delay=0.1)
                        kop4.scale_y = 0.8
                        kop4.animate_scale_y(1, duration=0.1, delay=0.1)
                        kop4.scale_x = 1.8
                        kop4.animate_scale_x(2, duration=0.1, delay=0.1)

def update():
        global speed, speed_not, popal, score, Score, game_over, Begin, highscore, high, target, delet_note, mode, speed_a, speed_low, delet_note_g
        target = delet_note.intersects()
        if target.hit:
            destroy(target.entity)
            target.entity.collider = None
            popal -= 1
            speed = speed + speed_low
        if speed_not == 1:
                speed = speed * speed_a
                speed_not = 0
        if popal > 1 or popal < -1:
            popal = 0
        if popal == 1:
                popal = 0
                score += 10
                Score.text = f'score: {int(score)}'
                if high < score:
                        high = int(score)
                        highscore.text = f'high score: {high}'
        elif popal == -1:
                popal = 0
                score -= 10 * mode
                Score.text = f'score: {int(score)}'
                if high < score:
                        high = int(score)
                        highscore.text = f'high score: {high}'
        target_G = delet_note_g.intersects()
        if score < 0:
            score = 0
        if score == 0 and Begin:
                game_over.enabled = True
                Begin = False
                delet_note_g.animate_z(60, duration=0.5, curve=curve.linear,loop=False)

        if game_over.enabled and target_G.hit:
                    destroy(target_G.entity)
                    target_G.entity.collider = None
        speed_text.text = f'speed: {int(600 - ((speed * 100)//1))}'

app.run()
