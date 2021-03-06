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
boost = Sprite("boost.png", 1)
ball.x = janela.width / 2 - ball.width / 2
ball.y = janela.height / 2 - ball.height / 2

teclado = Window.get_keyboard()

boostPosX = random.randint(100, 700)
boostPosY = random.randint(100, 500)

boost.set_position(boostPosX, boostPosY)

paddleE.x = 0
paddleE.y = janela.height / 2 - ball.height / 2

paddleD.x = janela.width - paddleD.width
paddleD.y = janela.height / 2 - ball.height / 2

player = 0
cpu = 0

relogio = 0
contadorFrames = 0
fps = 0

velx = 270
vely = 270
velPadE = 300
velPadD = 300
dist = 2

# game loop
while True:
    relogio += janela.delta_time()
    contadorFrames += 1
    if relogio >= 1:
        fps = int(contadorFrames / relogio)
        relogio = 0
        contadorFrames = 0

    ball.move_x(velx * janela.delta_time())
    ball.move_y(vely * janela.delta_time())

    # IA
    if ball.x >= (janela.width / 1.28):
        if ball.y < paddleD.y:
            paddleD.y = paddleD.y - velPadD * janela.delta_time()
        else:
            paddleD.y = paddleD.y + velPadD * janela.delta_time()

    if teclado.key_pressed("w"):
        if paddleE.y >= 0:
            paddleE.y -= velPadE * janela.delta_time()
    if teclado.key_pressed("s"):
        if (paddleE.y + paddleE.height) <= janela.height:
            paddleE.y += velPadE * janela.delta_time()

    # Game Physics
    if ball.x + ball.width + dist >= janela.width:
        ball.move_x(-dist)
        velx = -velx
    if ball.y + ball.height + dist >= janela.height:
        ball.move_y(-dist)
        vely = -vely

    if ball.x <= 0:
        ball.move_x(dist)
        velx = -velx
    if ball.y <= 0:
        ball.move_y(dist)
        vely = -vely

    if math.floor(ball.x) <= 0:
        cpu += 1
        velx = 270
        vely = 270
        velx = -velx
        vely = -vely
        ball.x = janela.width / 2 - ball.width / 2
        ball.y = janela.height / 2 - ball.height / 2

    if math.floor(ball.x + ball.width + dist + 1) >= janela.width:
        player += 1
        velx = 270
        vely = 270
        velx = -velx
        vely = -vely
        ball.x = janela.width / 2 - ball.width / 2
        ball.y = janela.height / 2 - ball.height / 2

    if ball.collided(paddleE):
        rd = random.randint(0, 1)
        ball.move_x(dist)
        ball.move_y(dist)
        velx = -270
        vely = -270
        velx = -velx
        if rd == 1:
            vely = -vely

    if ball.collided(paddleD):
        rd = random.randint(0, 1)
        ball.move_x(-dist)
        ball.move_y(-dist)
        velx = 270
        vely = 270
        velx = -velx
        if rd == 1:
            vely = -vely

    if ball.collided(boost):
        velx *= 1.25
        vely *= 1.25
        boostPosX = random.randint(100, 700)
        boostPosY = random.randint(100, 500)
        boost.set_position(boostPosX, boostPosY)

    background.draw()
    ball.draw()
    paddleE.draw()
    paddleD.draw()
    boost.draw()
    janela.draw_text(f" Player: {player} | CPU: {cpu}", (janela.width / 2) - 105, 10, 20)
    janela.draw_text(f"FPS: {fps}", janela.width - 200, 10, 20)

    janela.update()
