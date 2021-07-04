from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

# inicialização
janela = Window(800, 600)
janela.set_title("Pong")
# janela.set_background_color([255, 255, 0])
background = GameImage("fundo.jpg")
paddle = Sprite("paddle.png")
cpupaddle = Sprite("paddle.png")
ball = Sprite("bola.png", 1)
ball.x = janela.width / 2 - ball.width / 2
ball.y = janela.height / 2 - ball.height / 2

paddle.x = 0
paddle.y = janela.height / 2 - ball.height / 2

cpupaddle.x = 760
cpupaddle.y = janela.height / 2 - ball.height / 2

player = 0
cpu = 0

velx = 0.3
vely = 0.3
velpaddley = 0.3
velpaddlecpu = 0.3

# game loop
while(True):
    ball.move_x(velx)
    ball.move_y(vely)

    paddle.move_key_y(velpaddley)

    cpupaddle.move_y(velpaddlecpu)

    # Game Physics
    if(ball.x + ball.width >= janela.width) or (ball.x <= 0):
        velx = -velx
    if(ball.y + ball.height >= janela.height) or (ball.y <= 0):
        vely = -vely

    if(ball.x <= 0):
        cpu += 1

    if(ball.x >= 760):
        player += 1

    if (paddle.y + paddle.height >= janela.height) or (paddle.y <= 0):
        velpaddley = -velpaddley

    if (cpupaddle.y + cpupaddle.height >= janela.height) or (cpupaddle.y <= 0):
        velpaddlecpu = -velpaddlecpu

    if ball.collided(paddle):
        velx = -velx
        vely = -vely

    if ball.collided(cpupaddle):
        velx = -velx
        vely = -vely

    background.draw()
    ball.draw()
    paddle.draw()
    cpupaddle.draw()
    janela.draw_text(f" Player: {player} | CPU: {cpu}", (janela.width / 2) - 80, 10, 20)

    janela.update()



