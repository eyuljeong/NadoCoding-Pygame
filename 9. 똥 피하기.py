# Quiz) 하늘에서 떨어지는 똥 피하기 게임을 만드시오

# [게임 조건]
# 1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
# 2. 똥은 화면 가장 위에서 떨어짐, x 좌표는 매번 랜덤으로 설정
# 3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
# 4. 캐릭터가 똥과 충돌하면 게임 종료
# 5. FPS 는 30 으로 고정

# [게임 이미지]
# 1. 배경 : 640 * 480 (세로 가로) - background.png
# 2. 캐릭터 : 70 * 70 - character.png
# 3. 똥 : 70 * 70 - ddong.png

import pygame
from random import * 

##################################################

# 기본 초기화 (반드시 해야 하는 것들)

pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥을 피하거라..")

# FPS
clock = pygame.time.Clock()

##################################################

# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트 등)

# 배경 만들기
background = pygame.image.load("C:\\Users\\eyulj\\Desktop\\PythonWorkspace\\나도코딩 게임 개발\\background.png")

# 캐릭터 만들기
character = pygame.image.load("C:\\Users\\eyulj\\Desktop\\PythonWorkspace\\나도코딩 게임 개발\\character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height

character_to_x = 0
character_speed = 0.6

# 똥 만들기
ddong = pygame.image.load("C:\\Users\\eyulj\\Desktop\\PythonWorkspace\\나도코딩 게임 개발\\ddong.png")
ddong_size = ddong.get_rect().size 
ddong_width = ddong_size[0]
ddong_height = ddong_size[1]
ddong_x_pos = randint(0, screen_width - ddong_width)
ddong_y_pos = 0

ddong_to_y = 0
ddong_speed = 0.6

# 이벤트 루프
running = True
while running:
    dt = clock.tick(1000)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: 
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed

        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x * dt
    ddong_y_pos += ddong_to_y * dt
    
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if ddong_y_pos > screen_height:
        ddong_x_pos = randint(0, screen_width - ddong_width) 
        ddong_y_pos = 0 

    ddong_to_y = ddong_speed
    
    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    ddong_rect = ddong.get_rect()
    ddong_rect.left = ddong_x_pos
    ddong_rect.top = ddong_y_pos

    if character_rect.colliderect(ddong_rect):
        print("충돌했어요")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0, 0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(ddong, (ddong_x_pos, ddong_y_pos))
    pygame.display.update() 

pygame.time.delay(2000)
pygame.quit()