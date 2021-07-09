from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
import math

# inicialização
janela = Window(800, 600)
janela.set_title("Pong")
# janela.set_background_color([255, 255, 0])
background = GameImage("fundo.jpg")
paddleE = Sprite("paddle.png")
paddleD = Sprite("paddle.png")
ball = Sprite("bola.png", 1)
ball.x = janela.width / 2 - ball.width / 2
ball.y = janela.height / 2 - ball.height / 2

paddleE.x = 0
paddleE.y = janela.height / 2 - ball.height / 2

paddleD.x = janela.width - paddleD.width
paddleD.y = janela.height / 2 - ball.height / 2

player_1 = 0
player_2 = 0

velx = 300
vely = 300
velPadE = 0.3
velPadD = 0.3
dist = 2

# game loop
while(True):
    ball.move_x(velx * janela.delta_time())
    ball.move_y(vely * janela.delta_time())

    paddleE.move_key_y(velPadE)

    paddleD.move_y(velPadD)

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

    if(math.floor(ball.x) >= 757):
        player_1 += 1

    if (paddleE.y + paddleE.height >= janela.height) or (paddleE.y <= 0):
        velPadE = -velPadE

    if (paddleD.y + paddleD.height >= janela.height) or (paddleD.y <= 0):
        velPadD = -velPadD

    if ball.collided(paddleE):
        ball.move_x(dist)
        ball.move_y(dist)
        velx = -velx
        vely = -vely

    if ball.collided(paddleD):
        ball.move_x(-dist)
        ball.move_y(-dist)
        velx = -velx
        vely = -vely

    background.draw()
    ball.draw()
    paddleE.draw()
    paddleD.draw()
    janela.draw_text(f" Player 1: {player_1} | Player 2: {player_2}", (janela.width / 2) - 105, 10, 20)

    janela.update()