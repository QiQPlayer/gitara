from ursina import *
from ursina.color import rgba
from ursina.lights import DirectionalLight
import random

app = Ursina()
window.size = (2900, 1700)
#1540, 900 - laptop
#2900, 1700 - pc
Sky()

camera.rotation_x = 39
camera.rotation_y = 25
camera.y = 18
camera.x = -8
camera.z = -16
camera.fov = 70
light = DirectionalLight()
light.look_at(Vec3(2, -4, 1))
Begin = False

score = 50
popal = 0
speed = 6
speed_not = 0
high = 50
nota_color_r = [color.green, color.yellow, color.red, color.blue]

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
        color=color.rgb(0.85,0.85,0.85, 0.5),
        position=(1.5, 2.5, 5),
        scale=(0.3,0.3,80)
)
lin2 = Entity(
        model="cube",
        color=color.rgb(0.85,0.85,0.85, 0.5),
        position=(4.5, 2.5, 5),
        scale=(0.3,0.3,80)
)
lin3 = Entity(
        model="cube",
        color=color.rgb(0.85,0.85,0.85, 0.5),
        position=(-1.5, 2.5, 5),
        scale=(0.3,0.3,80)
)
lin4 = Entity(
        model="cube",
        color=color.rgb(0.85,0.85,0.85, 0.5),
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
        color=color.rgb(0.1, 0.1, 1, 0.5),
        position=(-4.5, 2.5, -5),
        scale=(2,1,2),
        collider="box"
)
kop2 = Entity(
        model="cube",
        color=color.rgb(0.1, 1, 0.1, 0.5),
        position=(-1.5, 2.5, -5),
        scale=(2,1,2),
        collider="box"
)
kop3 = Entity(
        model="cube",
        color=color.rgb(1, 0.1, 0.1, 0.5),
        position=(1.5, 2.5, -5),
        scale=(2,1,2),
        collider="box"
)
kop4 = Entity(
        model="cube",
        color=color.rgb(1, 1, 0.1, 0.5),
        position=(4.5, 2.5, -5),
        scale=(2,1,2),
        collider="box"
)
Score = Text(
        text=f'score: {score}',
        position=(-0.85, 0.23),
        scale=2,
        color=color.white,
        background=True
)
def spawn_nota(nota_color_r):
        global speed_not, speed, Begin
        if not Begin:
                return
        start.enabled = False
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
                position=(posi, 2.5, 40)
        )
        nota.animate_z(
                -25,
                duration=speed,
                curve=curve.linear,
                loop=False
        )
        speed_not += 1
        invoke(spawn_nota, nota_color_r, delay=(speed/4))
        destroy(nota, delay=speed)
def start_game():
    global Begin
    Begin = True
    spawn_nota(nota_color_r)
start = Button(
    text='Start Game',
    color=color.rgb32(34, 139, 34, 200),
    text_color=color.rgb32(0, 100, 0),
    scale=(0.5, 0.25),
    origin=(0, 0),
    text_size=2,
    on_click=lambda: start_game()
                      )
speed_text = Text(
    text=f'speed: {0}',
    position=(-0.85, 0.4),
    scale=2,
    color=color.white,
    background=True
)
game_over = Text(
    text='GAME OVER',
    origin=(-0.2, 0),
    scale=5,
    color=color.red,
    background=True,
    enabled=False
)
highscore = Text(
        text=f'high score: {high}',
        position=(-0.85, 0.05),
        scale=2,
        color=color.yellow,
        background=True,
)
target = 0
def input(key):
        global target, Begin, popal
        if key == 'a':
                target = kop1.intersects()
                if target.hit:
                        kop1.color = color.rgb(0.1, 0.1, 1, 1)
                        kop1.animate_color(color.rgb(0.1, 0.1, 1, 0.5), duration=0.05, delay=0.1)
                        target.entity.animate_scale(0, duration=0.2, curve=curve.linear)
                        destroy(target.entity, delay=0.2)
                        popal += 1
                        target.entity.collider = None
                elif Begin:
                        kop1.color = color.rgb(0.5, 0.5, 0.5, 1)
                        kop1.animate_color(color.rgb(0.1, 0.1, 1, 0.5), duration=0.05, delay=0.1)
                        popal -= 1
        elif key == 's':
                target = kop2.intersects()
                if target.hit:
                        kop2.color = color.rgb(0.1, 1, 0.1, 1)
                        kop2.animate_color(color.rgb(0.1, 1, 0.1, 0.5), duration=0.1, delay=0.1)
                        target.entity.animate_scale(0, duration=0.2, curve=curve.linear)
                        destroy(target.entity, delay=0.2)
                        popal += 1
                        target.entity.collider = None
                elif Begin:
                        kop2.color = color.rgb(0.5, 0.5, 0.5, 1)
                        kop2.animate_color(color.rgb(0.1, 1, 0.1, 0.5), duration=0.1, delay=0.1)
                        popal -= 1
        elif key == 'd':
                target = kop3.intersects()
                if target.hit:
                        kop3.color = color.rgb(1, 0.1, 0.1, 1)
                        kop3.animate_color(color.rgb(1, 0.1, 0.1, 0.5), duration=0.1, delay=0.1)
                        target.entity.animate_scale(0, duration=0.2, curve=curve.linear)
                        destroy(target.entity, delay=0.2)
                        popal += 1
                        target.entity.collider = None
                elif Begin:
                        kop3.color = color.rgb(0.5, 0.5, 0.5, 1)
                        kop3.animate_color(color.rgb(1, 0.1, 0.1, 0.5), duration=0.1, delay=0.1)
                        popal -= 1
        elif key == 'f':
                target = kop4.intersects()
                if target.hit:
                        kop4.color = color.rgb(1, 1, 0.1, 1)
                        kop4.animate_color(color.rgb(1, 1, 0.1, 0.5), duration=0.1, delay=0.1)
                        target.entity.animate_scale(0, duration=0.2, curve=curve.linear)
                        destroy(target.entity, delay=0.2)
                        popal += 1
                        target.entity.collider = None
                elif Begin:
                        kop4.color = color.rgb(0.5, 0.5, 0.5, 1)
                        kop4.animate_color(color.rgb(1, 1, 0.1, 0.5), duration=0.1, delay=0.1)
                        popal -= 1
def update():
        global speed, speed_not, popal, score, Score, game_over, Begin, highscore, high
        if speed_not == 1:
                speed = speed * 0.999
                speed_not = 0
        if popal == 1:
                popal = 0
                score += 10
                Score.text = f'score: {score}'
                if high < score:
                        high = score
                        highscore.text = f'high score: {high}'
        elif popal == -1:
                popal = 0
                score -= 10
                Score.text = f'score: {score}'
                if high < score:
                        high = score
                        highscore.text = f'high score: {high}'
        if score <= 0 and Begin:
                game_over.enabled = True
                Begin = False
        speed_text.text = f'speed: {int(600 - ((speed * 100)//1))}'
        print(speed)
app.run()
