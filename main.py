import pygame, sys
pygame.init()
#värv
lBlue = [153, 204, 255]

# ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")
screen.fill(lBlue)
clock = pygame.time.Clock()
score = 0

# kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 4
speedX2, speedY2 = 3,0
posX2,posY2 = 300,400

#pildid
ball = pygame.image.load("ball.png")
ball = pygame.transform.scale(ball, [20,20])
ball_rect = pygame.Rect(posX,posY,20,20)
pad = pygame.image.load("pad.png")
pad = pygame.transform.scale(pad, [120,20])
pad_rect = pygame.Rect(posX2,posY2,120,20)

gameover = False
while not gameover:
    # fps
    clock.tick(60)
    # pildi lisamine ekraanile
    screen.blit(ball, (posX, posY))
    screen.blit(pad, (posX2, posY2))
    pall = pygame.Rect(posX,posY,20,20)
    pad_rect = pygame.Rect(posX2, posY2, 120, 20)
    #pall
    posX += speedX
    posY += speedY
    posX2 += speedX2
    posY2 += speedY2
    #Score
    screen.blit(pygame.font.Font(None, 30).render(f"Score: {score}", True, [255, 255, 255]),
                [10, 20])
    if posX > screenX - ball.get_rect().width or posX < 0:
        speedX = -speedX
    if posY > screenY - ball.get_rect().height or posY < 0:
        speedY = -speedY
    if posY > screenY -ball.get_rect().height:
        score-=1
    if posX2 > screenX - pad.get_rect().width or posX2 < 0:
        speedX2 = -speedX2

    if pall.colliderect(pad_rect) and speedY > 0:
        speedY = -speedY
        score +=1

    pygame.display.flip()
    screen.fill(lBlue)
pygame.quit()
