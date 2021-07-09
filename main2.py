from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import math
import random

# inicialização
janela = Window(800, 600)
janela.set_title("Pong")
background = GameImage("fundo.jpg")
paddleE = Sprite("paddle.png")
paddleD = Sprite("paddle.png")
ball = Sprite("bola.png", 1)
ball.x = janela.width / 2 - ball.width / 2
ball.y = janela.height / 2 - ball.height / 2

teclado = Window.get_keyboard()

paddleE.x = 0
paddleE.y = janela.height / 2 - ball.height / 2

paddleD.x = janela.width - paddleD.width
paddleD.y = janela.height / 2 - ball.height / 2

player_1 = 0
player_2 = 0

num = random.randint(0, 1)

velx = 270
vely = 270
velPadE = 300
velPadD = 300
dist = 2

# game loop
while(True):
    ball.move_x(velx * janela.delta_time())
    ball.move_y(vely * janela.delta_time())

    if (teclado.key_pressed("UP")):
        if (paddleD.y >= 0):
            paddleD.y -= velPadE * janela.delta_time()
    if (teclado.key_pressed("DOWN")):
        if ((paddleD.y + paddleD.height) <= janela.height):
            paddleD.y += velPadD * janela.delta_time()

    if (teclado.key_pressed("w")):
        if (paddleE.y >= 0):
            paddleE.y -= velPadE * janela.delta_time()
    if (teclado.key_pressed("s")):
        if ((paddleE.y + paddleE.height) <= janela.height):
            paddleE.y += velPadE * janela.delta_time()

    # Game Physics
    if(ball.x + ball.width + dist >= janela.width):
        ball.move_x(-dist)
        velx = -velx
    if(ball.y + ball.height + dist >= janela.height):
        ball.move_y(-dist)
        vely = -vely

    if (ball.x <= 0):
        ball.move_x(dist)
        velx = -velx
    if (ball.y <= 0):
        ball.move_y(dist)
        vely = -vely

    if(math.floor(ball.x) <= 0):
        player_2 += 1
        num = random.randint(0, 1)
        if(num == 1):
            velx = -velx
            vely = -vely
        ball.x = janela.width / 2 - ball.width / 2
        ball.y = janela.height / 2 - ball.height / 2

    if math.floor(ball.x + ball.width + dist + 1) >= janela.width:
        player_1 += 1
        num = random.randint(0, 1)
        if (num == 1):
            velx = -velx
            vely = -vely
        ball.x = janela.width / 2 - ball.width / 2
        ball.y = janela.height / 2 - ball.height / 2

    if ball.collided(paddleE):
        ball.move_x(dist)
        ball.move_y(dist)
        velx = -velx

    if ball.collided(paddleD):
        ball.move_x(-dist)
        ball.move_y(-dist)
        velx = -velx

    background.draw()
    ball.draw()
    paddleE.draw()
    paddleD.draw()
    janela.draw_text(f" Player 1: {player_1} | Player 2: {player_2}", (janela.width / 2) - 105, 10, 20)

    janela.update()