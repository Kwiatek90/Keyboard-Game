import pygame 
from sys import exit
from random import randint, choice
import string

class Game_stats():
    def __init__(self):
        self.lives = 3 
        self.score = 0
        self.level = 1
        self.letter_generation_time = 750
        self.letter_generation_y = -60
        self.letter_speed = 2
        self.game_active = False
        
        #Score za poziom
        self.level_1_score = 10
        self.level_2_score = 20
        self.level_3_score = 40
        self.level_4_score = 60
        
    def check_lives(self):
        if self.lives == 0:
            self.game_active = False
            letters_group.empty()
            
    def difficult(self):
        if self.score >= 1000:
            self.score += self.level_4_score
            self.level = 4
            self.letter_generation_time = 100
            self.letter_generation_y = -15
            self.letter_speed = 5
        elif self.score >= 400:
            self.score += self.level_3_score
            self.level = 3
            self.letter_generation_time = 250
            self.letter_generation_y = -30
            self.letter_speed = 4
        elif self.score >= 100:
            self.score += self.level_2_score
            self.level = 2
            self.letter_generation_time = 500
            self.letter_generation_y = -45
            self.letter_speed = 3
        elif self.score >= 0:
            self.score += self.level_1_score
              
    def update(self):
        self.check_lives()

class Letter(pygame.sprite.Sprite):
    def __init__(self, letter):
        super().__init__()
        self.font = pygame.font.Font('graphics/fonts/Blomberg.otf', 50)
        self.image = self.font.render(f"{letter}", False, 'White')
        self.level = game_stats.letter_generation_y
        self.rect = self.image.get_rect(center = (choice([number for number in range(50, 950, 50)]), randint(self.level, -5)))
        self.letter_click = "K_" + str(letter).lower()
        
    def kill_letter(self):
        global score
        keys = pygame.key.get_pressed()
        for letter in string.ascii_lowercase:
            if keys[getattr(pygame, f"K_{letter}")] and self.letter_click == f"K_{letter}":
                self.kill()#tutaj if zalezne od levelu
                game_stats.difficult()
                   
    def destroy(self):
        if self.rect.y >= 500:
            self.kill()
            game_stats.lives -= 1
                   
    def update(self):
        self.rect.y += game_stats.letter_speed
        self.destroy()
        self.kill_letter()
        

def update_score():
    score_text = text_game_font.render(f'Score: {game_stats.score}', False, 'White')
    score_text_rect = score_text.get_rect(center = (490, 455))
    screen.blit(score_text, score_text_rect)
    return game_stats.score

def update_lives():
    lives_text = text_game_font.render(f'Lives: {game_stats.lives}', False, 'White')
    lives_text_rect = lives_text.get_rect(center = (340, 455))
    screen.blit(lives_text, lives_text_rect)
    return game_stats.lives

def update_level():
    level_text = text_game_font.render(f'Level: {game_stats.level}', False, 'White')
    level_text_rect = level_text.get_rect(center = (630, 455))
    screen.blit(level_text, level_text_rect)
    return game_stats.level

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Letter Strike")
clock = pygame.time.Clock()

game_stats = Game_stats()
letters_group = pygame.sprite.Group()

#Font
text_game_font = pygame.font.Font('graphics/fonts/Blomberg.otf', 25)
text_intro_font = pygame.font.Font('graphics/fonts/Blomberg.otf', 50)

#Game background
background_surf = pygame.image.load('graphics/background_game.jpg')

#Board
board = pygame.image.load('graphics/board.png').convert_alpha()
board_rect = board.get_rect(midbottom = (470, 580))

#Intro screen
game_name = text_intro_font.render('Letter strike', False, 'White')
game_name_rect = game_name.get_rect(center = (500, 100))

hand = pygame.image.load("graphics/hand.png").convert_alpha()
hand = pygame.transform.rotozoom(hand, 0, 0.75)
hand_rect = hand.get_rect(center = (600, 250))

letter_image = text_intro_font.render('ABC', False, 'White')
letter_image = pygame.transform.rotozoom(letter_image, 45, 2)
letter_image_rect = letter_image.get_rect(center = (400, 250))

game_message = text_intro_font.render('Press space to run game ',False, 'White')
game_message_rect = game_message.get_rect(center = (500, 400))

#Timer to generate letters
letter_timer = pygame.USEREVENT + 1
pygame.time.set_timer(letter_timer, game_stats.letter_generation_time)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_stats.game_active:
            if event.type == letter_timer:
                letters_group.add(Letter(choice(list(string.ascii_uppercase))))
                
        else:
             if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_stats.game_active = True
                game_stats.lives = 3 
                game_stats.score = 0
                game_stats.level = 1
                game_stats.letter_generation_time = 750
                game_stats.letter_generation_y = -60
                game_stats.letter_speed = 2
            
                
    if game_stats.game_active:
        screen.blit(background_surf, (0,0))
        screen.blit(board, board_rect)
        level = update_level()
        lives = update_lives()
        score = update_score()
        game_stats.update()

        letters_group.draw(screen)
        letters_group.update()

    else:
        screen.fill('#c9934d')
        screen.blit(game_name, game_name_rect)
        screen.blit(hand, hand_rect)
        screen.blit(letter_image,letter_image_rect)
        
        score_message = text_intro_font.render(f"Your score: {game_stats.score}", False, 'White')
        score_message_rect = score_message.get_rect(center = (500, 400))
        
        if game_stats.score == 0: screen.blit(game_message, game_message_rect)
        else: screen.blit(score_message, score_message_rect)
        
    pygame.display.update()
    clock.tick(60)
        
            
            