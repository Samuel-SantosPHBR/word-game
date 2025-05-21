import pygame
from typing import Tuple
from engine.InputKeys import InputKeys

class InputManager:
    def __init__(self):
        self.keys_down = {}
        self.keys_up = {}
        self.mouse_buttons_down = {}
        self.mouse_buttons_up = {}
        self.keys_hold = {}
        self.mouse_pos = (0, 0)

    def update(self, events):
        self.keys_down.clear()
        self.keys_up.clear()
        self.mouse_buttons_down.clear()
        self.mouse_buttons_up.clear()

        for event in events:
            if event.type == pygame.KEYDOWN:
                self.keys_down[event.key] = True
                self.keys_hold[event.key] = True

            elif event.type == pygame.KEYUP:
                self.keys_up[event.key] = True
                self.keys_hold.pop(event.key, None)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_buttons_down[event.button] = True
                self.mouse_pos = pygame.mouse.get_pos()

            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_buttons_up[event.button] = True
                self.mouse_pos = pygame.mouse.get_pos()

    def is_key_down(self, key: InputKeys) -> bool:
        return self.keys_down.get(key.value, False)

    def is_key_up(self, key: InputKeys) -> bool:
        return self.keys_up.get(key.value, False)

    def is_any_key_hold(self) -> bool:
        return len(self.keys_hold) > 0 

    def is_mouse_button_down(self, button: InputKeys) -> bool:
        return self.mouse_buttons_down.get(button.value, False)

    def is_mouse_button_up(self, button: InputKeys) -> bool:
        return self.mouse_buttons_up.get(button.value, False)

    def get_mouse_position(self) -> Tuple[int, int]:
        return self.mouse_pos
