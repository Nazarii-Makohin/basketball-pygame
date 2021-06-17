import pygame
from random import randint

pygame.init()
# умови для віконечка гри(екрану)
screen_width = 1080
screen_height = 720
display_output = [screen_width, screen_height]
screen = pygame.display.set_mode(display_output)
clock = pygame.time.Clock()
pygame.display.set_caption("SimpleGame")
# умови для мяча
basketball = pygame.image.load("basketball.png")
x = randint(0, screen_width)
y = 0
radius = 100
ball_rep_x = x + 50
ball_rep_y = y + 50
speed = 5
# умови для корзини
basket = pygame.image.load("basket.png")
basket_width = 125
basket_pos_x = 450
basket_pos_y = 600
basket_speed = 8
basket_rep_x = [basket_pos_x + 31, basket_pos_x + 94]
basket_rep_y = [basket_pos_y + 14, basket_pos_y + 20]

# умови для шрифту
black = (0, 0, 0)
gray = (200, 200, 200)

text_x = 15
text_y = 15
font = pygame.font.Font("freesansbold.ttf", 40)

play = True
#тут я добавляв звук при попаданні мяча в корзину
tick = pygame.mixer.Sound("tick.wav")

score = 0

#закриття гри на хрестик і рух корзини стрілками
def check_for_event():
    global play, basket_pos_x, basket_pos_y
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        basket_pos_x -= basket_speed
    if keys[pygame.K_RIGHT]:
        basket_pos_x += basket_speed


def show_images():
    global basket_rep_x, basket_rep_y
    screen.blit(basketball, (x, y))
    screen.blit(basket, (basket_pos_x, basket_pos_y))
    basket_rep_x = [basket_pos_x + 31, basket_pos_x + 94]
    basket_rep_y = [basket_pos_y + 14, basket_pos_y + 20]


def update_ball_pos():
    global y, ball_rep_x, ball_rep_y
    y += speed
    ball_rep_x = x + 50
    ball_rep_y = y + 50
    initialise_ball()

#створення мячів
def initialise_ball():
    global x, y
    if y > screen_height - radius:
        y = 0
        x = randint(0, screen_width)

#кордон корзини
def enforce_border():
    global x, y, basket_pos_x, basket_pos_y
    if x < 0:
        x = 0
    if x > screen_width - radius:
        x = screen_width - radius
    if y < 0:
        y = 0
    if y > screen_height - radius:
        y = screen_height - radius

    if basket_pos_x < 0:
        basket_pos_x = 0
    if basket_pos_x > screen_width - basket_width:
        basket_pos_x = screen_width - basket_width


def check_for_score():
    global score
    if ball_rep_x in range(basket_rep_x[0], basket_rep_x[1]) and ball_rep_y in range(basket_rep_y[0], basket_rep_y[1]):
        score += 1
        tick.play()
    elif ball_rep_y in range(basket_rep_y[0], basket_rep_y[1]) and ball_rep_x not in range(basket_rep_x[0], basket_rep_x[1]):
        score = 0


def show_score():
    score_disp = font.render("Score " + str(score), True, black)
    screen.blit(score_disp, (text_x, text_y))


while play:
    clock.tick(60)
    screen.fill(gray)
    check_for_event()
    update_ball_pos()
    enforce_border()
    show_images()
    check_for_score()
    show_score()
    pygame.display.flip()
pygame.quit()