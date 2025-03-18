import pygame
from engine.InputManager import InputManager  

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Teste do InputManager")

input_manager = InputManager()

running = True
while running:
    input_manager.update()

    if input_manager.is_key_down(pygame.K_ESCAPE):
        print("Tecla ESC pressionada")
        running = False

    if input_manager.is_key_down(pygame.K_SPACE):
        print("Tecla ESPAÇO pressionada")

    if input_manager.is_key_up(pygame.K_a):
        print(pygame.K_ESCAPE)

    if input_manager.is_any_key_hold():
        print("Tecla ou botão do mouse está sendo mantido pressionado")

    if input_manager.is_mouse_button_down(pygame.BUTTON_LEFT):
        print("Botão esquerdo do mouse pressionado")
        print(f"Posição do mouse: {input_manager.get_mouse_position()}")

    if input_manager.is_mouse_button_up(pygame.BUTTON_RIGHT):
        print("Botão direito do mouse solto")
        print(f"Posição do mouse: {input_manager.get_mouse_position()}")

    screen.fill((0, 0, 0))    
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()